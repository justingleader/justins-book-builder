# Stack Intelligence Template Snippets

This document provides ready-to-use snippets for common content blocks in Stack Intelligence documents. Copy and paste these snippets into your Quarto documents and customize them to fit your needs.

## Available Snippets

### Featured Quote

```qmd
{{{< featured-quote color="primaryorange" size="normal" >}}
This is an impactful quote that captures the essence of your message.

Author Name, Position at Company
{{{< /featured-quote >}}
```

### Case Study

```qmd
{{{< case-study company="ACME Corporation" segment="Technology" revenue="$250M" challenge="Scaling cloud infrastructure" outcome="30% cost reduction" >}}
ACME Corporation faced significant challenges with their legacy infrastructure. After implementing our solution, they were able to achieve substantial cost savings while improving performance.

> The transformation was remarkable. We never expected to see such immediate results.
> 
> — Jane Smith, CTO at ACME Corporation
{{{< /case-study >}}
```

### Listicle

```qmd
{{{< listicle title="Key Strategic Recommendations" style="numbered" >}}
1. Implement data-driven decision making across all departments
2. Develop a comprehensive cloud migration strategy
3. Establish clear KPIs for measuring digital transformation success
4. Create cross-functional teams to drive innovation
5. Invest in employee training for new technologies
{{{< /listicle >}}
```

### Figure

```qmd
{{{< figure src="images/chart.png" caption="Figure 1: Annual Growth Comparison" description="Comparison of annual growth rates between industry segments" credit="Stack Intelligence Research, 2023" width="90%" >}}
```

### Code Block

```qmd
{{{< code-block title="Sample API Integration" language="python" >}}
import requests

def get_data(api_key, endpoint):
    """Retrieve data from the API endpoint."""
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()
{{{< /code-block >}}
```

### Executive Action Plan

```qmd
{{{< action-plan title="90-Day Executive Action Plan" >}}
1. **Immediate (Days 1-30)**: Conduct stakeholder interviews and data assessment
2. **Short-term (Days 31-60)**: Develop strategic roadmap based on findings
3. **Medium-term (Days 61-90)**: Begin implementation of priority initiatives
   - Deploy pilot program in key department
   - Establish metrics dashboard
   - Train team leads on new processes
{{{< /action-plan >}}
```

### Statistics Highlight

```qmd
{{{< stats-highlight title="Industry Benchmarks" >}}
- **Average ROI**: 127% for companies implementing AI solutions
- **Implementation Time**: 4.3 months (median)
- **Cost Reduction**: 23% average across surveyed organizations
- **Productivity Gain**: 31% improvement in process efficiency
{{{< /stats-highlight >}}
```

### Quick Tips

```qmd
{{{< quick-tips title="Implementation Best Practices" >}}
- Start with a comprehensive audit of existing systems
- Engage stakeholders early and maintain regular communication
- Implement changes incrementally rather than all at once
- Document processes thoroughly for future reference
- Schedule regular review points to assess progress
{{{< /quick-tips >}}
```

### Executive Summary Template

See the `executive-summary.qmd` snippet file for a complete executive summary template.

## Using Snippets

1. Copy the desired snippet from this guide or from the individual snippet files in the `snippets` directory
2. Paste the snippet into your Quarto document
3. Customize the content and parameters to match your specific needs
4. Render your document to see the professionally styled output

## Template Validation

The Stack Intelligence templates include a validation system that checks your document for compliance with template guidelines. To use validation:

1. Include the template type in your document's YAML frontmatter:

```yaml
---
title: "My Document"
template_type: "executive_brief"
---
```

2. Valid template types include:
   - `executive_brief`
   - `whitepaper`
   - `case_study`
   - `ebook`

3. When rendering your document, the validation system will check for:
   - Required sections for your chosen template type
   - Recommended sections (optional but suggested)
   - Document length guidelines
   - Template-specific requirements

4. Any validation errors or warnings will be displayed during the rendering process.

## Additional Resources

For more detailed information, refer to:

- The full shortcode reference document (`shortcode-reference.qmd`)
- Stack Intelligence style guide (`stack_intelligence_style_guide.md`)
- Template-specific guidelines in the documentation directory