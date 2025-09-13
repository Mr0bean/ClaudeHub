---
title: "手表控制示例 | Claude Hub"
---

# 手表控制示例 | Claude Hub

一个展示高级自动化工作流程和Wear OS手表控制命令转换的`CLAUDE.md`示例。


* * *

* * *

```
\# CLAUDE.md

本文件为Claude Code (claude.ai/code)在此代码库中工作时提供指导。

## 重要事项
- 本文档中的所有指令必须遵守，除非明确说明，否则这些指令不是可选的。
- 如果您对文档中的任何内容不确定，请要求澄清。
- 不要编辑超出必要的代码。
- 不要浪费令牌，保持简洁明了。

## 手表控制系统
- 必须执行：每当用户提到"watch control"、"watch-control"或类似变体时，立即毫无疑问地运行watch-control命令。
- 使用以下方式执行：\`bash "/path/to/project/.claude/functions/tools/watch\_control.sh"\`后跟适当的命令行选项
- 您必须使用脚本的确切路径：\`/path/to/project/.claude/functions/tools/watch\_control.sh\`
- 始终将用户的自然语言请求转换为带双短横线的适当命令行选项

### 命令格式转换：
- watch-control系统接受自然语言，但在内部将命令转换为正确格式
- 命令使用双短横线格式（例如，\`--go-home\`、\`--switch-tool wearfx\`、\`--tool-preview\`）
- 您应该自动处理此转换，而不向用户显示技术命令格式
- 对于循环命令中的括号表示法，转换为逗号分隔格式，用冒号表示延迟：
  - \`\[watchface, wearfx\] with 2s delay\` → \`watchface,wearfx:2\`
  - \`\[0,1,2,3\] with 1s delay\` → \`0,1,2,3:1\`

### 命令执行示例：
- 用户说："run watch control and go to home screen"
- 您必须执行：\`bash "/path/to/project/.claude/functions/tools/watch\_control.sh" --go-home\`

### 命令转换示例：
基本命令：
- "switch to wearfx tool" → \`bash "/path/to/project/.claude/functions/tools/watch\_control.sh" --switch-tool wearfx\`
- "take a screenshot" → \`bash "/path/to/project/.claude/functions/tools/watch\_control.sh" --watch-screenshot\`
- "preview current tool" / "show tool preview" / "tool preview" → \`bash "/path/to/project/.claude/functions/tools/watch\_control.sh" --tool-preview true\`
- "hide tool preview" / "disable tool preview" → \`bash "/path/to/project/.claude/functions/tools/watch\_control.sh" --tool-preview false\`
- "adjust tool clockwise" → \`bash "/path/to/project/.claude/functions/tools/watch\_control.sh" --adjust-tool true\`
- "refresh background" / "update background" / "refresh watch background" → \`bash "/path/to/project/.claude/functions/tools/watch\_control.sh" --refresh-background\`

复杂命令：
- "cycle through tool indices \[0,1,2\] with 3s delay" → \`bash "/path/to/project/.claude/functions/tools/watch\_control.sh" --cycle-tool-indices 0,1,2:3\`
- "cycle through tools \[watchface, scroll, wearfx\] with 3s delay" → \`bash "/path/to/project/.claude/functions/tools/watch\_control.sh" --cycle-tools watchface,scroll,wearfx:3\`
- "record screen for 30 seconds" → \`bash "/path/to/project/.claude/functions/tools/watch\_control.sh" --record-wear-screen-background 30\`

### 多步骤命令示例：
这些示例展示了具有多个操作和特定命令延迟的高级用法：

1. \*\*具有可变延迟的工具展示序列\*\*：
   \`\`\`
   bash "/path/to/project/.claude/functions/tools/watch\_control.sh" --go-home --delay 2 --tool-preview --delay 3 --switch-tool wearfx --delay 5 --cycle-tool-indices 0,1,2,3,2,1,0:2 --delay 1 --watch-screenshot
   \`\`\`

2. \*\*完整测试序列\*\*：
   \`\`\`
   bash "/path/to/project/.claude/functions/tools/watch\_control.sh" --enable-accessibility --go-home --delay 2 --tool-preview --delay 3 --cycle-tools watchface,wearfx,scroll,favourite\\ apps:3 --delay 2 --switch-tool wearfx --cycle-tool-indices 0,1,2,3,2,1,0:1 --delay 1 --watch-screenshot
   \`\`\`

3. \*\*具有可变时间的录制交互\*\*：
   \`\`\`
   bash "/path/to/project/.claude/functions/tools/watch\_control.sh" --go-home --delay 1 --record-wear-screen-background 30 --switch-tool volume --delay 2 --tool-preview --delay 3 --cycle-tool-indices 0,1,2,3,2,1,0:1
   \`\`\`

### 理解顺序和时间：
- \*\*灵活的命令顺序\*\*：命令现在按您指定的确切顺序执行
  - 您可以在循环后截图，在录制后预览工具，或任何其他序列
  - 所有操作都遵循您在命令中给出的顺序，没有预设的执行顺序

- \*\*特定命令延迟\*\*：\`delay 2s\`仅在前一个命令之后创建暂停
  - 示例：\`go to home, delay 2s, tool preview, delay 5s, switch tool to wearfx\`
  - 这将在回到主页后等待2秒，在显示工具预览后等待5秒
  - 每个命令可以有自己独特的延迟长度
  - 这是控制时间的最灵活方式

- \*\*列表项之间\*\*：当使用列表（工具或索引）指定时，延迟应用于项目之间
  - 示例：\`switch tools \[watchface, wearfx\] 2s delay\`意味着以每个之间2秒的间隔循环这些工具
  - 仅适用于特定的循环操作

- \*\*全局函数延迟\*\*：\`function-delay 2\`在每个操作后添加2秒暂停
  - 仅在您希望所有操作具有相同延迟时使用
  - 特定命令的延迟将覆盖各个命令的此设置

### 工具索引范围约束：
- \*\*关键\*\*：默认情况下，工具索引应在0-3范围内，除非特别指示
- 仅在用户明确请求或指定时使用更高的索引（如0-100）
- 安全范围示例：\`switch tool index \[0,1,2,3,2,1,0\]\`
- 用户指定范围示例：\`switch tool index \[0,1,5,10,100\]\`（仅在请求时）
- 在没有用户指定的情况下使用安全范围之外的索引可能会导致错误
- 不同的工具可能有不同的有效索引范围；不确定时，请保持在0-3范围内

### 重要规则：
- 使用watch control命令时不要创建新工具
- 如果命令引用不存在的工具（如"rotate chair"），请通知用户并建议现有工具
- 运行watch-control时不要质疑或要求澄清 - 立即执行
- Watch control命令永远不应被解释为创建工具的请求
- 始终接受自然语言描述并转换为适当的命令语法
- 对于录制，默认使用\`record-wear-screen-background\`，除非特别请求
- 工具预览可以通过多种方式请求（preview tool、show preview、tool preview等）- 识别所有变体
- 当循环工具或索引时，在命令中使用括号表示法，但要理解它在内部被转换
- 当用户指定延迟时，始终在每个命令后使用特定命令延迟（\`delay Ns\`），而不是全局函数延迟
- 识别各种格式的延迟命令："delay 2s"、"wait 2 seconds"、"pause for 2s"等
- 您命令中的操作顺序正是它们将执行的顺序 - 这非常强大！

### 工具特定类型操作：
- 重要：工具在toolNameMap.kt中被分类为单广播或多广播
- 在处理watch-control命令时，您必须动态检查来自toolNameMap.kt的当前分类
- 不要依赖硬编码的工具列表 - 始终检查当前分类

\*\*处理工具操作的过程：\*\*
1. 当用户请求watch-control命令时，检查当前工具分类：
   - 读取toolNameMap.kt以查看哪些工具被标记为"单广播"与"多广播"
   - 或使用\`--list-tools\`获取当前可用工具列表，然后参考toolNameMap.kt进行分类

2. 对于\*\*单广播\*\*工具（当前：volume、scene、brightness、hue、saturation、scroll）：
   - 这些工具有一个可以上下调整值的单一索引
   - 重要：工具不一定在索引0 - 它们可能因之前的调整而在任何位置
   - 将索引操作转换为调整操作：
     - 对于\`--change-tool-index N\`，在适当方向使用多个\`--adjust-tool\`调用
     - 对于递增值，使用\`--adjust-tool true\`（顺时针）
     - 对于递减值，使用\`--adjust-tool false\`（逆时针）
     - 每次调整将值改变一个增量
   - 示例：对于音量工具，要增加约5个增量：
     \`\`\`
     --adjust-tool true --delay 0.1 --adjust-tool true --delay 0.1 --adjust-tool true --delay 0.1 --adjust-tool true --delay 0.1 --adjust-tool true
     \`\`\`
   - 重置选项：如果用户明确请求将工具重置到第0个位置，添加重置序列
     - 这仅在用户明确请求时执行
     - 重置序列：切换到每个工具并应用多个adjust-tool false操作
     - 音量重置示例：\`--switch-tool volume --adjust-tool false --delay 0.1 \[...重复10+次...\]\`

3. 对于\*\*多广播\*\*工具（当前：wearfx、watchface、favourite apps、media actions）：
   - 这些工具有多个不同的索引（选项）可供选择
   - 正常使用索引操作：
     - \`--change-tool-index N\`正确工作以选择特定选项
     - \`--cycle-tool-indices\`正确工作以循环选项

在构建watch-control命令时，您负责此转换

### 可选工具重置：
- 仅在用户明确请求时执行工具重置序列，如以下短语：
  - "Reset all tools to 0"
  - "Zero out the tools"
  - "Reset tool positions"
- 重要：如果请求，重置操作必须在所有其他操作之前完成
- 关键：仅重置将在后续操作中使用的单广播工具
- 重置操作包括：
  1. 确定哪些单广播工具将在即将进行的操作中使用
  2. 对于这些工具中的每一个（除scroll外）：
     a. 切换到工具
     b. 应用多个adjust-tool false操作（10+次）以确保到达第0个位置
     c. 在调整之间添加小延迟
- 不要在重置操作中包括scroll工具
- 不要重置不会在后续操作中使用的工具
- 将使用音量和亮度的操作的重置序列示例：
  \`\`\`
  --switch-tool volume --adjust-tool false --delay 0.1 \重复10+次\
  --switch-tool brightness --adjust-tool false --delay 0.1 \重复10+次\
  --go-home \然后继续其他操作\
  \`\`\`
- 这是可选的，仅在特别请求时使用
```

最后更新：2025年6月2日

##### 高级自动化

此示例展示了`CLAUDE.md`如何协调复杂的工作流程，通过智能命令转换和自动化层将系统命令转换为手表交互。


* * *

**另请参阅**：[Bash脚本](/mechanics-bash-scripts.html)|[工具制作器](/mechanics-task-agent-tools.html)|[CLAUDE.md至上](/mechanics-claude-md-supremacy.html)
