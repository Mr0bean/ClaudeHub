---
title: "Auto-Accept Permissions | ClaudeLog"
---

# Auto-Accept Permissions | ClaudeLog

Auto-accept permissions is a mechanic in Claude Code that eliminates confirmation prompts, enabling Claude to execute actions immediately without interrupting the flow for approval.

When activated, the UI displays "auto-accept edit on" and Claude will not pause to request permission before making file edits, running commands, or other operations. The permission request interface is typically presented when Claude determines a task could be potentially dangerous and requires explicit approval.

You can adjust which tools are allowed through auto-accept mode by updating your `allowedTools` configuration (see the [Claude Code Configuration Guide](/configuration/) for details).

You activate it by pressing `shift+tab` repeatedly to cycle through modes: normal-mode, auto-accept edit on, and plan mode on as indicated within the Claude Code UI.

This mechanic represents the opposite end of the safety spectrum from [Plan Mode](/mechanics/plan-mode/), prioritizing speed and uninterrupted execution over cautious verification. The seamless keyboard toggle makes it easy to switch modes as your workflow demands.

* * *

* * *

### Prior to Auto-Accept[​](#prior-to-auto-accept "Direct link to Prior to Auto-Accept")

I found myself constantly hitting `Enter` to approve Claude's actions when permission prompts appeared for file modifications, command execution, or system interactions.

While these prompts serve an important safety function, they create friction when you're confident in Claude's approach and want uninterrupted execution.

Folks on [r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/) have expressed similar frustration with the constant permission requests, particularly during repetitive tasks like refactoring or when trying to achieve long agentic sprints for 10-40 minutes.

### With Auto-Accept[​](#with-auto-accept "Direct link to With Auto-Accept")

Auto-accept transforms Claude Code into a seamless execution environment (assuming your `allowedTools` are setup correctly). Claude proceeds immediately with file edits, command execution, and other operations without breaking flow.

When I have a clear direction, auto-accept allows me to leave Claude working autonomously while I focus on other tasks. I can get in the zone on different work, only checking on Claude when he contacts me via the [bell notification](/faqs/claude-code-terminal-bell-notifications/) system.

I observe this is particularly valuable during:

-   Researching codebases and documentation
-   Large refactoring operations across multiple files
-   Following long plans that have been thoroughly checked

The result is dramatically faster iteration cycles and maintained focus on the problem rather than constant approval decisions.

* * *

* * *

### Safety Considerations[​](#safety-considerations "Direct link to Safety Considerations")

Use auto-accept cautiously. Without permission prompts, Claude would immediately execute all proposed changes. File modifications proceed without confirmation, bash commands run immediately, and potentially destructive operations occur without pause. Large scale modifications across multiple files happen in sequence, creating compound risk if something goes wrong.

### Permission Mode Cycling[​](#permission-mode-cycling "Direct link to Permission Mode Cycling")

Pressing `shift+tab` cycles through Claude Code's permission modes:

-   **normal-mode** - Standard permission prompts for all operations
-   **auto-accept edit on** - Auto-accept all permissions for any operations
-   **plan mode on** - Read-only research and planning mode

The UI clearly indicates which mode is active, displaying the exact terminology as you cycle through each state.

##### Execution Flow

Once auto-accept is enabled, Claude maintains continuous execution momentum. I observe this creates a distinctly different workflow rhythm compared to the deliberate verification pace of normal mode.

<img src="/img/discovery/000_orange.png" alt="Custom image" style="max-width: 165px; height: auto;" />

* * *

**See Also**: [Plan Mode](/mechanics/plan-mode/)|[Allowed Tools Configuration](/configuration/#allowed-tools)|[Dangerous Skip Permissions](/mechanics/dangerous-skip-permissions/)

**Author**:[<img src="/img/claudes-greatest-soldier.png" alt="InventorBlack profile" style="width: 25px; height: 25px; display: inline-block; vertical-align: middle; margin: 0 3px; border-radius: 50%;" />InventorBlack](https://www.linkedin.com/in/wilfredkasekende/)|CTO at [Command Stick](https://commandstick.com)|Mod at [r/ClaudeAi](https://reddit.com/r/ClaudeAI)

-   [Prior to Auto-Accept](#prior-to-auto-accept)
-   [With Auto-Accept](#with-auto-accept)
-   [Safety Considerations](#safety-considerations)
-   [Permission Mode Cycling](#permission-mode-cycling)