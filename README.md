# `sentinelone-validin`

`sentinelone-validin` is a [Synapse Rapid Power-Up](https://synapse.docs.vertex.link/en/latest/synapse/power_ups.html) for [Validin](https://validin.com). It provides commands to query for and model DNS records, HTTP crawl data, TLS certificates, and WHOIS information.

## Quick Start

```bash
# Load into Synapse
storm> pkg.load --path /path/to/s1-validin.yaml

# Configure API key
storm> s1.validin.setup.apikey <YOUR_API_KEY>

# Test connection
storm> inet:fqdn=example.com | s1.validin.dns
```

## Features

- **DNS History** - Forward/reverse DNS lookups with historical data
- **HTTP Crawling** - HTTP bodies, headers, favicons, and certificates from 850M+ daily crawls
- **TLS Certificates** - Certificates from the Certificate Transparency Stream
- **WHOIS Data** - Registration and ownership history
- **Bulk Enrichment** - Combined DNS, HTTP, and WHOIS data in one command

## Documentation

- [Admin Guide](docs/admin_guide.md) - Installation and configuration
- [User Guide](docs/user_guide.md) - Commands and usage examples
- [Package Documentation](docs/package_documentation.md) - Technical details

## Requirements

- Synapse `>=2.144.0,<3.0.0`
- Validin API key
- Synapse Axon (for download features)
- Synapse FileParser (for parsing downloaded content)

## Development

```bash
# Install dev dependencies
pip install -e .

# Run tests
pytest

# Debug mode
storm> $lib.debug = $lib.true
```

## Minimal Runtime Setup

In order to run the power-up in a minimal runtime environment, you can use the following command:

```bash
docker compose run --rm storm
```

This will start a storm shell facing the cortex with the power-up loaded. 
Synapse-axon is not included in the minimal runtime setup, however you can still use the download command to download HTTP bodies, certificates, and favicons, then parse.

First load your Api Key 
```
storm> s1.validin.setup.apikey <YOUR_API_KEY>
```
Then you use the powerup as below: 
```
storm> [inet:fqdn=example.com] | s1.validin.dns
```

### Limitations

- Requires Synapse FileParser to process downloaded content (e.g., `inet:http:body`, `crypto:x509:cert`)
  - FileParser is not included in the minimal runtime setup


