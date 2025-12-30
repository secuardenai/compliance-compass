# ComplianceCompass REST API Documentation

A simple, static JSON API for accessing compliance control mappings across OWASP Proactive Controls, ISO27001:2013, and NIST SSDF.

## Base URL

```
https://secuardenai.github.io/compliance-compass
```

## Features

- **Static JSON endpoints** - Fast, CDN-cached responses
- **No authentication required** - Open access for all
- **CORS-enabled** - Use from any domain
- **Zero rate limits** - Hosted on GitHub Pages
- **Version controlled** - All data tracked in Git

## Response Format

All endpoints return JSON with the following structure:

```json
{
  "meta": {
    "version": "1.0.0",
    "generated": "2025-12-29T12:00:00Z",
    "total": 137,
    "endpoint": "/api/all.json"
  },
  "data": [ /* array of controls or single control object */ ]
}
```

## Endpoints

### 1. Get All Controls

Retrieve all compliance controls across all standards.

**Endpoint:** `/api/all.json`

**Example Request:**
```bash
curl https://secuardenai.github.io/compliance-compass/api/all.json
```

**Example with JavaScript:**
```javascript
fetch('https://secuardenai.github.io/compliance-compass/api/all.json')
  .then(response => response.json())
  .then(data => {
    console.log(`Total controls: ${data.meta.total}`);
    console.log('Controls:', data.data);
  });
```

**Response:**
```json
{
  "meta": {
    "version": "1.0.0",
    "generated": "2025-12-29T12:00:00Z",
    "total": 137,
    "endpoint": "/api/all.json"
  },
  "data": [
    {
      "id": "C1-1",
      "standard": "OWASP",
      "category": "C1: Define Security Requirements",
      "title": "Verify the use of a secure software development lifecycle...",
      "description": "",
      "mappings": {
        "owasp": [],
        "iso27001": ["A.14.1.1"],
        "nist": ["PO.1.1", "PO.1.4"]
      },
      "recommendation": "Create a secure development lifecycle program..."
    },
    // ... 136 more controls
  ]
}
```

---

### 2. Get Controls by Standard

Filter controls by a specific security standard.

**Available Standards:**
- `owasp` - OWASP Proactive Controls
- `iso27001` - ISO27001:2013 (AppSec controls)
- `nist` - NIST Secure Software Development Framework (SSDF)

**Endpoints:**
- `/api/standards/owasp.json`
- `/api/standards/iso27001.json`
- `/api/standards/nist.json`

**Example Request:**
```bash
curl https://secuardenai.github.io/compliance-compass/api/standards/owasp.json
```

**Example with Python:**
```python
import requests

response = requests.get(
    'https://secuardenai.github.io/compliance-compass/api/standards/owasp.json'
)
data = response.json()

print(f"Total OWASP controls: {data['meta']['total']}")
for control in data['data']:
    print(f"{control['id']}: {control['title']}")
```

---

### 3. Get Controls by Category

Filter controls by category slug.

**Endpoint Pattern:** `/api/categories/{category-slug}.json`

**Example Categories:**
- `c1-define-security-requirements`
- `c2-leverage-security-frameworks-and-libraries`
- `c3-secure-database-access`
- `management-of-privileged-access-rights`
- `key-management`
- `define-security-requirements-for-software-development`

See the full list of 54 categories in `/api/index.json`

**Example Request:**
```bash
curl https://secuardenai.github.io/compliance-compass/api/categories/c1-define-security-requirements.json
```

---

### 4. Get Individual Control

Retrieve detailed information for a specific control by its ID.

**Endpoint Pattern:** `/api/controls/{control-id}.json`

**Control ID Format:**
- OWASP: `c1-1`, `c2-1`, `c10-6`
- ISO27001: `a-9-2-3`, `a-14-1-1`
- NIST: `po-1-1`, `ps-1-1`, `rv-3-4`

