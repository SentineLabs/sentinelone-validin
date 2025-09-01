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
- `inet:http:request._s1:validin:response:body:sha1` - SHA1 of crawled body
- `inet:http:request._s1:validin:response:favicon` - Favicon bytes
- `inet:http:request._s1:validin:response:favicon:md5` - MD5 of favicon

## API Integration

### Endpoints

#### `s1.validin.certs`

- `/api/axon/domain/certificates/:domain` - Certificate Transparency Stream

#### `s1.validin.dns`

- `/api/axon/domain/dns/history/:domain` - Domain DNS history
- `/api/axon/domain/dns/hostname/:domain` - Domain PTR records
- `/api/axon/domain/dns/extra/:domain` - Domain MX, TXT, and CNAME records
- `/api/axon/ip/dns/history/:ip` - IP DNS history
- `/api/axon/ip/dns/hostname/:ip` - IP PTR records

#### `s1.validin.download`

- `/api/axon/hash/content/certificate/sha1/:hash` - Certificate bytes
- `/api/axon/hash/content/html/sha1/:hash` - Response body bytes 
- `/api/axon/hash/content/favicon/md5/:hash` - Favicon bytes

#### `s1.validin.enrich`

- `/api/v2/domain/combined/connections/:domain` - Domain connections

#### `s1.validin.http`

- `/api/axon/domain/crawl/history/:domain` - Domain Crawl history
- `/api/axon/ip/crawl/history/{ip}` - IP crawl history

#### `s1.validin.whois`

- `/api/axon/domain/registration/history/:domain` - Registration history

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
