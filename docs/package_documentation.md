# `s1-validin` Package Documentation

## Architecture

### Modules

| Module | Description |
|--------|-------------|
| `s1.validin` | Core module |
| `s1.validin.api` | Validin API client |
| `s1.validin.download` | Content downloader |
| `s1.validin.ingest` | Data ingestion base |
| `s1.validin.ingest.crawlr` | HTTP crawl ingestion |
| `s1.validin.ingest.ctstream` | Certificate Transparency |
| `s1.validin.ingest.dns` | DNS record ingestion |
| `s1.validin.ingest.pivot` | Hash pivot ingestion |
| `s1.validin.ingest.registration` | WHOIS ingestion |
| `s1.validin.model` | Data model extensions |
| `s1.validin.privsep` | User privilege separation |
| `s1.validin.privsep.admin` | Admin privilege separation |

### Data Model Extensions

- `inet:http:request._s1:validin:response:body:sha1` - SHA1 of crawled body
- `inet:http:request._s1:validin:response:favicon` - Favicon bytes
- `inet:http:request._s1:validin:response:favicon:md5` - MD5 of favicon
- `inet:http:request._s1:validin:response:banner_0:md5` - MD5 of banner hash
- `inet:http:request._s1:validin:response:class_0:md5` - CLASS v0.0 hash
- `inet:http:request._s1:validin:response:class_1:md5` - CLASS v0.1 hash

## API Integration

### Endpoints

Breakdown of endpoints used by command.

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

#### `s1.validin.http.pivot`

- `/api/axon/hash/pivots/:hash` - Hash pivot search
- `/api/axon/hash/pivots/:hash/:category` - Category-filtered hash pivot

#### `s1.validin.whois`

- `/api/axon/domain/registration/history/:domain` - Registration history

### Authentication

API key stored in Synapse `$lib.globals` and `$lib.user.vars`

- Global: `s1:validin:api:key`
- User: `s1:validin:api:key:self`
