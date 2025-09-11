# Changelog

## [3.0.0] - 2025-01-22

### Initial Public Release

First public version of S1 Validin Rapid Power-Up for Synapse.

### Features

- DNS record lookups (forward/reverse) with historical data
- HTTP crawl history with content download
- SSL certificate fetching and analysis
- WHOIS record retrieval
- Comprehensive enrichment combining all data sources
- Wildcard subdomain discovery
- Date range filtering
- Optic UI right-click actions

### Data Sources

- Validin Crawler
- Certificate transparency logs
- Historical DNS and WHOIS records

### Requirements

- Synapse >=2.144.0
- Valid Validin API key
- Synapse Axon (for downloads)
- Synapse FileParser (for parsing)
