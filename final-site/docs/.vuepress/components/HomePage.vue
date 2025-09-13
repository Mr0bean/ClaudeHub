<template>
  <div class="home-page" :style="pageStyle">
    <!-- Hero 区域 -->
    <section class="hero-section">
      <div class="hero-background"></div>
      <div class="hero-content">
        <div class="hero-badge">
          <span class="badge-icon">🚀</span>
          <span class="badge-text">Claude Code 中文社区</span>
        </div>

        <h1 class="hero-title">
          <span class="gradient-text">ClaudeLog</span>
          <span class="subtitle">中文文档</span>
        </h1>

        <p class="hero-description">
          为中文 Claude 开发者社区提供完整的文档支持
          <br />
          涵盖 <strong>68+</strong> 页面的专业技术文档，保持原站点的完整结构和功能
        </p>

        <div class="hero-actions">
          <RouterLink to="/guide.html" class="btn btn-primary">
            <span class="btn-icon">📚</span>
            开始阅读
          </RouterLink>
          <RouterLink to="/install-claude-code.html" class="btn btn-secondary">
            <span class="btn-icon">⚡</span>
            快速安装
          </RouterLink>
        </div>

        <div class="hero-stats">
          <div class="stat-item">
            <div class="stat-number">68+</div>
            <div class="stat-label">文档页面</div>
          </div>
          <div class="stat-item">
            <div class="stat-number">95%</div>
            <div class="stat-label">翻译进度</div>
          </div>
          <div class="stat-item">
            <div class="stat-number">20+</div>
            <div class="stat-label">MCP 扩展</div>
          </div>
        </div>
      </div>
    </section>

    <!-- 特性卡片 -->
    <section class="features-section">
      <div class="container">
        <h2 class="section-title">
          <span class="gradient-text">核心特性</span>
        </h2>

        <div class="features-grid">
          <div class="feature-card">
            <div class="feature-icon">
              <span>🎯</span>
            </div>
            <h3>完整文档</h3>
            <p>涵盖 Claude Code 的所有功能、API、配置和最佳实践</p>
          </div>

          <div class="feature-card">
            <div class="feature-icon">
              <span>🔧</span>
            </div>
            <h3>MCP 扩展</h3>
            <p>20+ 个模型上下文协议扩展，增强 Claude 的能力</p>
          </div>

          <div class="feature-card">
            <div class="feature-icon">
              <span>🚀</span>
            </div>
            <h3>性能优化</h3>
            <p>深入的性能优化技巧和上下文管理策略</p>
          </div>

          <div class="feature-card">
            <div class="feature-icon">
              <span>🤖</span>
            </div>
            <h3>智能代理</h3>
            <p>构建和管理智能代理的完整指南</p>
          </div>

          <div class="feature-card">
            <div class="feature-icon">
              <span>💡</span>
            </div>
            <h3>最佳实践</h3>
            <p>经过验证的开发模式和实战经验</p>
          </div>

          <div class="feature-card">
            <div class="feature-icon">
              <span>🌐</span>
            </div>
            <h3>中文优化</h3>
            <p>专为中文用户优化的文档和示例</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 快速链接 -->
    <section class="quick-links-section">
      <div class="container">
        <h2 class="section-title">
          <span class="gradient-text">快速导航</span>
        </h2>

        <div class="links-grid">
          <RouterLink to="/guide.html" class="link-card">
            <div class="link-icon">📖</div>
            <div class="link-content">
              <h4>入门指南</h4>
              <p>从零开始学习 Claude Code</p>
            </div>
            <div class="link-arrow">→</div>
          </RouterLink>

          <RouterLink to="/mechanics-you-are-the-main-thread.html" class="link-card">
            <div class="link-icon">⚙️</div>
            <div class="link-content">
              <h4>核心机制</h4>
              <p>深入理解运行原理</p>
            </div>
            <div class="link-arrow">→</div>
          </RouterLink>

          <RouterLink to="/claude-code-mcps.html" class="link-card">
            <div class="link-icon">🔌</div>
            <div class="link-content">
              <h4>MCPs 扩展</h4>
              <p>探索强大的扩展生态</p>
            </div>
            <div class="link-arrow">→</div>
          </RouterLink>

          <RouterLink to="/faq.html" class="link-card">
            <div class="link-icon">❓</div>
            <div class="link-content">
              <h4>常见问题</h4>
              <p>快速解决常见问题</p>
            </div>
            <div class="link-arrow">→</div>
          </RouterLink>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
  data() {
    return {
      isDark: false
    }
  },
  computed: {
    pageStyle() {
      return this.isDark ? {
        background: 'linear-gradient(180deg, #0f172a 0%, #1e293b 100%)',
        minHeight: '100vh'
      } : {
        background: 'transparent',
        minHeight: '100vh'
      }
    }
  },
  mounted() {
    // 初始化检测暗黑模式
    if (typeof window !== 'undefined') {
      this.isDark = document.documentElement.classList.contains('dark');

      // 监听主题变化
      const observer = new MutationObserver(() => {
        this.isDark = document.documentElement.classList.contains('dark');
      });
      observer.observe(document.documentElement, {
        attributes: true,
        attributeFilter: ['class']
      });
    }
  }
}
</script>

