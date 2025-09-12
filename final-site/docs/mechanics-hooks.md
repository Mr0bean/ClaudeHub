---
title: "钩子 | ClaudeLog"
---

# 钩子 | ClaudeLog

钩子是 Claude Code 引入的一种新机制，允许基于给定事件（如工具执行、文件更改或部署活动）进行确定性响应。

### 实际应用实现[​](#practical-implementation)

我一直在尝试一些简单的用例，探索如何使用它们来提高现有工作流程的可靠性，例如在将 ClaudeLog 网站部署上线之前运行各种部署前/后的相关活动。

当你在线更新网站时，必须执行各种 SEO 相关活动，例如：

-   **部署你的网站地图**到各种网站管理工具
-   **检查构建过程**没有生成无效的 JSON 模式（不同的网站管理工具对此出奇地敏感）
-   **验证 URL** 都是活跃且格式正确的

这些是简单易得的成果，Claude 根据我现有的部署管道建议我探索将它们实现到我的工作流程中。

* * *

* * *

### 作用域挑战[​](#scoping-challenges)

有趣的是，我发现最棘手的部分是确定激活要求的作用域，使它们不会过早激活。

### 作用域不当的钩子示例[​](#poorly-scoped-hook-example)

```json
{
  "hooks": {
    "postToolUse": {
      "bash": "expensive_validation.sh"
    }
  }
}
```

*这会在任何 bash 命令上触发，即使是简单的 `ls` 或 `pwd` 命令也会运行昂贵的验证*

### 更好的作用域钩子示例 - 智能调度器模式[​](#better-scoped-hook-example---smart-dispatcher-pattern)

```json
{
  "hooks": {
    "postToolUse": {
      "bash": "smart_dispatcher.sh"
    }
  }
}
```

**智能调度器脚本：**

```bash
#!/bin/bash
# smart_dispatcher.sh - Routes to appropriate validation based on command content

if echo "$CLAUDE_TOOL_INPUT" | jq -r '.command' | grep -q "npm run build\|yarn build\|next build"; then
    echo "🏗️  Build detected, running post-build validations..."
    ./validate_build.sh &
    ./check_sitemap.sh &
    ./verify_urls.sh &
    wait
elif echo "$CLAUDE_TOOL_INPUT" | jq -r '.command' | grep -q "git push\|vercel --prod"; then
    echo "🚀 Deployment detected, running SEO checks..."
    ./deploy_sitemap.sh
else
    echo "ℹ️  Standard command, no additional validation needed"
fi
```

*这会基于内容分析智能地路由命令，仅在需要时运行昂贵的操作*

* * *

* * *

### 寻找钩子机会[​](#finding-hook-opportunities)

要找到钩子在你的设置中可能有用的建议，请务必让 Claude 审查你当前的系统并建议钩子的好处。

只是要注意，如果它们不必要地触发，你的 Agent 会变得极其缓慢（不过值得庆幸的是，这不会消耗你的令牌）。

### 可用的触发器[​](#available-triggers)

-   **PreToolUse** - 工具执行前
-   **PostToolUse** - 工具完成后
-   **UserPromptSubmit** - 用户提交提示时
-   **Stop** - Claude Code 代理完成响应时

### 最佳实践[​](#best-practices)

-   **智能调度** - 使用具有智能命令路由的单一入口点，避免性能损失
-   **退出代码检查** - 在 PostToolUse 钩子中验证成功的命令执行（`$CLAUDE_EXIT_CODE` 仅在执行后可用）
-   **并行执行** - 使用 `&` 和 `wait` 并发运行独立验证，以加快处理速度
-   **JSON 输入解析** - 使用 `jq` 提取命令详情（回退优雅地处理缺失字段）
-   **性能监控** - 跟踪钩子执行时间并缓存结果以识别瓶颈
-   **错误处理** - 非关键钩子的优雅失败可防止工作流中断
-   **精确作用域** - 针对特定命令而非广泛的工具类别，以保持响应性

##### 工作流自动化

钩子将被动开发转变为主动自动化。作用域良好的钩子消除了手动部署步骤，并在问题到达生产环境之前就捕获它们。关键是精确的触发模式。

<img src="/img/discovery/036_cl_orange.png" alt="Custom image" style="max-width: 165px; height: auto;" />

* * *

**另请参阅**：[配置](/configuration.html)|[Claude Code 中的钩子是什么](https://docs.anthropic.com/en/docs/claude-code/hooks)

**作者**：[<img src="/img/profiles/inventorblack.png" alt="InventorBlack" style="width: 25px; height: 25px; border-radius: 50%; vertical-align: middle;" /> InventorBlack](https://x.com/inventorblack)|[Command Stick](https://commandstick.com) 的 CTO|[r/ClaudeAi](https://reddit.com/r/ClaudeAi) 的版主

-   [实际应用实现](#practical-implementation)
-   [作用域挑战](#scoping-challenges)
-   [作用域不当的钩子示例](#poorly-scoped-hook-example)
-   [更好的作用域钩子示例 - 智能调度器模式](#better-scoped-hook-example---smart-dispatcher-pattern)
-   [寻找钩子机会](#finding-hook-opportunities)
-   [可用的触发器](#available-triggers)
-   [最佳实践](#best-practices)