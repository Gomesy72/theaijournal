#!/usr/bin/env python3
"""
The AI Journal - Daily Automation Pipeline
Generates AI news articles automatically using subagents
"""

import os
import sys
import json
import subprocess
import datetime
import random
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

# Configuration
CONFIG = {
    "categories": [
        "ai-news",
        "robotics",
        "medicine",
        "jobs",
        "ubi"
    ],
    "sources": [
        "TechCrunch",
        "Ars Technica",
        "MIT Technology Review",
        "Nature AI",
        "Wired",
        "The Verge",
        "IEEE Spectrum",
        "VentureBeat"
    ],
    "output_dir": "articles",
    "max_articles_per_day": 3,
    "min_word_count": 1500,
    "style": "journalistic",
    "tone": "informative",
    "target_audience": "tech-savvy professionals and policymakers"
}

def log(message):
    """Log with timestamp"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

def generate_article_topic():
    """Generate a trending AI topic for today's article"""
    
    topics = [
        {
            "category": "ai-news",
            "title": "GPT-5 Multimodal Breakthrough: What It Means for Developers",
            "angle": "Technical analysis of new capabilities"
        },
        {
            "category": "ai-news",
            "title": "EU AI Act 2.0: New Compliance Requirements for Foundation Models",
            "angle": "Regulatory impact analysis"
        },
        {
            "category": "robotics",
            "title": "Boston Dynamics Atlas 2.0: Humanoid Robots Enter Home Service Market",
            "angle": "Market disruption analysis"
        },
        {
            "category": "medicine",
            "title": "AI-Designed Drug Shows Promise in Phase 2 Alzheimer's Trial",
            "angle": "Clinical trial results analysis"
        },
        {
            "category": "jobs",
            "title": "12 Million Jobs Lost to AI in 2025: Sector-by-Sector Breakdown",
            "angle": "Economic impact assessment"
        },
        {
            "category": "ubi",
            "title": "Finland's UBI Experiment: 5-Year Results Show Surprising Outcomes",
            "angle": "Policy effectiveness analysis"
        }
    ]
    
    return random.choice(topics)

def write_article_file(article_data, date_str):
    """Write article to HTML file"""
    
    # Generate filename
    slug = article_data["title"].lower().replace(" ", "-").replace(":", "").replace("?", "")[:50]
    filename = f"{article_data['category']}-{slug}-{date_str}.html"
    filepath = os.path.join(CONFIG["output_dir"], filename)
    
    # Create HTML template
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{article_data['title']} | The AI Journal</title>
    <link rel="stylesheet" href="../styles.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body>

    <div class="noise-overlay"></div>

    <header class="masthead">
        <div class="container">
            <div class="masthead-inner">
                <div class="masthead-left">
                    <span class="masthead-date">{date_str}</span>
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
            <span class="article-tag">{article_data['category'].upper()}</span>
            <h1 class="article-title">{article_data['title']}</h1>
            <div class="article-meta">
                <span>{date_str}</span>
                <span>10 min read</span>
                <span>{article_data['angle']}</span>
            </div>
        </div>
        
        <div class="article-content">
            <article class="article-body">
                <p><em>Article content generated by AI research agent...</em></p>
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
</html>"""
    
    # Write file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    
    log(f"Created article: {filepath}")
    return filepath

def update_homepage(article_files, date_str):
    """Update homepage with new articles"""
    log("Updating homepage...")
    # This would modify index.html to include new articles
    pass

def main():
    """Main pipeline function"""
    log("Starting The AI Journal daily pipeline...")
    
    # Get current date
    today = datetime.datetime.now()
    date_str = today.strftime("%Y%m%d")
    
    log(f"Date: {today.strftime('%Y-%m-%d')}")
    
    # Generate topics for today
    num_articles = min(CONFIG["max_articles_per_day"], len(CONFIG["categories"]))
    selected_topics = random.sample(CONFIG["categories"], num_articles)
    
    log(f"Selected categories: {', '.join(selected_topics)}")
    
    # Generate articles
    article_files = []
    for category in selected_topics:
        topic = generate_article_topic()
        if topic["category"] == category:
            filepath = write_article_file(topic, date_str)
            article_files.append(filepath)
    
    # Update homepage
    update_homepage(article_files, date_str)
    
    log(f"Pipeline complete! Generated {len(article_files)} articles.")
    
    return article_files

if __name__ == "__main__":
    try:
        articles = main()
        log("Success!")
    except Exception as e:
        log(f"Error: {str(e)}")
        sys.exit(1)
