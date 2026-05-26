# Netlify Deployment Steps

## Deploy From GitHub

1. In Netlify, select **Add new project** > **Import an existing project**.
2. Choose **GitHub** and select the repository `willx1-xu/-`.
3. Select the production branch `main`.
4. Leave **Base directory** empty.
5. Leave **Build command** empty. This site is static HTML and requires no build.
6. Set **Publish directory** to `.`.
7. Select **Deploy**.

The repository already includes `netlify.toml`, which uses the repository root as the publish directory, caches `/assets/*`, and serves `404.html` for missing paths.

## Enable RFQ Form Handling

1. Open the deployed site in Netlify.
2. Go to **Forms** and select **Enable form detection**.
3. Trigger a new deploy from **Deploys** > **Trigger deploy** > **Deploy site**.
4. After that deploy completes, confirm the form named `rfq` appears under **Forms**.
5. Under **Project configuration** > **Notifications** > **Emails and webhooks**, add a **Form submission notification** for `rfq` submissions to `xuke@link-jl.com`.
6. Submit one test RFQ from the deployed website and confirm the submission appears in Netlify and the email notification is received.

All RFQ entry points submit the same `rfq` form fields: name, email, phone / WhatsApp, company, country, interest, voltage / capacity / power, quantity / project scale, and message.

## Before Production Launch

- In Netlify, open **Domain management** > **Add domain** to attach the production domain and complete the DNS instructions shown by Netlify.
- The canonical production domain is `https://www.link-jl.com`; SEO URL files should target this domain before binding it in Netlify.
- Confirm this domain in `sitemap.xml`, `robots.txt`, canonical tags, and Open Graph URLs, then redeploy.
- Verify `/404.html`, `/robots.txt`, and `/sitemap.xml` on the deployed domain.

## References

- [Deploy from a repository](https://docs.netlify.com/deploy/create-deploys/)
- [Netlify Forms setup](https://docs.netlify.com/forms/setup/)
- [Form submission notifications](https://docs.netlify.com/manage-notifications/notification-emails/)
