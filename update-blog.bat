# 博客自动更新脚本
# 每天定时从 GitHub 拉取最新文章并部署

cd D:\hexo-blog

# 拉取最新文章
git pull origin master

# 安装依赖（如果需要）
call pnpm install

# 构建博客
call pnpm hexo generate

# 推送到 GitHub（触发 Actions 自动部署）
git push origin master
