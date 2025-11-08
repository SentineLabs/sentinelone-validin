# Changelog

## [3.3.0] - 2025-11-08

### Features

- Add `s1.validin.http.pivot` command for pivoting from HTTP content or hashes to related artifacts
- Support pivoting from `inet:http:request`, `hash:md5`, `hash:sha1`, and `hash:sha256` nodes
- Add category filtering for pivots (BANNER_0_HASH, BODY_SHA1, CERT_FINGERPRINT, etc.)
- Add `s1.validin.ingest.pivot` module for handling pivot data ingestion
- Add new data model extensions:
  - `inet:http:request._s1:validin:response:banner_0:md5` - MD5 banner hash
  - `inet:http:request._s1:validin:response:class_0:md5` - CLASS v0.0 hash
  - `inet:http:request._s1:validin:response:class_1:md5` - CLASS v0.1 hash
- Add dry-run mode to `s1.validin.http.pivot` for previewing results without creating nodes
- Add Optic UI action for HTTP pivot functionality

### Improvements

- Enhanced pivot statistics output for better debugging
- Improved error handling in pivot operations

## [3.2.0] - 2025-11-07

### Features

- WHOIS command now accepts `inet:email` nodes in addition to `inet:fqdn`

### Fixes

- Fixed WHOIS FQDN API handling
- Fixed DNS seen interval not being set correctly

## [3.1.1] - 2025-09-23

### Bugfixes

- Fix an issue where the seen interval was not being set correctly


## [3.1.0] - 2025-09-11

### Initial Public Release

First public version of S1 Validin Rapid Power-Up for Synapse.

### Features

- DNS record lookups (forward/reverse) with historical data
- HTTP crawl history with content download
- TLS certificates
- WHOIS records
- Node enrichment combining all data sources
- Wildcard subdomain discovery
- Date range filtering
- Optic UI right-click actions
