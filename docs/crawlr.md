# Validin Crawler

_(Composed from a conversation on May 14th 2025 in #validin-sentinelone slack channel.)_

Validin web crawling system discovers and processes web content through IP space and virtual host crawls.

## Crawling Mechanism

**1. IP Space Crawls:**
* **Frequency:** 3 times per week.
* **Duration:** Approximately 1 day per session.
* **Scope:** Scans defined IP address ranges.

**2. Virtual Host Crawls:**
* **Frequency:** Continuous, daily.
* **Scheduling:**
    * **Priority Scan (Short List):**
        * **Content:** ~350 million domains (IPv4 only).
        * **Frequency:** Every 2 days.
        * **Curation:** Sources include block lists, zone files, certificates. Domains removed if inactive in these sources.
    * **Comprehensive Scan (Full List):**
        * **Content:** ~4.8 billion domains (IPv4 only).
        * **Frequency:** Every 2 weeks.
    * **Automation:** Time-driven; manages list creation and curation.

**3. Crawling Stack:**
* **Architecture:** Headless (direct request issuance, no browser rendering).
* **Methodology:** Manages network bytes directly for HTTP/S transactions.

## Crawling Agenda & Behavior

**1. Target Scope:**
* Any domain name resolving to an IPv4 address.

**2. Initial Request Path:**
* Always starts at the root path (`/`).
* Additional paths are only requested via server-issued redirects.

**3. HTTP Redirect Handling:**
* **Policy:** Follows up to 3 HTTP redirects.
* **Conditions:** Redirects must be same-host, same-port, and same-protocol.
* **Mechanism:** Uses `Location:` header. `<meta>` redirect support is backlogged.
* **Host Constraint:** Never leaves the original host (IP or domain) during redirects to prevent exploitation.

**4. Favicon Fetching:**
* **Objective:** Fetches and hashes favicons.
* **Path:** Prioritizes path from HTTP headers; defaults to `/favicon.ico`.
* **Request Counting:** These requests are excluded from daily volume metrics (e.g., "850 million/day" count).

**5. `/ads.txt` Fetching (Discontinued):**
* **History:** Previously fetched on Effective Top-Level Domains plus one (E2LDs).
* **Status:** Discontinued due to low perceived value.