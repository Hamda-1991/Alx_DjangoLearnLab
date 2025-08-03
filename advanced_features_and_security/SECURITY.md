# Security Summary

- `DEBUG = False` to prevent leaking sensitive info.
- CSRF and Session cookies secured.
- CSP headers to limit sources.
- SQL injection avoided using Django ORM and query sanitization.
