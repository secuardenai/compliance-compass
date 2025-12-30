# Contributing to ComplianceCompass

Thank you for your interest in contributing to ComplianceCompass! This document provides guidelines and instructions for contributing.

## 🎯 How Can I Contribute?

### 1. Adding New Standards

Want to add PCI-DSS, HIPAA, SOC 2, or other frameworks?

**Steps:**
1. Fork the repository
2. Create a new branch: `git checkout -b add-pci-dss-standard`
3. Add data following our schema in `app.js` or create a new data file
4. Update cross-mappings with existing standards
5. Update the README to include the new standard
6. Submit a pull request with clear documentation

**Data Format:**
```javascript
{
    id: "PCI-6.5.1",  // Unique identifier
    standard: "PCI-DSS",  // Standard name
    category: "Secure Coding",  // Category
    title: "Injection Flaws",  // Control title
    description: "Train developers in secure coding...",  // Description
    mappings: {  // Cross-standard mappings
        owasp: ["C5"],
        iso27001: ["A.14.2.1"],
        nist: ["PW.1.1"]
    },
    recommendation: "Implement input validation..." // Implementation guidance
}
```

### 2. Improving Existing Mappings

Found a better way to map controls across standards?

**Steps:**
1. Open an issue first to discuss your proposed changes
2. Provide evidence from official documentation
3. Explain your reasoning
4. Get community feedback
5. Submit a PR with the updated mappings

**Evidence Requirements:**
- Link to official standard documentation
- Quote relevant sections
- Explain the mapping logic
- Consider edge cases

### 3. Reporting Issues

#### Bug Reports

**Before submitting:**
- Search existing issues to avoid duplicates
- Check if it's actually a bug vs. intended behavior

**Include:**
- Browser and version
- Steps to reproduce
- Expected vs. actual behavior
- Screenshots if applicable

#### Incorrect Mappings

**Include:**
- Control IDs involved
- Why the current mapping is incorrect
- What it should be instead
- Supporting documentation/evidence

### 4. Feature Requests

**Before submitting:**
- Check if the feature already exists
- Search existing feature requests

**Include:**
- Clear description of the feature
- Use case / problem it solves
- Proposed implementation (if you have ideas)
- Mockups or examples (if applicable)

## 📝 Development Guidelines

### Code Style

**JavaScript:**
- Use ES6+ features
- Meaningful variable names
- Comment complex logic
- Follow existing patterns in `app.js`

**HTML/CSS:**
- Semantic HTML
- Maintain existing design system
- Mobile-responsive
- Accessibility considerations

### Commit Messages

Use clear, descriptive commit messages:

```
Add: PCI-DSS Requirement 6.5 mappings
Fix: Incorrect OWASP C1 to ISO27001 mapping
Update: README with Python package installation
Docs: Add API usage examples
```

### Pull Request Process

1. **Update documentation** - Ensure README and other docs reflect your changes
2. **Test thoroughly** - Verify functionality across browsers
3. **Keep PRs focused** - One feature/fix per PR
4. **Describe changes** - Clear description of what and why
5. **Reference issues** - Link to related issues
6. **Be responsive** - Respond to review comments promptly

**PR Template:**
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] New standard addition
- [ ] Mapping improvement
- [ ] Bug fix
- [ ] Feature enhancement
- [ ] Documentation update

## Testing Done
- Tested in Chrome, Firefox, Safari
- Verified mappings against official docs
- Checked mobile responsiveness

## Evidence
- Link to standard documentation
- Screenshots (if UI change)

## Checklist
- [ ] Updated README.md
- [ ] Added/updated tests
- [ ] Verified all links work
- [ ] Follows existing code style
```

## 🔍 Review Process

1. **Automated checks** - Must pass (if we add CI/CD)
2. **Maintainer review** - At least one maintainer approval required
3. **Community feedback** - For significant changes, allow time for community input
4. **Documentation** - Must include relevant documentation updates

## 🎨 Design Guidelines

When contributing UI changes:

**Visual Consistency:**
- Use existing color scheme (CSS variables)
- Follow Secuarden brand colors
- Maintain dark theme aesthetic
- Keep animations smooth and purposeful

**Accessibility:**
- Maintain WCAG 2.1 AA compliance
- Keyboard navigation support
- Screen reader compatibility
- Sufficient color contrast

## 📚 Documentation

All significant changes should include documentation updates:

- **README.md** - For user-facing features
- **API.md** - For API changes (when we add API)
- **Code comments** - For complex logic
- **Examples** - Show how to use new features

## 🤝 Code of Conduct

### Our Standards

**Be respectful:**
- Use welcoming and inclusive language
- Respect differing viewpoints and experiences
- Accept constructive criticism gracefully
- Focus on what's best for the community

**Be constructive:**
- Provide helpful feedback
- Assume good intentions
- Help newcomers
- Share knowledge

**Be professional:**
- Stay on topic
- No harassment or discrimination
- No spam or self-promotion
- Respect maintainer decisions

### Enforcement

Instances of unacceptable behavior may result in:
1. Warning
2. Temporary ban
3. Permanent ban

Report issues to: support@secuarden.com

## 🏆 Recognition

Contributors will be:
- Listed in README.md
- Mentioned in release notes
- Invited to join our Slack community
- Given credit in presentations/blog posts

## 📧 Questions?

Not sure about something? Ask!

- Open a discussion on GitHub
- Email us: support@secuarden.com
- Tag @secuarden on Twitter

## 🙏 Thank You!

Every contribution, no matter how small, helps make compliance clearer for security teams worldwide. We appreciate your time and expertise!

---

<p align="center">
  Built with ❤️ by the <a href="https://secuarden.com">Secuarden</a> community
</p>
