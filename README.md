# CloudFlare-DNS-Updater
A little Python script to update your cloud flare DNS if you have a dynamic IP  
Cloudflare does not sponsor nor endorse this script!

# setup
1. Login into your CloudFlare account  
2. Get your `Global API Key` from [here](https://www.cloudflare.com/a/account/my-account)
3. Paste your `Global API Key` as the `CFAPI_KEY`
4. Enter your email as `CFAPI_EMAIL`
5. Get your Zone ID from `https://www.cloudflare.com/a/overview/<YOUR DOMAIN>` (replace `<YOUR DOMAIN>` with your domain name)
6. Paste your `Zone ID` as `CFAPI_ZONE`
7. Enter the domain you want to update as `CFAPI_DOMAIN_NAME` (for example: `www.finlaydag33k.nl` - Must be part of your zone!)
8. Enter the domain type you want to update as  `CFAPI_DOMAIN_TYPE` (so for example: `www.finlaydag33k.nl` is an `A`-Type, so I'd enter `A`)
9. run the script!