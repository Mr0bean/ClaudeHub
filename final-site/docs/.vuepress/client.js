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

        // 只同步添加 dark 类，不修改 data-theme
        if (isDark) {
          document.documentElement.classList.add('dark')
        } else {
          document.documentElement.classList.remove('dark')
        }
      }

      // 初始化
      updateDarkMode()

      // 添加标志防止无限循环
      let isUpdating = false

      // 监听 html 元素的属性变化
      const observer = new MutationObserver((mutations) => {
        if (isUpdating) return

        mutations.forEach((mutation) => {
          if (mutation.type === 'attributes' &&
              mutation.attributeName === 'data-theme') {
            isUpdating = true
            updateDarkMode()
            setTimeout(() => { isUpdating = false }, 100)
          }
        })
      })

      // 只监听 data-theme 变化，不监听 class
      observer.observe(document.documentElement, {
        attributes: true,
        attributeFilter: ['data-theme']
      })

      // 移除点击事件监听器，让VuePress自己处理

      // 检查 localStorage 中的主题设置
      const storedTheme = localStorage.getItem('vuepress-color-scheme')
      if (storedTheme === 'dark') {
        document.documentElement.setAttribute('data-theme', 'dark')
        document.documentElement.classList.add('dark')
      }
    })
  }
})