#!/usr/bin/env python3
"""
Convert standalone article HTML to The AI Journal template
"""

import sys
import re
from pathlib import Path

ARTICLE_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | The AI Journal</title>
    <link rel="stylesheet" href="../styles.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body>

    <div class="noise-overlay"></div>

    <header class="masthead">
        <div class="container">
            <div class="masthead-inner">
                <div class="masthead-left">
                    <span class="masthead-date">{date}</span>
                    <span class="masthead-issue">AI Daily Brief</span>
                </div>
                <div class="masthead-center">
                    <div class="masthead-logo">AIJ</div>
                    <h1 class="masthead-title">The AI Journal</h1>
                    <div class="masthead-tagline">AI-Curated News &middot; Human-Verified</div>
                </div>
                <div class="masthead-right">
                    <a href="../index.html#newsletter" class="btn-subscribe">Subscribe &rarr;</a>
                </div>
            </div>
        </div>
    </header>

    <nav class="site-nav">
        <div class="container">
            <div class="site-nav-inner">
                <a href="../index.html">Home</a>
                <a href="../index.html#ai-news">AI News</a>
                <a href="../index.html#robotics">Robotics</a>
                <a href="../index.html#medicine">Medicine</a>
                <a href="../index.html#jobs">Jobs</a>
                <a href="../index.html#ubi">UBI</a>
            </div>
        </div>
    </nav>

    <div class="article-page container">
        <a href="../index.html" class="back-link">&larr; Back to Latest Issue</a>
        
        <div class="article-header">
            <span class="article-tag">{category}</span>
            <h1 class="article-title">{title}</h1>
            <div class="article-meta">
                <span>{date}</span>
                <span>10 min read</span>
                <span>{angle}</span>
            </div>
        </div>
        
        <div class="article-content">
            <article class="article-body">
                {body}
            </article>
        </div>
    </div>

    <footer class="site-footer">
        <div class="container">
            <div class="footer-bottom">
                <p class="copyright">&copy; 2026 The AI Journal. All rights reserved.</p>
                <div class="footer-legal">
                    <a href="../privacy.html">Privacy Policy</a>
                    <a href="../terms.html">Terms of Service</a>
                </div>
            </div>
        </div>
    </footer>

</body>
</html>'''

def extract_content(html_file):
    """Extract title and body from standalone HTML article"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract title
    title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
    title = title_match.group(1) if title_match else "Untitled"
    # Clean up title - remove "- The AI Journal" suffix
    title = re.sub(r'\s*[-|]\s*The AI Journal$', '', title, flags=re.IGNORECASE)
    
    # Extract body content (between <body> and </body>)
    body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL | re.IGNORECASE)
    if body_match:
        body = body_match.group(1).strip()
        # Remove any inline style tags
        body = re.sub(r'<style>.*?</style>', '', body, flags=re.DOTALL | re.IGNORECASE)
        # Remove any script tags
        body = re.sub(r'<script>.*?</script>', '', body, flags=re.DOTALL | re.IGNORECASE)
    else:
        body = content
    
    return title, body

def convert_article(input_file, output_file, category="Research", angle="Analysis", date="June 2, 2026"):
    """Convert standalone article to AI Journal template"""
    
    # Extract content
    title, body = extract_content(input_file)
    
    # Create wrapped HTML
    html = ARTICLE_TEMPLATE.format(
        title=title,
        date=date,
        category=category.upper(),
        angle=angle,
        body=body
    )
    
    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"Converted: {input_file} -> {output_file}")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python convert_article.py <input_file> <output_file> [category] [angle]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    category = sys.argv[3] if len(sys.argv) > 3 else "Research"
    angle = sys.argv[4] if len(sys.argv) > 4 else "Analysis"
    
    convert_article(input_file, output_file, category, angle)