<style scoped lang="scss">
.home-page {
  margin-top: -3.6rem; // 抵消导航栏高度
}

// Hero 区域
.hero-section {
  position: relative;
  min-height: 600px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 120px 20px 80px;
  overflow: hidden;
}

.hero-background {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, #e0e7ff 0%, #c7d2fe 25%, #a5b4fc 50%, #8b5cf6 75%, #7c3aed 100%);
  opacity: 0.15;

  &::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: radial-gradient(circle at 20% 50%, rgba(0, 201, 255, 0.3) 0%, transparent 50%),
                radial-gradient(circle at 80% 50%, rgba(126, 85, 255, 0.3) 0%, transparent 50%),
                radial-gradient(circle at 50% 100%, rgba(90, 45, 209, 0.2) 0%, transparent 50%);
    mix-blend-mode: multiply;
    animation: heroGradient 15s ease-in-out infinite;
  }

  &::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-image:
      radial-gradient(circle at 1px 1px, rgba(126, 85, 255, 0.15) 1px, transparent 1px);
    background-size: 40px 40px;
    animation: dotMove 60s linear infinite;
  }
}

@keyframes heroGradient {
  0%, 100% { opacity: 0.3; transform: scale(1) rotate(0deg); }
  50% { opacity: 0.5; transform: scale(1.1) rotate(5deg); }
}

@keyframes dotMove {
  0% { transform: translate(0, 0); }
  100% { transform: translate(40px, 40px); }
}

.hero-content {
  position: relative;
  text-align: center;
  max-width: 900px;
  z-index: 1;
}

.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  background: linear-gradient(135deg, rgba(0, 201, 255, 0.1), rgba(90, 45, 209, 0.1));
  border: 1px solid rgba(90, 45, 209, 0.2);
  border-radius: 24px;
  margin-bottom: 24px;

  .badge-icon {
    font-size: 18px;
  }

  .badge-text {
    font-size: 14px;
    font-weight: 600;
    color: #5A2DD1;
  }
}

.hero-title {
  font-size: 4rem;
  font-weight: 800;
  margin-bottom: 16px;
  line-height: 1.2;

  @media (max-width: 768px) {
    font-size: 3rem;
  }

  .subtitle {
    display: block;
    font-size: 2rem;
    font-weight: 600;
    color: #64748B;
    margin-top: 8px;
  }
}

