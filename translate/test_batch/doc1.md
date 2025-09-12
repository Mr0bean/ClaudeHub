# Getting Started with VuePress

VuePress is a Vue-powered static site generator. It takes Markdown documents and renders them into a beautiful website.

## Installation

To install VuePress, use npm:

```bash
npm install -D vuepress
```

## Configuration

Create a `.vuepress/config.js` file:

```javascript
module.exports = {
  title: 'My Docs',
  description: 'Documentation site',
  themeConfig: {
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Guide', link: '/guide/' }
    ]
  }
}
```

For more information, visit: https://vuepress.vuejs.org/