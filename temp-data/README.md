# Application Security Related Actions in Common Security Standards

Multiple industry standards in cybersecurity guide how to build and run security programs. A tiny portion of these standards (other than OWASP) is mapped to application security. It isn't easy to understand what needs to be done to be **compliant** with a particular standard's asks.

Having lived through this confusion in our professional careers, we have been building a mapping between **application security** requirements for various standards so that teams can know how a particular security measure maps to requirements in multiple standards.

This repository currently covers the following three standards:
1. OWASP Proactive Security Controls
2. ISO27001:2013
3. NIST SSDF

Each CSVs include the following information:
1. Specific controls within the standard that map to application security (directly or indirectly)

2. How each controls maps to the other two.

3. Recommendations/information on what can be done to implement that control.

## Example 
![record example](/images/csv-record-example.png "CSV record example")

A simple utility service is hosted on our website ([here](https://www.appsec360.com/security-requirement-wizard/)) to play around with various combinations.

**Note:**
1. All this information is available on the web. The only thing we did is to do the mapping based on our analysis of the standards. We found it useful to have this mapping handy to us during our professional careers in application security. Hopefully few other will find this useful too.
Create a PR if you want to suggest any changes.

