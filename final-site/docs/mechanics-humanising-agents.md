---
title: "Humanising Agents | ClaudeLog"
---

# Humanising Agents | ClaudeLog

`Custom agents` are assigned distinct personalities through their specialised roles, system prompts, and tool configurations. However, the default interaction model can feel overly formal. We can create more engaging collaborations by humanizing our agents with `nicknames` and expressive `text-faces`.

* * *

* * *

## Beyond Formal Invocation[​](#beyond-formal-invocation "Direct link to Beyond Formal Invocation")

Traditional agent invocation feels mechanical:

```bash
ask performance optimiser assistant to review the changes

```

With [nicknames](/mechanics/agent-engineering/#agent-nicknaming-for-efficiency), the interaction becomes more natural:

```bash
ask P1 to review the changes

```

But we can go even further by adding personality through `text-faces`, creating agents that feel more like collaborators than tools.

* * *

* * *

## Text-Face Personalities[​](#text-face-personalities "Direct link to Text-Face Personalities")

While playing around with different ways to personalize agents, I had the idea of exploring `text-faces`. When it first loaded I knew it was a hit! Each face represents the agent's personality, role, or typical mood while complementing the clean terminal aesthetic that developers love.

### Text-Face Examples by Role[​](#text-face-examples-by-role "Direct link to Text-Face Examples by Role")

Each category shows different personality approaches for common development roles:

#### Debugging & Testing[​](#debugging--testing "Direct link to Debugging & Testing")

`( ͡° ͜ʖ ͡°) Mischievous Debugger` - Playful problem solver who enjoys hunting down tricky bugs `(つ◉益◉)つ Bug Hunter` - Aggressive pursuer of software defects `(¬_¬) Test Engineer` - Skeptical validator who questions everything

#### Code Review & Quality[​](#code-review--quality "Direct link to Code Review & Quality")

`¯\_(ツ)_/¯ Casual Code Reviewer` - Laid-back reviewer who keeps things simple and practical `(ㆆ_ㆆ) Quality Auditor` - Sharp-eyed observer who notices every detail `ಠ_ಠ Security Analyst` - Disapproving guardian of system security

#### Performance & Optimization[​](#performance--optimization "Direct link to Performance & Optimization")

`'(ᗒᗣᗕ)՞ Performance Optimizer` - High-energy assistant focused on speed and efficiency `★⌒ヽ( ͡° ε ͡°) Performance Tuner` - Stellar optimizer of system performance `˙ ͜ʟ˙ Memory Manager` - Focused fighter against memory leaks

#### Development & Refactoring[​](#development--refactoring "Direct link to Development & Refactoring")

`(• ε •) Gentle Refactorer` - Soft-spoken helper that improves code with care `ʕ•ᴥ•ʔ UI Developer` - Friendly interface specialist with a warm approach `(ง'̀-'́)ง Dead Code Remover` - Fighting eliminator of unused code

#### Documentation & Communication[​](#documentation--communication "Direct link to Documentation & Communication")

`(͡• ͜໒ ͡• ) Documentation Writer` - Loving creator of beautiful documentation `♥‿♥ Requirements Helper` - Sweet assistant for unclear specifications `┌༼◉ل͟◉༽┐ Grammar Checker` - Intense scrutinizer of language precision

#### Operations & Management[​](#operations--management "Direct link to Operations & Management")

`┗(▀̿Ĺ̯▀̿ ̿)┓ Git Manager` - Cool operator dancing between branches `( ͡ _ ͡°)ﾉ⚲ Deployment Guard` - Waving protector of production releases `⚆_⚆ Database Expert` - Wide-eyed master of data management

#### Specialized & Creative[​](#specialized--creative "Direct link to Specialized & Creative")

`【≽ܫ≼】 Research King` - Magnificent gatherer of knowledge and insights `⋋| ◉ ͟ʖ ◉ |⋌ Metrics Spy` - Watchful observer of performance data `(┛ಠДಠ)┛彡┻━┻ Frustrated Developer` - Overwhelmed coder who's had enough

* * *

* * *

## Implementation Strategy[​](#implementation-strategy "Direct link to Implementation Strategy")

When designing your own humanized assistants, use the categories above as a starting point:

1.  **Match personality to function** - A `┗(▀̿Ĺ̯▀̿ ̿)┓ Git Manager` needs different energy than a `(• ε •) Gentle Refactorer`
2.  **Choose appropriate intensity** - Compare the laid-back `¯\_(ツ)_/¯ Casual Code Reviewer` with the intense `┌༼◉ل͟◉༽┐ Grammar Checker`
3.  **Consider your team context** - The `(┛ಠДಠ)┛彡┻━┻ Frustrated Developer` might work in casual teams but not formal environments
4.  **Match complexity to specialization** - Complex faces like `⋌༼ •̀ ⌂ •́ ༽⋋ Algorithm Expert` should match equally specialized roles
5.  **Test display compatibility** - Ensure your chosen `text-faces` render correctly across different terminals and systems

* * *

## Resources[​](#resources "Direct link to Resources")

For additional `text-face` inspiration, explore: [Text Faces Collection](https://texteditor.com/text-faces/)

Color Personalization

You can match the color of your custom agent output to make it even more personalized! Each agent can have its own distinctive color scheme that complements its `text-face` personality.

##### Fun & Social Coding

Using `text-faces` with `custom agents` transforms coding from a solitary technical task into something surprisingly fun and social! Each assistant feels like a distinct personality you're collaborating with, making development sessions more engaging.

<img src="/img/discovery/021_happy_orange.png" alt="Custom image" style="max-width: 165px; height: auto;" />

* * *

**See Also**: [Custom Agents](/mechanics/custom-agents/) | [Agent Engineering](/mechanics/agent-engineering/) | [Task Agent Tools](/mechanics/task-agent-tools/)

**Author**:[<img src="/img/claudes-greatest-soldier.png" alt="InventorBlack profile" style="width: 25px; height: 25px; display: inline-block; vertical-align: middle; margin: 0 3px; border-radius: 50%;" />InventorBlack](https://www.linkedin.com/in/wilfredkasekende/)|CTO at [Command Stick](https://commandstick.com)|Mod at [r/ClaudeAi](https://reddit.com/r/ClaudeAI)

-   [Beyond Formal Invocation](#beyond-formal-invocation)
-   [Text-Face Personalities](#text-face-personalities)
    -   [Text-Face Examples by Role](#text-face-examples-by-role)
-   [Implementation Strategy](#implementation-strategy)
-   [Resources](#resources)