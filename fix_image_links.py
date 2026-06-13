with open("index.html", "r") as f:
    html = f.read()

# Fix the portfolio image references
replacements = {
    "images/portfolio/01-saas.jpg": "images/portfolio/project-saas-rollout.jpg",
    "images/portfolio/02-docs.jpg": "images/portfolio/project-knowledge-base.jpg",
    "images/portfolio/03-analytics.jpg": "images/portfolio/project-adoption-feedback.jpg",
    "images/portfolio/04-product.jpg": "images/portfolio/project-ai-workflows.jpg",
    "images/portfolio/05-training.jpg": "images/portfolio/project-flashcard-app.jpg",
    "images/portfolio/06-community.jpg": "images/portfolio/project-community-ops.jpg"
}

for old, new in replacements.items():
    html = html.replace(old, new)

with open("index.html", "w") as f:
    f.write(html)

print("Fixed image links.")
