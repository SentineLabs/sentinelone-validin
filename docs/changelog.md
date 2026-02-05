# Changelog

## [3.4.0] - 2026-02-05

### Features

- Add `s1.validin.reputation` command for domain and IP reputation checks
- Add IP reputation ingestion with ASN and geolocation data
- Add domain reputation ingestion with ranking data (Majestic, Tranco, Umbrella, Anchors)
- Add new data model extensions:
  - `inet:fqdn._s1:validin:verdict` - Reputation verdict for domains
  - `inet:fqdn._s1:validin:reputation` - Reputation score for domains
  - `inet:fqdn._s1:validin:rank:majestic` - Majestic Million rank
  - `inet:fqdn._s1:validin:rank:tranco` - Tranco Top 1M rank
  - `inet:fqdn._s1:validin:rank:umbrella` - Umbrella Top 1M rank
  - `inet:fqdn._s1:validin:rank:anchors` - Validin Top Anchors rank
  - `inet:ipv4._s1:validin:verdict` - Reputation verdict for IPv4
  - `inet:ipv4._s1:validin:reputation` - Reputation score for IPv4
  - `inet:ipv4._s1:validin:rank:pivot_count` - Pivot count for IPv4
  - `inet:ipv4._s1:validin:rank:top_a` - Validin Top A rank for IPv4
  - `inet:ipv6._s1:validin:verdict` - Reputation verdict for IPv6
  - `inet:ipv6._s1:validin:reputation` - Reputation score for IPv6
  - `inet:ipv6._s1:validin:rank:pivot_count` - Pivot count for IPv6
  - `inet:ipv6._s1:validin:rank:top_a` - Validin Top A rank for IPv6

### Improvements

- IP reputation now always parses ASN and geolocation information
- Enhanced ASN modeling using `inet:asnet4` and `inet:asnet6` forms for CIDR-to-ASN relationships
- Improved ownership data processing to handle multiple ownership entries
- Added comprehensive test coverage for reputation functionality

## [3.3.1] - 2025-11-19

### Fixes

- Fixed HTTP crawler certificate handling when no issuer is reported

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