**Example Request:**
```bash
curl https://secuardenai.github.io/compliance-compass/api/controls/c1-1.json
```

**Response:**
```json
{
  "meta": {
    "version": "1.0.0",
    "generated": "2025-12-29T12:00:00Z",
    "total": 1,
    "endpoint": "/api/controls/c1-1.json"
  },
  "data": {
    "id": "C1-1",
    "standard": "OWASP",
    "category": "C1: Define Security Requirements",
    "title": "Verify the use of a secure software development lifecycle...",
    "description": "",
    "mappings": {
      "owasp": [],
      "iso27001": ["A.14.1.1"],
      "nist": ["PO.1.1", "PO.1.4"]
    },
    "recommendation": "Create a secure development lifecycle program..."
  }
}
```

---

### 5. Get Control Mappings

Retrieve only the cross-standard mappings for a specific control.

**Endpoint Pattern:** `/api/mappings/{control-id}.json`

**Example Request:**
```bash
curl https://secuardenai.github.io/compliance-compass/api/mappings/c1-1.json
```

**Response:**
```json
{
  "meta": {
    "version": "1.0.0",
    "generated": "2025-12-29T12:00:00Z",
    "total": 1,
    "endpoint": "/api/mappings/c1-1.json"
  },
  "data": {
    "id": "C1-1",
    "standard": "OWASP",
    "title": "Verify the use of a secure software development lifecycle...",
    "mappings": {
      "owasp": [],
      "iso27001": ["A.14.1.1"],
      "nist": ["PO.1.1", "PO.1.4"]
    }
  }
}
```

---

### 6. API Index

Discover all available endpoints and metadata.

**Endpoint:** `/api/index.json`

**Example Request:**
```bash
curl https://secuardenai.github.io/compliance-compass/api/index.json
```

---

## Data Model

### Control Object

| Field | Type | Description |
|-------|------|-------------|
| `id` | String | Unique control identifier (e.g., `C1-1`, `A.14.1.1`, `PO.1.1`) |
| `standard` | String | Standard name: `OWASP`, `ISO27001`, or `NIST` |
| `category` | String | Control category or domain |
| `title` | String | Control requirement or recommendation |
| `description` | String | Detailed description (may be empty) |
| `mappings` | Object | Cross-standard mappings |
| `mappings.owasp` | Array | Array of OWASP control IDs |
| `mappings.iso27001` | Array | Array of ISO27001 control IDs |
| `mappings.nist` | Array | Array of NIST practice IDs |
| `recommendation` | String | Implementation guidance and references |

---

## Use Cases

### 1. CI/CD Integration

Check if your security controls satisfy multiple compliance frameworks:

```bash
#!/bin/bash
# Check which standards a control satisfies

CONTROL_ID="c1-1"
API_URL="https://secuardenai.github.io/compliance-compass/api/mappings/$CONTROL_ID.json"

curl -s $API_URL | jq '.data.mappings'
```

### 2. Compliance Dashboard

Build a dashboard showing compliance coverage:

```javascript
// Fetch all controls and calculate coverage
async function getComplianceCoverage() {
  const response = await fetch(
    'https://secuardenai.github.io/compliance-compass/api/all.json'
  );
  const { data } = await response.json();

  // Group by standard
  const coverage = data.reduce((acc, control) => {
    acc[control.standard] = (acc[control.standard] || 0) + 1;
    return acc;
  }, {});

  console.log('Compliance Coverage:', coverage);
}
```

### 3. Gap Analysis

Find controls that map across all three standards:

```python
import requests

response = requests.get(
    'https://secuardenai.github.io/compliance-compass/api/all.json'
)
controls = response.json()['data']

# Find controls with mappings to all standards
complete_mappings = [
    c for c in controls
    if (len(c['mappings']['owasp']) > 0 or c['standard'] == 'OWASP') and
       (len(c['mappings']['iso27001']) > 0 or c['standard'] == 'ISO27001') and
       (len(c['mappings']['nist']) > 0 or c['standard'] == 'NIST')
]

print(f"Controls with complete cross-standard mappings: {len(complete_mappings)}")
```

