#!/usr/bin/env bash
# 一键安装 skill：从 registry.json 解析条目 → 本地 git 工作副本（或克隆 GitHub）→
# 软链进唯一存储 ~/.agents/skills/（~/.zcode/skills 与 ~/.claude/skills 已是它的目录级软链）。
#
# 用法：
#   install-skill.sh <skill-id>            # 克隆/更新 registry 记录的 repo 并安装
#   install-skill.sh <skill-id> <本地路径>  # 软链指定本地 git 工作副本（单一事实源）
#   install-skill.sh --list                # 列出 registry 全部 skill 与安装状态
set -euo pipefail
REG_DIR="$(cd "$(dirname "$0")/.." && pwd)"
REG="$REG_DIR/registry.json"
STORE="$HOME/.agents/skills"
WORK="$HOME/.skill-worktrees"   # 无本地副本时的克隆缓存
export REG_DIR

ensure_layout() {
  mkdir -p "$STORE"
  # 目录级软链（幂等）：~/.zcode/skills 与 ~/.claude/skills -> ~/.agents/skills
  for d in "$HOME/.zcode/skills" "$HOME/.claude/skills"; do
    if [ -L "$d" ]; then continue; fi
    if [ -d "$d" ]; then
      # 合并残余内容后替换（只搬 STORE 里没有的）
      for item in "$d"/*; do
        [ -e "$item" ] || continue
        name="$(basename "$item")"
        [ -e "$STORE/$name" ] || mv "$item" "$STORE/$name"
      done
      rm -rf "$d"
    fi
    ln -s "$STORE" "$d"
  done
}

if [ "${1:-}" = "--list" ]; then
  python3 - <<'PY'
import json, os
d = json.load(open(os.path.join(os.environ['REG_DIR'], 'registry.json')))
for s in d["skills"]:
    inst = os.path.exists(os.path.expanduser("~/.agents/skills/") + s["id"])
    print(f"{'[installed]' if inst else '[   --   ]'} {s['id']:<28} {s.get('repo','')}")
PY
  exit 0
fi

[ $# -ge 1 ] || { echo "usage: $0 <skill-id> [local-path]  |  $0 --list"; exit 1; }
ID="$1"; LOCAL="${2:-}"
ensure_layout

REPO_BRANCH="$(python3 - "$ID" <<'PY'
import json, os, sys
d = json.load(open(os.path.join(os.environ['REG_DIR'], 'registry.json')))
for s in d["skills"]:
    if s["id"] == sys.argv[1]:
        print(s.get("repo", ""), s.get("default_branch", "main"))
        break
else:
    sys.exit("not in registry")
PY
)"
REPO="${REPO_BRANCH%% *}"; BRANCH="${REPO_BRANCH##* }"
[ -n "$REPO" ] || { echo "skill '$ID' not found in registry"; exit 1; }

if [ -n "$LOCAL" ]; then
  SRC="$LOCAL"
elif [ -d "$WORK/$ID" ]; then
  git -C "$WORK/$ID" fetch --quiet origin
  git -C "$WORK/$ID" reset --hard --quiet "origin/$BRANCH"
  SRC="$WORK/$ID"
else
  mkdir -p "$WORK"
  git clone --quiet "git@github.com:${REPO}.git" "$WORK/$ID"
  SRC="$WORK/$ID"
fi

[ -f "$SRC/SKILL.md" ] || { echo "no SKILL.md in $SRC"; exit 1; }
ln -sfn "$SRC" "$STORE/$ID"
echo "installed: $STORE/$ID -> $SRC"
echo "visible via: ~/.agents/skills, ~/.zcode/skills, ~/.claude/skills (目录级软链)"
