AI Automation Course Project — CI/CD for Hugging Face Space

🔧 Title: “Auto-Deploy a Python App with GitHub Actions”
📚 Learning Objectives (for students)
By the end of this project, students will:

Understand CI/CD fundamentals (Continuous Integration & Deployment)
Use GitHub Actions to automate testing & deployment
Learn to deploy a simple Python AI/ML app on Hugging Face Spaces
Explore how teams work together using branching & pipelines

🏗️ Project Setup
Students will:
Clone a pre-made repo (or write a basic Python app with a requirements.txt)
Add app.py
Push to GitHub

Set up two workflows:
build-and-test.yaml
deploy.yaml

🔐 Add Hugging Face Token
Go to Hugging Face > Settings > Access Tokens
Generate token with Write permission
On GitHub, go to repo Settings > Secrets > Actions
Add secret: HF_TOKEN
