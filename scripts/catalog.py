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
           '> 私有 Skill 台账：索引聚合，不复制或接管来源仓库。', '',
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
            '第一条校验数据并生成首页；第二条只检查数据和首页是否一致。不联网、不安装、不覆盖本地 Skill。', '']
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