.gradient-text {
  background: linear-gradient(135deg, #00C9FF 0%, #5A2DD1 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-description {
  font-size: 1.25rem;
  color: #475569;
  margin-bottom: 32px;
  line-height: 1.8;

  strong {
    color: #5A2DD1;
    font-weight: 700;
  }
}

.hero-actions {
  display: flex;
  gap: 16px;
  justify-content: center;
  margin-bottom: 48px;

  @media (max-width: 640px) {
    flex-direction: column;
    align-items: center;
  }
}

.btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 14px 28px;
  border-radius: 12px;
  font-weight: 600;
  font-size: 16px;
  text-decoration: none;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  cursor: pointer;

  .btn-icon {
    font-size: 20px;
  }

  &.btn-primary {
    background: linear-gradient(135deg, #00C9FF 0%, #5A2DD1 100%);
    color: white;
    box-shadow: 0 4px 20px rgba(90, 45, 209, 0.3);

    &:hover {
      transform: translateY(-2px);
      box-shadow: 0 8px 30px rgba(90, 45, 209, 0.4);
    }
  }

  &.btn-secondary {
    background: white;
    color: #5A2DD1;
    border: 2px solid #E2E8F0;

    &:hover {
      background: #F8FAFC;
      border-color: #5A2DD1;
      transform: translateY(-2px);
    }
  }
}

.hero-stats {
  display: flex;
  gap: 48px;
  justify-content: center;

  @media (max-width: 640px) {
    gap: 32px;
  }

  .stat-item {
    text-align: center;

    .stat-number {
      font-size: 2.5rem;
      font-weight: 800;
      background: linear-gradient(135deg, #00C9FF 0%, #5A2DD1 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }

    .stat-label {
      font-size: 14px;
      color: #64748B;
      font-weight: 500;
    }
  }
}

// 特性卡片区域
.features-section {
  padding: 80px 20px;
  background: linear-gradient(180deg, rgba(248, 250, 252, 0.5) 0%, rgba(241, 245, 249, 0.3) 100%);
  position: relative;

  &::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: radial-gradient(circle at 50% 50%, rgba(126, 85, 255, 0.02) 0%, transparent 70%);
    pointer-events: none;
  }
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  position: relative;
  z-index: 1;
}

.section-title {
  text-align: center;
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 48px;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 24px;
}

.feature-card {
  position: relative;
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.9), rgba(248, 250, 252, 0.9));
  padding: 32px;
  border-radius: 16px;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  border: 1px solid transparent;
  background-clip: padding-box;
  overflow: hidden;

  &::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(135deg, rgba(126, 85, 255, 0.1), rgba(0, 201, 255, 0.1));
    opacity: 0;
    transition: opacity 0.3s;
    z-index: -1;
  }

  &::after {
    content: '';
    position: absolute;
    inset: 0;
    border-radius: 16px;
    padding: 1px;
    background: linear-gradient(135deg, #7E55FF, #00C9FF);
    -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
    -webkit-mask-composite: xor;
    mask-composite: exclude;
    opacity: 0;
    transition: opacity 0.3s;
  }

  &:hover {
    transform: translateY(-6px);
    box-shadow: 0 20px 40px -10px rgba(126, 85, 255, 0.3);

    &::before {
      opacity: 1;
    }

    &::after {
      opacity: 0.5;
    }
  }

  .feature-icon {
    width: 64px;
    height: 64px;
    background: linear-gradient(135deg, #00C9FF 0%, #5A2DD1 100%);
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 20px;
    box-shadow: 0 8px 16px -4px rgba(90, 45, 209, 0.3);
    position: relative;
    overflow: hidden;

    &::before {
      content: '';
      position: absolute;
      top: 50%;
      left: 50%;
      width: 100%;
      height: 100%;
      background: radial-gradient(circle, rgba(255, 255, 255, 0.3) 0%, transparent 70%);
      transform: translate(-50%, -50%);
    }

    span {
      font-size: 32px;
      position: relative;
      z-index: 1;
      filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.2));
    }
  }

  h3 {
    font-size: 1.25rem;
    font-weight: 700;
    color: #0F172A;
    margin-bottom: 12px;
  }

  p {
    color: #64748B;
    line-height: 1.6;
  }
}

// 快速链接区域
.quick-links-section {
  padding: 80px 20px;
}

.links-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 20px;
}

.link-card {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 24px;
  background: white;
  border: 2px solid #E2E8F0;
  border-radius: 12px;
  text-decoration: none;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);

  &:hover {
    border-color: #5A2DD1;
    transform: translateX(4px);
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);

    .link-arrow {
      transform: translateX(4px);
    }
  }

  .link-icon {
    font-size: 32px;
    flex-shrink: 0;
  }

  .link-content {
    flex: 1;

    h4 {
      font-size: 1.125rem;
      font-weight: 600;
      color: #0F172A;
      margin-bottom: 4px;
    }

    p {
      font-size: 14px;
      color: #64748B;
      margin: 0;
    }
  }

  .link-arrow {
    font-size: 20px;
    color: #5A2DD1;
    transition: transform 0.3s;
  }
}

