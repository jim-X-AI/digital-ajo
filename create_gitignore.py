def create_gitignore():
    gitignore_content = """# Node.js/React
node_modules/
build/
dist/
.env
.env.local
.env.development.local
.env.test.local
.env.production.local
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
.pnp.*
.cache/
.parcel-cache
.next/
out/
.coverage
.nyc_output

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST
.python-version
.pytest_cache/
.venv/
venv/

# IDE
.vscode/
.idea/
*.suo
*.ntvs*
*.njsproj
*.sln
*.sw?

# System
.DS_Store
Thumbs.db
*.swp
*.swo

# Testing
/jest_results/
/cypress/screenshots/
/cypress/videos/
/test-results/

# Debug
debug.log
*.log

# Environment files
*.env
*.bak
*.tmp
*.temp

# Build files
*.css.map
*.js.map
*.sass.map
*.scss.map
*.less.map
*.styl.map

# Local development
*.local
"""

    with open(".gitignore", "w", encoding="utf-8") as f:
        f.write(gitignore_content)
    print(".gitignore file created successfully in project root directory")


if __name__ == "__main__":
    create_gitignore()