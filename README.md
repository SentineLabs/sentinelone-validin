# S1 Validin

Synapse Rapid Power-Up for [Validin](https://validin.com) web intelligence platform. Enriches Synapse with DNS records, HTTP crawl data, SSL certificates, and WHOIS information.

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

- **DNS Intelligence** - Forward/reverse DNS lookups with historical data
- **HTTP Crawling** - Web content, headers, favicons from 850M+ daily crawls
- **SSL Certificates** - Certificate chains and CT logs
- **WHOIS Data** - Registration and ownership history
- **Bulk Enrichment** - Combined DNS, HTTP, and WHOIS in one command

## Documentation

- [Admin Guide](docs/admin_guide.md) - Installation and configuration
- [User Guide](docs/user_guide.md) - Commands and usage examples
- [Package Documentation](docs/package_documentation.md) - Technical details
- [Crawler Info](docs/crawlr.md) - How Validin crawls the web

## Requirements

- Synapse `>=2.144.0,<3.0.0`
- Valid Validin API key
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

## Support

- Slack: #validin-sentinelone
- Repo: https://ghe.eng.sentinelone.tech/aaron-stephens/s1-validin