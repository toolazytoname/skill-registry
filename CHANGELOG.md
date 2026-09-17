# 历史

## 2026-09-16 — 登记 agent-progress

- 优化通用进度看板 skill：渲染升级为统计卡 + 阶段条形图 + 状态圆点 + 完成清单的深色看板，新增 `status` 摘要命令（文本 / `--json`）。
- 独立工程发布为 public 仓库 toolazytoname/agent-progress（18 项单元测试通过，render 结果经无头浏览器截图人工验收）。
- 登记进索引，分类「Agent 编排」。

## 2026-09-12 — 初始化

- 建立私有 Skill 索引，首批登记 9 个条目。
- 核对 8 个既有来源的 Skill 路径和默认分支。
- 发布 cli-worker-delegation，34 项模拟 CLI 单元测试通过。
- 增加导航生成与一致性校验；记录未覆盖范围与待确认项。

## 2026-09-12 — 公开发布

- 按用户明确授权，将 cli-worker-delegation 和 skill-registry 改为 public。
- 更新登记表可见性、首页与维护说明；保留初始化历史。

## 2026-09-17 — 登记 appstore-submit

- 新增 appstore-submit（private，Agent 编排）：iOS App 上架 App Store 端到端流程 Skill，源自 2026-09-17 一次真实上架复盘（提交审核成功，状态「正在等待审核」）。
- 语法校验：shell/plist lint 通过；流程本身经真实运行验证，记录于 runtime_verified_at。
- 仓库可见性未明确时按维护约定默认 private，后续可由用户转 public。
