---
title: "Todo Lists As Instruction Mirrors | ClaudeLog"
---

# Todo Lists As Instruction Mirrors | ClaudeLog

The todo list tool is my second favorite Claude Code tool, after the task/agent tool. The todo list tool does more than just track progress—it reveals how Claude interprets your instructions.

I often use Claude's todos to benchmark my instructions, especially for step-by-step processes that I expect to be mirror-reflected. When his todos reflect my intentions, I know my instructions are understood. When his todos deviate, it flags possible areas for improvement in my communication.

* * *

* * *

**Todo List Discrepancies**

-   **Wrong Order**: Instructions specify do step A then B, but Claude's todos list B then A
-   **Missing Todos**: Instructions mention running tests, but Claude's todo list omits this step entirely
-   **Extra Todos**: Claude adds "backup existing files" when the instructions never mentioned this
-   **Wrong Granularity**: Instructions say "update documentation" but Claude creates separate todos for each individual file
-   **Misunderstood Steps**: Instructions say "review changes" but Claude lists "commit changes"

**Live Steering**

Claude's todo lists communicate the effect of live steering Claude's objectives. When Claude reviews your prompts mid-task and uses them to update his plan, you can steer future todos.

Consider a basic example of changing an element's color. Proper utilization of todo lists can more clearly steer future todos because you can see exactly what he plans to do.

**Before Steering:**

-    Fix nav menu alignment
-    Update footer text
-    Add new contact form validation
-    Change button background color to `#3b82f6`
-    Update documentation

**Mid-Task Steering:**

```
Actually, let's use `#10b981` for the button color instead, and make sure you also update the hover state to `#059669`.
```

**After Steering:**

-    Fix nav menu alignment
-    Update footer text
-    Add new contact form validation
-    Change button background color to `#10b981`
-    Update documentation

##### Experiment

Try encouraging Claude to be more granular in his todos. Instead of "Style the navigation bar", have Claude reveal the specific adjustments: "Change height from 60px to 80px", "Reduce padding-top from 16px to 12px", "Adjust background from #ffffff to rgba(255,255,255,0.9)". This transparency exposes Claude's design decisions before he makes them, allowing you to approve or redirect his aesthetic choices.

<img src="/img/discovery/036_cl_orange.png" alt="Custom image" style="max-width: 165px; height: auto;" />

* * *

**See Also**: [You Are The Main Thread](/mechanics-you-are-the-main-thread.html)|[Tight Feedback Loops](/mechanics-tight-feedback-loops.html)|[CLAUDE.md Supremacy](/mechanics-claude-md-supremacy.html)

**Author**: [<img src="/img/profiles/inventorblack.png" alt="InventorBlack" style="width: 25px; height: 25px; border-radius: 50%;" />InventorBlack](/contact.html)|CTO at [Command Stick](https://commandstick.com)|Mod at [r/ClaudeAi](https://reddit.com/r/ClaudeAi)