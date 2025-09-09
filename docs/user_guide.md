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
inet:fqdn=example.com | s1.validin.dns --first-seen 2024-01-01 --last-seen 2024-12-31

// Reverse DNS (IP to domain)
inet:ipv4=1.2.3.4 | s1.validin.dns
```

### HTTP Crawl Data

```storm
// Get crawl history for domain
inet:fqdn=example.com | s1.validin.http

// Get crawl history for IP
inet:ipv4=1.2.3.4 | s1.validin.http

// Download HTML/favicon content
inet:fqdn=example.com | s1.validin.http --download
```

### Certificates

```storm
// Get certificates
inet:fqdn=example.com | s1.validin.certs

// Include wildcard certificates
inet:fqdn=example.com | s1.validin.certs --wildcard

// Download certificate files
inet:fqdn=example.com | s1.validin.certs --download
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
inet:fqdn=example.com | s1.validin.enrich --first-seen 2024-01-01
```

### Download Content

```storm
// Download certificate
crypto:x509:cert | s1.validin.download

// Download and parse
crypto:x509:cert | s1.validin.download --yield | fileparser.parse
```

## Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--first-seen` | Start date filter | None |
| `--last-seen` | End date filter | None |
| `--wildcard` | Include subdomains | False |
| `--limit` | Max records | 20000 |
| `--yield` | Yield nodes | False |
| `--download` | Download content | False |

## Use Cases

### Threat Investigation

```storm
// Investigate suspicious domain
inet:fqdn=malicious.example | s1.validin.enrich
  | -> inet:dns:a -> inet:ipv4
  | s1.validin.dns
```

### Infrastructure Mapping

```storm
// Map domain infrastructure
inet:fqdn=target.com | s1.validin.dns --wildcard
  | -> inet:ipv4
  | uniq
```

### Certificate Analysis

```storm
// Analyze SSL certificates
inet:fqdn=example.com | s1.validin.certs --download
  | -> crypto:x509:cert
  | fileparser.parse
```

## Tips

- Use `--wildcard` for comprehensive subdomain discovery
- Combine with native Synapse pivots for powerful analysis
- Set reasonable `--limit` values for large datasets
- Use date filters to focus on specific timeframes
