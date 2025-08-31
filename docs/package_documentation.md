# S1 Validin Package Documentation

## Architecture

### Modules
| Module | Description |
|--------|-------------|
| `s1.validin` | Core module |
| `s1.validin.api` | Validin API client |
| `s1.validin.download` | Content downloader |
| `s1.validin.ingest` | Data ingestion base |
| `s1.validin.ingest.crawlr` | HTTP crawl ingestion |
| `s1.validin.ingest.ctstream` | Certificate transparency |
| `s1.validin.ingest.dns` | DNS record ingestion |
| `s1.validin.ingest.registration` | WHOIS ingestion |
| `s1.validin.model` | Data model extensions |
| `s1.validin.privsep` | Privilege separation |

### Data Model Extensions
- `inet:http:request._s1:validin:response:body_hash` - SHA1 of crawled body
- `inet:http:request._s1:validin:response:favicon_hash` - MD5 of favicon
- `inet:http:request._s1:validin:response:favicon` - Favicon bytes

## API Integration

### Endpoints
- `/v2/domain/combined/connections/{fqdn}` - Domain connections
- `/axon/domain/crawl/history/{fqdn}` - Crawl history
- `/axon/ip/crawl/history/{ip}` - IP crawl history
- `/v2/ct/{fqdn}` - Certificate transparency
- `/axon/hash/content/html/sha1/{sha1}` - HTML content
- `/axon/hash/content/favicon/md5/{md5}` - Favicon content

### Authentication
- API key stored in Synapse $lib.globals and $lib.user.vars
- Global: `s1:validin:api:key`
- User: `s1:validin:api:key:self`

## Data Sources

### Crawling Coverage
- **IP Space:** 3x weekly full scans
- **Priority Domains:** ~350M domains every 2 days
- **Full Domain List:** ~4.8B domains every 2 weeks
- **Method:** Headless HTTP/S crawling

### Data Types
1. **DNS Records**
   - A/AAAA records
   - Forward/reverse lookups
   - Historical data

2. **HTTP Crawl**
   - Response headers
   - HTML content (SHA1)
   - Favicons (MD5)
   - Redirects (up to 3)

3. **Certificates**
   - X.509 certificates
   - Certificate chains
   - CT logs

4. **WHOIS**
   - Registration data
   - Historical changes

## Storm Commands

### Setup Commands
- `s1.validin.setup.apikey` - Configure API key
- `s1.validin.setup.apihostname` - Set API hostname

### Data Commands
- `s1.validin.dns` - DNS lookups
- `s1.validin.http` - HTTP crawl data
- `s1.validin.certs` - SSL certificates
- `s1.validin.whois` - WHOIS records
- `s1.validin.enrich` - Combined enrichment
- `s1.validin.download` - Content download

## Optic Actions
Power-Up provides right-click actions in Optic UI:
- DNS lookup (with/without wildcards)
- WHOIS lookup (with/without wildcards)
- Certificate fetch (with/without wildcards)
- HTTP history
- Full enrichment
- Download & parse
