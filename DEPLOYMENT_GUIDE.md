# Apex Power Systems — Deployment Package

Apex 独立站部署包(充电桩 + 充电控制器聚焦,极简高端白设计)

## 包含内容

- 26 个 HTML 页面(首页、产品、解决方案、案例、关于、联系、隐私政策、404)
- 10 个充电产品页:5 充电桩 + 3 控制器 + 2 协议板
- 全部图片已优化为 WebP(比 JPG 小 49%,带懒加载)
- 结构化数据(Product / Organization Schema)
- GA4 分析代码(占位 ID:`G-XXXXXXXXXX` — 需替换为真实 ID)
- 三套部署配置:Netlify、Vercel、Apache

## 快速部署

### Netlify(推荐,表单开箱即用)
1. 解压本包,把 `indie-site-deploy/` 内容推到一个 GitHub 仓库
2. 在 Netlify 导入该仓库
3. 构建命令:无(纯静态);发布目录:`.`
4. 部署后在 Netlify 后台配置 `rfq` 表单邮件通知 → `xuke@link-jl.com`

### Vercel
1. 推送到 GitHub 仓库
2. Vercel 导入,使用默认静态设置,项目根目录为仓库根目录
3. 注意:表单提交在 Vercel 上不生效,需另行接表单后端

### cPanel / Apache
1. 上传所有文件到 web 根目录
2. 保留 `.htaccess`(已含 gzip、缓存、404 配置)
3. 启用 SSL

## 上线前必做

1. **替换 GA4 ID**:所有页面中 `G-XXXXXXXXXX` → 你的真实 Measurement ID
2. **域名解析**:`www.link-jl.com` 解析到托管平台并启用 SSL
3. **表单通知**:Netlify Forms 后台配置邮件通知
4. **sitemap 域名**:如更换域名,更新 `sitemap.xml` / `robots.txt` / canonical 标签

## 目录结构

```text
/
  index.html          首页(产品 + 案例 + 询盘)
  products/           产品列表 + 10 个产品详情页
  solutions/          3 个充电解决方案
  about/ quality/     公司介绍、质量
  contact/            联系 / RFQ 表单
  privacy/            隐私政策
  assets/             图片(WebP)+ 全站 CSS
  netlify.toml        Netlify 配置
  vercel.json         Vercel 配置
  .htaccess           Apache 配置
  sitemap.xml         23+1 条 URL
  robots.txt          SEO
  404.html            自定义 404
```

## 联系

- 邮箱:xuke@link-jl.com
- WhatsApp:+86 13201571341
