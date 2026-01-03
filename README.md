# ComplianceCompass 🧭

> The missing layer between AppSec findings and SOC2 / ISO / PCI evidence.
>
>> Security tools find issues. Auditors ask what framework does this satisfy?
>> **ComplianceCompass** answers that.

**ComplianceCompass** is an open-source tool that maps application security requirements across OWASP Proactive Controls, ISO27001:2013, and NIST SSDF. Stop guessing what controls you need to implement—see exactly how security requirements map across frameworks.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/SecuardenAI/compliance-compass)](https://github.com/SecuardenAI/compliance-compass/stargazers)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/SecuardenAI/compliance-compass/pulls)

🌐 **[Live Demo](https://secuardenai.github.io/compliance-compass)** | 📖 **[Documentation](#documentation)** | 🐛 **[Report Bug](https://github.com/SecuardenAI/compliance-compass/issues)**

---

## 🎯 Why ComplianceCompass?

If you've ever tried to understand what you need to implement to be compliant with multiple security standards, you know the pain:

- **Confusing overlap**: Different standards use different terminology for the same concepts
- **Incomplete coverage**: Not all standards cover application security comprehensively  
- **No clear mapping**: It's unclear which controls in one framework correspond to another
- **Implementation gaps**: Knowing _what_ to implement is half the battle

ComplianceCompass solves this by providing:

✅ **Cross-framework mappings** showing how OWASP, ISO27001, and NIST SSDF align  
✅ **Implementation guidance** for each control with actionable recommendations  
✅ **Interactive search** to find controls by keyword, category, or standard  
✅ **Export capabilities** to generate documentation for auditors  


> ### Not a GRC tool. Not a scanner. A translation layer.

## Who this repo is for?
  - Security engineers doing audits
  - Startups prepping for SOC 2
  - Consultants writing compliance reports

## 🚀 Quick Start

### Option 1: Use the Web App

Visit **[compliancecompass.secuarden.com](https://secuardenai.github.io/compliance-compass)** and start exploring immediately. No installation required.

### Option 2: Run Locally

```bash
# Clone the repository
git clone https://github.com/SecuardenAI/compliance-compass.git
cd compliance-compass

# Open in browser
open index.html
# or use a local server
python -m http.server 8000
```

### Option 3: Use as a Library

Coming soon: Python package and npm module for programmatic access.

---

## 📊 Standards Covered

### OWASP Proactive Controls (10 Controls)
Security techniques that should be included in software development to produce secure applications.

### ISO27001:2013 (AppSec Controls)
International standard for information security management systems, filtered for application development requirements.

### NIST SSDF (Secure Software Development Framework)
Framework of fundamental secure software development practices based on established standards.

---

## 🎨 Features

### 🔍 **Interactive Explorer**
- Search across all controls by keyword
- Filter by standard (OWASP, ISO27001, NIST)
- Filter by category (Authentication, Data Protection, etc.)
- See cross-standard mappings instantly

### 📥 **Export Options**
- Export filtered results to JSON
- Generate audit documentation
- API access (coming soon)

### 🎯 **Cross-Mappings**
Every control shows which requirements in other standards it maps to, making it easy to:
- Satisfy multiple compliance requirements with one implementation
- Understand equivalent controls across frameworks
- Build comprehensive security programs

### 💡 **Implementation Guidance**
Each control includes:
- Clear description of the requirement
- Cross-standard mappings
- Actionable implementation recommendations
- References to tools and libraries

---

## 📖 Documentation

### Understanding the Mappings

ComplianceCompass uses expert analysis to map controls across standards. For example:

**OWASP C1: Define Security Requirements** maps to:
- ISO27001: A.14.1.1 (Information Security Requirements Analysis)
- NIST SSDF: PO.1.1 (Define Security Requirements)

This means if you implement OWASP C1 properly, you're simultaneously addressing requirements in ISO27001 and NIST SSDF.

### Data Structure

```json
{
  "id": "OWASP-C1",
  "standard": "OWASP",
  "category": "Security Architecture",
  "title": "Define Security Requirements",
  "description": "Security requirements provide a foundation...",
  "mappings": {
    "iso27001": ["A.14.1.1", "A.14.2.1"],
    "nist": ["PO.1.1", "PO.1.2", "PO.3.1"]
  },
  "recommendation": "Leverage security frameworks like OWASP ASVS..."
}
```

### API Usage (Coming Soon)

```python
# Python
from compliance_compass import get_control, search_controls

# Get specific control
control = get_control("OWASP-C1")

# Search controls
results = search_controls(query="authentication", standard="ISO27001")
```

```javascript
// JavaScript
import { getControl, searchControls } from 'compliance-compass';

// Get specific control
const control = await getControl('OWASP-C1');

// Search controls
const results = await searchControls({ 
  query: 'authentication', 
  standard: 'ISO27001' 
});
```

---

## 🛠️ Use Cases

### For Security Teams
- **Audit preparation**: Generate cross-framework compliance documentation
- **Gap analysis**: Identify which controls you're missing
- **Strategy planning**: Understand which implementations satisfy multiple requirements

### For Developers
- **Requirement clarity**: See exactly what security controls to implement
- **Framework guidance**: Get actionable recommendations for each control
- **Efficiency**: Satisfy multiple compliance requirements with single implementations

### For Auditors
- **Control verification**: Map client implementations to multiple frameworks
- **Documentation**: Export mappings for audit reports
- **Efficiency**: Quickly understand cross-standard coverage

### For Consultants
- **Client education**: Show clients how their security program maps to standards
- **Proposal development**: Demonstrate comprehensive compliance approach
- **Multi-client tracking**: Manage compliance across different frameworks

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Adding New Standards
Have expertise in PCI-DSS, HIPAA, or other frameworks? Help us add them!

1. Fork the repository
2. Add standard data following our schema
3. Update mappings with the new standard
4. Submit a pull request

### Improving Mappings
Found a better way to map controls? 

1. Open an issue explaining your reasoning
2. Reference official documentation
3. Discuss with the community
4. Submit a PR with updates

### Reporting Issues
Found incorrect mappings or bugs?

- **[Report an issue](https://github.com/SecuardenAI/compliance-compass/issues/new)**
- Include: What's wrong, what it should be, your evidence

See our [Contributing Guide](CONTRIBUTING.md) for more details.

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Data Attribution

Compliance framework data is sourced from:
- **OWASP**: [Proactive Controls](https://owasp.org/www-project-proactive-controls/)
- **ISO**: ISO/IEC 27001:2013 (publicly available control descriptions)
- **NIST**: [SP 800-218](https://csrc.nist.gov/publications/detail/sp/800-218/final)

Mappings are interpretive and based on expert analysis. They should be verified for your specific use case.

---

## 🌟 Built By

**ComplianceCompass** is built and maintained by [Secuarden](https://secuarden.com) — Product Security Intelligence That Auditors Actually Accept.

We built this because we were frustrated by the lack of clear guidance on what to implement for compliance. We hope it helps you navigate the complexity.

### Why We Built This

At Secuarden, we analyze application security at scale. We saw teams struggling to:
- Understand what controls they needed across different frameworks
- Map their security implementations to audit requirements
- Communicate their security posture in compliance-speak

ComplianceCompass is our contribution to making compliance clearer for everyone.

---

## 🔗 Related Projects

- **[Secuarden](https://secuarden.com)** - Context-aware security intelligence platform
- **[OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/)** - Application Security Verification Standard
- **[OpenCRE](https://www.opencre.org/)** - Common Requirement Enumeration

---

## 📣 Spread the Word

If ComplianceCompass helped you, please:
- ⭐ Star this repository
- 🐦 [Share on Twitter](https://twitter.com/intent/tweet?text=Check%20out%20ComplianceCompass%20-%20an%20open-source%20tool%20to%20navigate%20AppSec%20compliance%20across%20OWASP,%20ISO27001,%20and%20NIST!%20https://github.com/SecuardenAI/compliance-compass)
- 💼 [Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https://github.com/SecuardenAI/compliance-compass)
- 📝 Write a blog post about how you're using it

---

## 💬 Support

- 📖 [Documentation](https://secuardenai.github.io/compliance-compass)
- 💬 [GitHub Discussions](https://github.com/SecuardenAI/compliance-compass/discussions)
- 🐛 [Issue Tracker](https://github.com/SecuardenAI/compliance-compass/issues)
- 📧 Email: support@secuarden.com

---

<p align="center">
  Made with ❤️ by the <a href="https://secuarden.com">Secuarden</a> team
  <br>
  <sub>Helping security teams navigate compliance with confidence</sub>
</p>
