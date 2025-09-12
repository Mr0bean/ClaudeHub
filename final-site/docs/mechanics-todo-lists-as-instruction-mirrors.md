---
title: "Todo Lists as Instruction Mirrors | ClaudeLog"
---

# Todo Lists as Instruction Mirrors | ClaudeLog

The Todo list tool is my second favourite Claude Code tool, second only to the Task/Agent tool. The Todo list tool serves a purpose beyond just tracking progress, it reveals how Claude interprets your instructions.

I often benchmark my instructions against Claude's todos, particularly for step by step processes I am aspiring for a mirror like reflection. When his todos mirror my intentions, I know my instructions are grokked. When his todos diverge, it flags an area for potential improvement in my communication.

* * *

* * *

**Todo List Divergence**

-   **Out of Order**: Instructions specify step A then B, but Claude's todos list B then A
-   **Missing Todo Item**: Instructions mention running tests, but Claude's todo list omits this step entirely
-   **Extra Todo Item**: Claude adds "backup existing files" when instructions never mentioned this
-   **Wrong Granularity**: Instructions say "update documentation" but Claude creates separate todos for each individual file
-   **Misinterpreted Step**: Instructions say "review changes" but Claude lists "commit changes" instead

**Real-Time Steering**

Claude's todo list communicates the effects of real-time steering of Claude's goals. You can steer future todo items as Claude reviews your prompts mid-task and uses them to update his planning.

Consider a basic example of changing an element's colour. Properly utilising the todo list allows for clearer steering of future todos as you can see exactly what he plans to do.

**Before Steering:**

-    Fix the navigation menu alignment
-    Update the footer text
-    Add new contact form validation
-    Change the button background color to `blue`
-    Update documentation

**Mid-task Steering:**

```bash
Actually make it green instead

```

**After Steering:**

-    Fix the navigation menu alignment
-    Update the footer text
-    Add new contact form validation
-    Change the button background color to `green`
-    Update documentation

##### Experiment

Try encouraging Claude to be granular with his todos. Instead of "style the navbar," get Claude to reveal specific adjustments: "change height from 60px to 80px," "reduce padding-top from 16px to 12px," "adjust background from #ffffff to rgba(255,255,255,0.95)." This transparency exposes Claude's design decisions before he makes them, letting you approve or redirect his aesthetic choices.

<img src="/img/discovery/024_excite_orange.png" alt="Custom image" style="max-width: 165px; height: auto;" />

* * *

**See Also**: [You Are the Main Thread](/mechanics/you-are-the-main-thread/)|[Tight Feedback Loops](/mechanics/tight-feedback-loops/)|[CLAUDE.md Supremacy](/mechanics/claude-md-supremacy/)

**Author**:[<img src="/img/claudes-greatest-soldier.png" alt="InventorBlack profile" style="width: 25px; height: 25px; display: inline-block; vertical-align: middle; margin: 0 3px; border-radius: 50%;" />InventorBlack](https://www.linkedin.com/in/wilfredkasekende/)|CTO at [Command Stick](https://commandstick.com)|Mod at [r/ClaudeAi](https://reddit.com/r/ClaudeAI)