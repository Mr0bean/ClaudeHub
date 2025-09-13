# ClaudeHub 部署文档

## 问题说明

### 遇到的问题
VuePress 构建的静态网站部署到 Nginx 服务器时，静态资源（CSS、JS、图片）无法正确加载，导致页面样式丢失和功能异常。

### 问题原因
1. **VuePress 配置**：项目使用了 `base: '/ClaudeHub/'` 配置
2. **资源路径**：VuePress 生成的 HTML 中资源链接为 `/ClaudeHub/assets/xxx.css`
3. **Nginx 配置不匹配**：默认配置无法正确处理带 base path 的资源请求

### 解决方案
使用 Nginx `rewrite` 规则，将带前缀的资源请求重写为文件系统中的实际路径。

## 部署步骤

### 方法一：自动部署（推荐）

1. **运行部署脚本**：
```bash
# 在服务器上执行
sudo bash scripts/deploy.sh
```

### 方法二：手动部署

1. **克隆代码**：
```bash
cd /var/www
git clone https://github.com/Mr0bean/ClaudeHub.git claudehub-deploy
```

2. **构建项目**：
```bash
cd claudehub-deploy/final-site
npm install
npm run build
```

3. **部署文件**：
```bash
mkdir -p /var/www/claudehub
cp -r docs/.vuepress/dist/* /var/www/claudehub/
```

4. **配置 Nginx**：
```bash
cp nginx-config/claudehub.conf /etc/nginx/sites-available/claudehub
ln -sf /etc/nginx/sites-available/claudehub /etc/nginx/sites-enabled/claudehub
nginx -t && systemctl reload nginx
```

## 核心 Nginx 配置解释

```nginx
# 处理静态资源 - 关键修复点
location ~ ^/ClaudeHub/(assets|img)/ {
    rewrite ^/ClaudeHub/(.*)$ /$1 break;
    try_files $uri =404;
    expires 1y;
    add_header Cache-Control "public, immutable";
}
```

**工作原理**：
- 请求：`/ClaudeHub/assets/style-xxx.css`
- 重写为：`/assets/style-xxx.css`
- 文件系统路径：`/var/www/claudehub/assets/style-xxx.css`

## 更新部署

服务器上运行更新脚本：
```bash
/var/www/update-claudehub.sh
```

## 验证部署

1. **检查页面加载**：访问 `http://YOUR_SERVER_IP/ClaudeHub/`
2. **验证静态资源**：
```bash
curl -I http://YOUR_SERVER_IP/ClaudeHub/assets/style-CPUcPdP3.css
# 应该返回 200 OK，Content-Type: text/css
```
3. **检查控制台**：浏览器开发者工具无 404 错误

## 故障排除

### 静态资源 404
- 检查 Nginx 配置中的 `rewrite` 规则
- 确认文件路径：`ls -la /var/www/claudehub/assets/`

### 样式不生效
- 验证 CSS 文件的 Content-Type：应该是 `text/css`
- 检查浏览器缓存

### 页面无法访问
- 确认 Nginx 配置语法：`nginx -t`
- 检查服务状态：`systemctl status nginx`

## 技术细节

- **VuePress 版本**：支持 base path 配置
- **Nginx 版本**：1.18+ 推荐
- **Node.js 版本**：18.0+ 必需
- **构建输出**：65 个 HTML 页面，完整的中文文档