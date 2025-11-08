# `s1-validin` User Guide

## Overview

`s1-validin` integrates Validin's data into Synapse, providing DNS records, HTTP crawl data, certificates, and WHOIS information.

## Commands

### DNS Records

```storm
// Basic DNS lookup
inet:fqdn=example.com | s1.validin.dns

// Include subdomains
inet:fqdn=example.com | s1.validin.dns --wildcard

// Filter by date
inet:fqdn=example.com | s1.validin.dns --first-seen 2024/01/01 --last-seen 2024/12/31

// Reverse DNS (IP to domain)
inet:ipv4=1.2.3.4 | s1.validin.dns
```

### HTTP Crawl Data

```storm
// Get crawl history for domain
inet:fqdn=example.com | s1.validin.http

// Get crawl history for IP
inet:ipv4=1.2.3.4 | s1.validin.http

// Download HTTP content
inet:fqdn=example.com | s1.validin.http --download
```

### Certificates

```storm
// Get certificates
inet:fqdn=example.com | s1.validin.certs

// Include wildcard certificates
inet:fqdn=example.com | s1.validin.certs --wildcard
```

### WHOIS Records

```storm
// Get WHOIS data
inet:fqdn=example.com | s1.validin.whois

// Include subdomains
inet:fqdn=example.com | s1.validin.whois --wildcard
```

### Enrichment

```storm
// Comprehensive enrichment (DNS + HTTP + WHOIS)
inet:fqdn=example.com | s1.validin.enrich

// With date filtering
inet:fqdn=example.com | s1.validin.enrich --first-seen 2024/01/01
```

### Download Content

```storm
// Download certificate
crypto:x509:cert | s1.validin.download

// Download and parse
crypto:x509:cert | s1.validin.download --yield | fileparser.parse
```

### HTTP Pivoting

```storm
// Pivot from an HTTP request to related artifacts
inet:http:request=<guid> | s1.validin.http.pivot

// Pivot from a hash (MD5, SHA1, or SHA256)
hash:sha256=<value> | s1.validin.http.pivot

// Filter by specific category
inet:http:request=<guid> | s1.validin.http.pivot --category BODY_SHA1

// Preview without creating nodes
inet:http:request=<guid> | s1.validin.http.pivot --dry-run

// Filter by date range
hash:md5=<value> | s1.validin.http.pivot --first-seen 2024/01/01 --last-seen 2024/12/31
```

**Available Pivot Categories:**
- `BANNER_0_HASH` - Banner hash pivots
- `BODY_SHA1` - HTTP body SHA1 pivots
- `CERT_FINGERPRINT` - Certificate fingerprint pivots
- `CERT_FINGERPRINT_SHA256` - Certificate SHA256 pivots
- `CLASS_0_HASH` - CLASS v0.0 hash pivots
- `CLASS_1_HASH` - CLASS v0.1 hash pivots
- `FAVICON_HASH` - Favicon hash pivots
- `HEADER_HASH` - Header hash pivots

## Common Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--first-seen` | Start date filter | None |
| `--last-seen` | End date filter | None |
| `--wildcard` | Include subdomains | False |
| `--limit` | Max records | 20000 |
| `--yield` | Yield nodes | False |
| `--category` | Pivot category filter | None |
| `--dry-run` | Preview without creating nodes | False |

## Tips

- Use `--wildcard` for comprehensive subdomain discovery
- Combine with native Synapse pivots for powerful analysis
- Set reasonable `--limit` values for large datasets
- Use date filters to focus on specific timeframes
- Use `--dry-run` with `s1.validin.http.pivot` to preview results before creating nodes
- Pivot operations can discover related infrastructure based on HTTP fingerprints and hashes
