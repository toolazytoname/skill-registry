# Personal Skill Registry

> 公开 Skill 台账：索引聚合，不复制或接管来源仓库。

结构化数据的唯一来源是 `registry.json`；此首页由 `scripts/catalog.py` 生成。

## 导航

- [维护约定](docs/conventions.md)
- [首轮盘点与待确认项](reports/inventory.md)
- [变更日志](CHANGELOG.md)

当前登记 **9** 个 Skill。来源路径检查不等于运行验证，也不等于原创认定。

## Agent 编排

| Skill | 用途 | 来源可见性 |
| --- | --- | --- |
| [cli-worker-delegation](https://github.com/toolazytoname/cli-worker-delegation/blob/e774cf279d34be531fb003b2618a2ab21852efe7/SKILL.md) | 将有界本地任务委派给 Cursor 或 Grok CLI；显式授权编辑，主 agent 独立核验。 | public |

## 网络与家庭基础设施

| Skill | 用途 | 来源可见性 |
| --- | --- | --- |
| [reality-handshake](https://github.com/toolazytoname/reality-handshake/blob/9ecdaa0990eb837e4c1b05a72561fa74daaa45f5/SKILL.md) | Real-world hands-on protocols — practical tooling for everyday problems. | public |
| [home-nas-skill](https://github.com/toolazytoname/home-nas-skill/blob/d8fa92883957e19c45654ba3977d0fdb1887591c/SKILL.md) | 把旧 x86 小主机搭成全自动家庭媒体中心：*arr + Jellyfin + Immich + 音乐书库。含大陆镜像/代理与弱 CPU 1080p 直放的实战手册（Claude Skill）。 | public |

## 数据与知识管理

| Skill | 用途 | 来源可见性 |
| --- | --- | --- |
| [yinxiang-export](https://github.com/toolazytoname/yinxiang-export/blob/f1df32041a404ba794c785d4a179978463ba4fc6/.agents/skills/yinxiang-export/SKILL.md) | Archive-first Yinxiang local export: preserved source, Markdown reading layer, and an Agent Skill. | public |

## 生活工具

| Skill | 用途 | 来源可见性 |
| --- | --- | --- |
| [cn-electronics-shop](https://github.com/toolazytoname/cn-electronics-shop/blob/0755d84cbcd96131b0d8d4cf9f027d24faba6d67/SKILL.md) | 国内数码选购顾问 Skill：拆需求、京东/天猫/闲鱼比价、验闲鱼、叠国补和大促 | public |

## 部署与运维

| Skill | 用途 | 来源可见性 |
| --- | --- | --- |
| [dsh-deploy](https://github.com/toolazytoname/dsh-deploy/blob/c46fe9497f31c7e6b87ec171cad086e0e94e0bd4/SKILL.md) | Skill and templates to deploy DeepSeek Harness (dsh web) behind nginx + Tailscale Funnel, with Safari cookie auth and remote-settings patches | public |
| [paseo-relay-deploy](https://github.com/toolazytoname/paseo-relay-deploy/blob/ebf8f281520c2a65dd5b4e716a5f6d878a3508a7/SKILL.md) | Skill: 自托管 Paseo WebSocket 中继，让手机 App 在不开 Tailscale 的情况下控制多台工作机。含 keepmind9 空 sync/keepalive 补丁、中国大陆云 Funnel 443、可选 Mihomo TUN fail-close。 | public |
| [happy-relay-deploy](https://github.com/toolazytoname/happy-relay-deploy/blob/6cae04982121a25ec4a0470c2e47941d67ecb5ed/SKILL.md) | Kimi skill: 自托管 Happy 中继（happy-server-light）部署与维护 —— 手机远程控制多台机器上的 Claude Code。含中国大陆机房未备案域名的 HTTPS 绕行方案、v3 API 兼容补丁、运维排障手册。 | public |

## 内容与媒体

| Skill | 用途 | 来源可见性 |
| --- | --- | --- |
| [grok-imagine-on-plan](https://github.com/toolazytoname/grok-imagine-on-plan/blob/c5f2d62a5de591183c1e4c2225def2dee087ba8e/SKILL.md) | Agent skill: generate images and videos on SuperGrok/Grok coding-plan quota via Grok Build tools | public |

## 本地维护

```sh
python3 scripts/catalog.py
python3 scripts/catalog.py --check
```

第一条校验数据并生成首页；第二条只检查数据和首页是否一致。不联网、不安装、不覆盖本地 Skill。
