import os

def generate_summary():
    return """
AI SEO Insight Report
By Shivendra Singh

Summary:
Some keywords have high impressions but low CTR.

Recommendations:
1. Improve titles and meta descriptions
2. Focus on high performing keywords
3. Optimize thumbnails
"""

os.makedirs("reports", exist_ok=True)

with open("reports/insight_report.md", "w") as f:
    f.write(generate_summary())

print("Report generated")