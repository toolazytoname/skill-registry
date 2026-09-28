#!/usr/bin/env python3
"""Validate registry and generate/check the human-readable index. Stdlib only."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def render():
    data = json.loads((ROOT / 'registry.json').read_text())
    assert data['schema_version'] == 1, 'unsupported schema'
    skills = data['skills']
    ids = set()
    groups = {}
    for s in skills:
        for key in ('id', 'summary', 'repo', 'skill_path', 'category', 'visibility', 'origin', 'source_checked_at'):
            assert s.get(key), f'missing {key}: {s}'
        assert s['id'] not in ids, f'duplicate: {s["id"]}'
        ids.add(s['id'])
        assert s['visibility'] in ('public', 'private')
        assert len(s['repo'].split('/')) == 2
        assert s['skill_path'].endswith('SKILL.md')
        groups.setdefault(s['category'], []).append(s)
    out = ['# Personal Skill Registry', '',
           '> 公开 Skill 台账：索引聚合，不复制或接管来源仓库。', '',
           '结构化数据的唯一来源是 `registry.json`；此首页由 `scripts/catalog.py` 生成。', '',
           '## 导航', '',
           '- [维护约定](docs/conventions.md)',
           '- [首轮盘点与待确认项](reports/inventory.md)',
           '- [变更日志](CHANGELOG.md)', '',
           f'当前登记 **{len(skills)}** 个 Skill。来源路径检查不等于运行验证，也不等于原创认定。', '']
    for category, entries in groups.items():
        out += [f'## {category}', '', '| Skill | 用途 | 来源可见性 |', '| --- | --- | --- |']
        for s in entries:
            url = f'https://github.com/{s["repo"]}/blob/{s["observed_commit"]}/{s["skill_path"]}'
            summary = s['summary'].replace('|', '\\|').replace('\n', ' ')
            out.append(f'| [{s["id"]}]({url}) | {summary} | {s["visibility"]} |')
        out.append('')
    out += ['## 本地维护', '', '```sh', 'python3 scripts/catalog.py', 'python3 scripts/catalog.py --check', '```', '',
            '第一条校验数据并生成首页；第二条只检查数据和首页是否一致。不联网、不安装、不覆盖本地 Skill。', '',
            '## 一键安装布局（2026-09-18 起）', '',
            '本机 skill 发现路径已整合为**单一存储**：`~/.agents/skills/` 为唯一真实目录，',
            '`~/.zcode/skills` 与 `~/.claude/skills` 均为指向它的**目录级软链**——装一个 skill',
            '只需放进 `~/.agents/skills/`，三个运行时（ZCode / Claude Code / CLI agents）全部可见。', '',
            '- 安装/更新：`scripts/install-skill.sh <skill-id> [本地git工作副本路径]`',
            '  - 不给本地路径则从 registry 记录的 GitHub 仓库克隆到 `~/.skill-worktrees/` 再软链；',
            '  - 给本地路径（如项目里的工作副本）则直接软链它，保持单一事实源，更新自动生效。',
            '- 查看状态：`scripts/install-skill.sh --list`',
            '- registry 条目约定：`installed_paths` 记录安装点；`install_type` 记录软链目标。', '']
    return '\n'.join(out)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    expected = render()
    path = ROOT / 'README.md'
    if args.check:
        if not path.exists() or path.read_text() != expected:
            parser.exit(1, 'README out of date; run python3 scripts/catalog.py\n')
        print('Registry valid; README is current.')
    else:
        path.write_text(expected)
        print('Registry valid; README generated.')

if __name__ == '__main__':
    main()