// 暗色模式支持 - 支持 VuePress 的 data-theme 属性
:global(html[data-theme="dark"]),
:global(html.dark) {
  .home-page {
    background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%) !important;
    color: #cbd5e1 !important;
  }

  .hero-section {
    background: transparent !important;

    .hero-background {
      background: linear-gradient(135deg,
        rgba(15, 23, 42, 0.8) 0%,
        rgba(30, 41, 59, 0.6) 25%,
        rgba(51, 65, 85, 0.5) 50%,
        rgba(71, 85, 105, 0.4) 75%,
        rgba(100, 116, 139, 0.3) 100%);
      opacity: 0.8;

      &::before {
        background: radial-gradient(circle at 20% 50%, rgba(0, 201, 255, 0.2) 0%, transparent 50%),
                    radial-gradient(circle at 80% 50%, rgba(126, 85, 255, 0.2) 0%, transparent 50%),
                    radial-gradient(circle at 50% 100%, rgba(90, 45, 209, 0.15) 0%, transparent 50%);
      }

      &::after {
        background-image:
          radial-gradient(circle at 1px 1px, rgba(165, 180, 252, 0.1) 1px, transparent 1px);
      }
    }
  }

  .hero-badge {
    background: linear-gradient(135deg, rgba(0, 201, 255, 0.15), rgba(126, 85, 255, 0.15));
    border-color: rgba(165, 180, 252, 0.3);

    .badge-text {
      color: #a5b4fc;
    }
  }

  .hero-title {
    .gradient-text {
      background: linear-gradient(135deg, #5DEBFF 0%, #a5b4fc 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }

    .subtitle {
      color: #cbd5e1;
    }
  }

  .hero-description {
    color: #e2e8f0;

    strong {
      color: #a5b4fc;
    }
  }

  .btn {
    &.btn-primary {
      background: linear-gradient(135deg, #5DEBFF 0%, #7e55ff 100%);
      box-shadow: 0 4px 20px rgba(126, 85, 255, 0.4);

      &:hover {
        box-shadow: 0 8px 30px rgba(126, 85, 255, 0.5);
      }
    }

    &.btn-secondary {
      background: rgba(30, 41, 59, 0.8);
      color: #a5b4fc;
      border-color: rgba(126, 85, 255, 0.3);

      &:hover {
        background: rgba(51, 65, 85, 0.8);
        border-color: #7e55ff;
      }
    }
  }

  .hero-stats {
    .stat-number {
      background: linear-gradient(135deg, #5DEBFF 0%, #a5b4fc 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }

    .stat-label {
      color: #94a3b8;
    }
  }

  .features-section {
    background: linear-gradient(180deg, rgba(15, 23, 42, 0.5) 0%, rgba(30, 41, 59, 0.3) 100%);

    &::before {
      background: radial-gradient(circle at 50% 50%, rgba(126, 85, 255, 0.05) 0%, transparent 70%);
    }
  }

  .section-title {
    .gradient-text {
      background: linear-gradient(135deg, #5DEBFF 0%, #a5b4fc 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }
  }

  .feature-card {
    background: linear-gradient(135deg, rgba(30, 41, 59, 0.9), rgba(51, 65, 85, 0.9));
    border-color: rgba(126, 85, 255, 0.2);

    &::before {
      background: linear-gradient(135deg, rgba(126, 85, 255, 0.05), rgba(0, 201, 255, 0.05));
    }

    &::after {
      background: linear-gradient(135deg, #7e55ff, #5DEBFF);
    }

    &:hover {
      box-shadow: 0 20px 40px -10px rgba(126, 85, 255, 0.4);
      border-color: transparent;
    }

    .feature-icon {
      background: linear-gradient(135deg, #5DEBFF 0%, #7e55ff 100%);
      box-shadow: 0 8px 16px -4px rgba(126, 85, 255, 0.4);
    }

    h3 {
      color: #f1f5f9;
    }

    p {
      color: #cbd5e1;
    }
  }

  .quick-links-section {
    background: transparent;
  }

  .link-card {
    background: linear-gradient(135deg, rgba(30, 41, 59, 0.6), rgba(51, 65, 85, 0.6));
    border-color: rgba(126, 85, 255, 0.2);

    &:hover {
      border-color: #7e55ff;
      background: linear-gradient(135deg, rgba(30, 41, 59, 0.8), rgba(51, 65, 85, 0.8));
      box-shadow: 0 10px 20px -5px rgba(126, 85, 255, 0.3);
    }

    .link-icon {
      filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.3));
    }

    .link-content h4 {
      color: #f1f5f9;
    }

    .link-content p {
      color: #cbd5e1;
    }

    .link-arrow {
      color: #a5b4fc;
    }
  }
  } // 关闭.home-page
}
</style>