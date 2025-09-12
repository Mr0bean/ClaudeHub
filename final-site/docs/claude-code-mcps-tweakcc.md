---
title: "TweakCC | ClaudeLog"
---

# TweakCC | ClaudeLog

**Lightweight CLI tool for personalizing your Claude Code interface with custom themes and visual enhancements**

**Author**: [@Piebald-AI](https://github.com/Piebald-AI)  |  [GitHub Repo](https://github.com/Piebald-AI/tweakcc)  |  69 Stars|4 Forks|MIT License|Updated Aug 24, 2025

* * *

### Overview[​](#overview "Direct link to Overview")

TweakCC transforms your Claude Code experience through comprehensive interface personalization. This lightweight CLI tool allows you to customize colors, animations, messaging, and styling to create a unique development environment that reflects your personal preferences.

Built with React and Ink, TweakCC provides an interactive terminal interface for creating custom themes, selecting from over 70 animations, and personalizing every aspect of your Claude Code CLI experience.

* * *

* * *

<!-- Screenshot temporarily removed due to missing asset -->

* * *

* * *

### Features[​](#features "Direct link to Features")

-   **Custom Theme Creation** - Interactive HSL/RGB color picker for complete interface customization
-   **70+ Thinking Animations** - Choose from a vast collection of spinning and processing animations
-   **Personalized Thinking Verbs** - Custom messages displayed during Claude's processing states
-   **Markdown Element Styling** - Customize the appearance of markdown elements in responses (Work in Progress)
-   **User Message Styling** - Personalize how your messages appear in chat history
-   **Banner Text Customization** - Change banner text with figlet font styling
-   **Cross-Platform Support** - Compatible with Windows, macOS, and Linux
-   **Persistent Configuration** - Settings saved in `~/.tweakcc/config.js` and persist across updates

* * *

* * *

### Installation[​](#installation "Direct link to Installation")

**Quick Start (Recommended)**

```bash
npx tweakcc

```

**Alternative Package Managers**

```bash
# Using pnpm

pnpm dlx tweakcc

# Global installation (if preferred)

npm install -g tweakcc

tweakcc

```

* * *

* * *

### Usage[​](#usage "Direct link to Usage")

**Interactive Theme Creation**

```bash
# Launch the customization interface

npx tweakcc

```

Follow the interactive prompts to:

-   **Select custom colors** with visual picker
-   **Choose from 70+ animations** for processing states
-   **Set personalized thinking verbs** for custom messaging
-   **Configure markdown styling** for response formatting (WIP feature)

**Configuration Management**

TweakCC works by patching Claude Code's `cli.js` file and saves your preferences to `~/.tweakcc/config.js`. Your customizations include:

-   **Color Themes** - HSL/RGB values for interface elements
-   **Animation Selection** - Preferred thinking/processing animations
-   **Custom Messages** - Personalized thinking verbs and banner text
-   **Style Overrides** - Markdown and user message styling preferences

**Environment Integration**

-   Your customizations automatically apply when running Claude Code
-   Configurations persist across Claude Code updates
-   Re-run tweakcc to modify or update your theme
-   Compatible with Claude Code version 1.0.88

For detailed configuration options and advanced theming, see the [official documentation](https://github.com/Piebald-AI/tweakcc).

* * *

### Integration with Claude Code[​](#integration-with-claude-code "Direct link to Integration with Claude Code")

TweakCC seamlessly integrates with your Claude Code installation, providing a personalized interface without affecting core functionality.

**Enhanced Development Experience**

-   Visual customization that matches your development environment
-   Personalized animations and messages for a unique CLI experience
-   Persistent theming that survives Claude Code updates
-   Interactive configuration that makes customization accessible to all users

##### CLI Personalization

Developers spend significant time in CLI environments, and TweakCC addresses the desire for personalized, visually appealing interfaces. The tool makes Claude Code feel uniquely yours while maintaining all its powerful functionality.

<img src="/img/discovery/036_cl.png" alt="Custom image" style="max-width: 165px; height: auto;" />

* * *

*TweakCC is developed by Piebald LLC as a community project. For technical support and updates, please refer to the official GitHub repository.*

-   [Overview](#overview)
-   [Features](#features)
-   [Installation](#installation)
-   [Usage](#usage)
-   [Integration with Claude Code](#integration-with-claude-code)