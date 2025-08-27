# S1 Validin Admin Guide

## Installation

### Requirements
- Synapse >=2.144.0,<3.0.0
- Synapse Axon (for download features)
- Synapse FileParser (for parsing downloaded content)

### Install Steps
```bash
# Load into Synapse
storm> pkg.load --path /path/to/s1-validin.yaml
```

## Configuration

### API Key Setup (Required)
```storm
// Global key (all users)
s1.validin.setup.apikey <YOUR_API_KEY>

// Per-user key
s1.validin.setup.apikey <YOUR_API_KEY> --self
```

### API Hostname (Optional)
```storm
// Default: pilot.validin.com
s1.validin.setup.apihostname <hostname>
```

## Permissions

| Permission | Gate | Description |
|------------|------|-------------|
| `s1.validin.user` | cortex | Access to Validin API commands |

### Grant Permissions
```storm
auth.user.addrule <username> s1.validin.user
```

## Monitoring

### Check API Status
```storm
// Test API connection
inet:fqdn=example.com | s1.validin.dns --limit 1
```

### Rate Limits
- Default: 20,000 records per query
- Adjust with `--limit` parameter

## Troubleshooting

### Common Issues

**API Key Invalid**
- Verify key with Validin support
- Check user vs global key settings

**No Results**
- Verify target exists in Validin data
- Check date range filters
- Try with `--wildcard` flag

**Timeout Errors**
- Reduce `--limit` value
- Narrow date range with `--first-seen`/`--last-seen`
