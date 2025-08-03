# Security Review

## HTTPS Enforcement

- All traffic is redirected to HTTPS (`SECURE_SSL_REDIRECT = True`)
- HSTS policy is enforced for one year and preloaded by browsers.

## Secure Cookies

- Cookies are only transmitted over HTTPS (`SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE`).

## HTTP Headers

- Clickjacking protection: `X_FRAME_OPTIONS = 'DENY'`
- Content sniffing protection: `SECURE_CONTENT_TYPE_NOSNIFF = True`
- XSS filter enabled: `SECURE_BROWSER_XSS_FILTER = True`

## Deployment

- SSL certificates configured in Nginx.
- HTTP to HTTPS redirect added.
