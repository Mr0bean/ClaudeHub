import { defineClientConfig } from 'vuepress/client'
import { onMounted } from 'vue'

export default defineClientConfig({
  setup() {
    onMounted(() => {
      // 监听 VuePress 2.0 的暗黑模式切换
      const updateDarkMode = () => {
        // VuePress 2.0 使用 data-theme 属性
        const currentTheme = document.documentElement.getAttribute('data-theme')
        const isDark = currentTheme === 'dark'

        // 同步添加 dark 类以支持我们的自定义样式
        if (isDark) {
          document.documentElement.classList.add('dark')
          // 确保 data-theme 设置正确
          document.documentElement.setAttribute('data-theme', 'dark')
        } else {
          document.documentElement.classList.remove('dark')
          document.documentElement.setAttribute('data-theme', 'light')
        }
      }

      // 初始化
      updateDarkMode()

      // 监听 html 元素的属性变化
      const observer = new MutationObserver((mutations) => {
        mutations.forEach((mutation) => {
          if (mutation.type === 'attributes' &&
              (mutation.attributeName === 'data-theme' || mutation.attributeName === 'class')) {
            updateDarkMode()
          }
        })
      })

      // 监听 html 元素的 data-theme 和 class 变化
      observer.observe(document.documentElement, {
        attributes: true,
        attributeFilter: ['data-theme', 'class']
      })

      // 监听按钮点击事件 - VuePress 的暗黑模式切换按钮
      document.addEventListener('click', (e) => {
        const button = e.target.closest('button')
        if (button && (button.getAttribute('aria-label')?.includes('color mode') ||
                      button.getAttribute('title')?.includes('color mode'))) {
          // 切换 data-theme
          const currentTheme = document.documentElement.getAttribute('data-theme')
          const newTheme = currentTheme === 'dark' ? 'light' : 'dark'
          document.documentElement.setAttribute('data-theme', newTheme)

          // 存储到 localStorage
          localStorage.setItem('vuepress-color-scheme', newTheme)

          setTimeout(updateDarkMode, 10)
        }
      })

      // 检查 localStorage 中的主题设置
      const storedTheme = localStorage.getItem('vuepress-color-scheme')
      if (storedTheme === 'dark') {
        document.documentElement.setAttribute('data-theme', 'dark')
        document.documentElement.classList.add('dark')
      }
    })
  }
})