#!/bin/bash

# ClaudeHub 部署脚本
# 用于在服务器上自动部署 VuePress 网站

set -e  # 如果任何命令失败，立即退出

echo "🚀 开始部署 ClaudeHub..."

# 配置变量
REPO_URL="https://github.com/Mr0bean/ClaudeHub.git"
DEPLOY_DIR="/var/www/claudehub-deploy"
WEB_DIR="/var/www/claudehub"
NGINX_CONFIG="/etc/nginx/sites-available/claudehub"

# 1. 克隆或更新代码
if [ -d "$DEPLOY_DIR" ]; then
    echo "📥 更新现有代码..."
    cd $DEPLOY_DIR
    git pull origin main
else
    echo "📥 克隆代码仓库..."
    git clone $REPO_URL $DEPLOY_DIR
    cd $DEPLOY_DIR
fi

# 2. 安装依赖并构建
echo "🔧 安装依赖..."
cd final-site
npm install

echo "🏗️ 构建 VuePress 项目..."
npm run build

# 3. 部署到 web 目录
echo "📁 部署文件..."
rm -rf $WEB_DIR/*
cp -r docs/.vuepress/dist/* $WEB_DIR/

# 4. 配置 Nginx
echo "⚙️ 配置 Nginx..."
if [ -f "../nginx-config/claudehub.conf" ]; then
    cp ../nginx-config/claudehub.conf $NGINX_CONFIG
    nginx -t && systemctl reload nginx
    echo "✅ Nginx 配置已更新"
else
    echo "⚠️ Nginx 配置文件不存在，请手动配置"
fi

# 5. 设置权限
chown -R www-data:www-data $WEB_DIR
chmod -R 755 $WEB_DIR

echo "🎉 部署完成！"
echo "📍 访问地址: http://YOUR_SERVER_IP/ClaudeHub/"