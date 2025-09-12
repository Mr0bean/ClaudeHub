---
title: "Sanity Check | ClaudeLog"
---

# Sanity Check | ClaudeLog

> Original: Prior to AI agents we ran sanity checks like:

```bash
console.log("sanity")

```

```bash
print("sanity")

```

```bash
Log.d("test", "sanity")

```

* * *

* * *

When collaborating with AI agents we have to perform a different kind of sanity check.

Add your name at the top of your `CLAUDE.md`:

**CLAUDE.md**

```bash
# My name is {NAME}

This file provides guidance to Claude Code when working with this repository.

## Project Overview

This is a React application built with TypeScript and Vite.

...

```

Then ask Claude:

```bash
What is my name?

```

* * *

This works as a quick sanity check. If Claude knows your name, all is good. If he does not, then something is wrong.

There are various situations where things could go wrong:

-   Forgetting to set a `CLAUDE.md`
-   Putting the `CLAUDE.md` in the wrong folder
-   Accidentally deleting part of the `CLAUDE.md`
-   Mispelling `CLAUSE.md`
-   Running out of context window (sometimes unavoidable)

The simplest way to 'sanity check' your configuration is to place your name at the top of your `CLAUDE.md` and ask Claude your name.

##### Experiment

Random thought whilst writing this: it could be interesting to have 'sanity check points' dotted across your `CLAUDE.md` so you could check their integrity as the context window fills up.

<img src="/img/discovery/016_scary_orange.png" alt="Custom image" style="max-width: 165px; height: auto;" />

* * *

**See Also**: [CLAUDE.md Supremacy](/mechanics/claude-md-supremacy/)|[Configuration](/configuration/)|[Context Window Constraints](/mechanics/context-window-constraints-as-training/)

**Author**:[<img src="/img/claudes-greatest-soldier.png" alt="InventorBlack profile" style="width: 25px; height: 25px; display: inline-block; vertical-align: middle; margin: 0 3px; border-radius: 50%;" />InventorBlack](https://www.linkedin.com/in/wilfredkasekende/)|CTO at [Command Stick](https://commandstick.com)|Mod at [r/ClaudeAi](https://reddit.com/r/ClaudeAI)