### 4. Documentation Generation

Generate compliance documentation from the API:

```python
import requests
import markdown

def generate_compliance_doc(standard):
    url = f'https://secuardenai.github.io/compliance-compass/api/standards/{standard}.json'
    response = requests.get(url)
    controls = response.json()['data']

    markdown_doc = f"# {standard.upper()} Compliance Controls\n\n"

    for control in controls:
        markdown_doc += f"## {control['id']}: {control['title']}\n\n"
        markdown_doc += f"{control['recommendation']}\n\n"

        # Add mappings
        if any(control['mappings'].values()):
            markdown_doc += "**Cross-Standard Mappings:**\n"
            for std, ids in control['mappings'].items():
                if ids:
                    markdown_doc += f"- {std.upper()}: {', '.join(ids)}\n"
            markdown_doc += "\n"

    return markdown_doc

# Generate documentation for OWASP
doc = generate_compliance_doc('owasp')
with open('owasp-controls.md', 'w') as f:
    f.write(doc)
```

---

## Error Handling

Since this is a static API, errors are limited to:

- **404 Not Found** - Endpoint or control ID doesn't exist
- **Network errors** - Connection issues (rare with GitHub Pages CDN)

**Example Error Handling:**

```javascript
async function getControl(controlId) {
  try {
    const response = await fetch(
      `https://secuardenai.github.io/compliance-compass/api/controls/${controlId}.json`
    );

    if (!response.ok) {
      throw new Error(`Control ${controlId} not found`);
    }

    return await response.json();
  } catch (error) {
    console.error('API Error:', error);
    return null;
  }
}
```

---

## CORS Support

All endpoints support Cross-Origin Resource Sharing (CORS). You can make requests from any domain:

```javascript
// Works from any website
fetch('https://secuardenai.github.io/compliance-compass/api/all.json')
  .then(response => response.json())
  .then(data => console.log(data));
```

---

## Rate Limits

**There are no rate limits.** Since this is a static API hosted on GitHub Pages, you can make as many requests as needed. However, please be respectful and implement caching on your end for better performance.

**Recommended Caching:**

```javascript
// Cache API responses for 1 hour
const CACHE_DURATION = 3600000; // 1 hour in milliseconds
const cache = new Map();

async function getCachedData(url) {
  const now = Date.now();
  const cached = cache.get(url);

  if (cached && (now - cached.timestamp) < CACHE_DURATION) {
    return cached.data;
  }

  const response = await fetch(url);
  const data = await response.json();

  cache.set(url, { data, timestamp: now });
  return data;
}
```

---

## Versioning

The API version is included in the `meta.version` field of each response. Currently at `v1.0.0`.

Future versions will maintain backward compatibility. Breaking changes will result in a new major version.

---

## Contributing

Found an error in the mappings or have suggestions? Please:

1. Open an issue: [GitHub Issues](https://github.com/SecuardenAI/compliance-compass/issues)
2. Submit a pull request with corrections to the CSV source files in `/temp-data/data_files/`
3. Include evidence for any mapping changes (official documentation, standards references)

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## License

This API and its data are available under the [MIT License](LICENSE). Free to use for commercial and non-commercial purposes.

---

## Support

- **Documentation**: This file
- **Issues**: [GitHub Issues](https://github.com/SecuardenAI/compliance-compass/issues)
- **Discussions**: [GitHub Discussions](https://github.com/SecuardenAI/compliance-compass/discussions)
- **Website**: [ComplianceCompass](https://secuardenai.github.io/compliance-compass)

---

## Changelog

### v1.0.0 (2025-12-29)
- Initial API release
- 137 controls across OWASP, ISO27001, and NIST SSDF
- 333 total endpoint files
- Full cross-standard mapping support
