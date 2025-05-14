import os
from pathlib import Path

def prepare_netlify():
    # Create netlify.toml configuration file
    netlify_toml = """[build]
  command = "npm run build"
  publish = "build"
  functions = "functions"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200

[dev]
  framework = "create-react-app"
  targetPort = 3000
  autoLaunch = false
"""
    with open("digital-ajo/netlify.toml", "w", encoding="utf-8") as f:
        f.write(netlify_toml)

    # Create build script in package.json if not exists
    package_json_path = "digital-ajo/package.json"
    if os.path.exists(package_json_path):
        with open(package_json_path, "r+", encoding="utf-8") as f:
            content = f.read()
            if '"build"' not in content:
                updated = content.replace('"scripts": {', '"scripts": {\n    "build": "react-scripts build",')
                f.seek(0)
                f.write(updated)
                f.truncate()

    print("Netlify configuration prepared successfully!")
    print("\nFollow these steps to deploy:")
    print("1. Push your code to GitHub")
    print("2. Go to Netlify.com and connect your GitHub repository")
    print("3. Select your digital-ajo project")
    print("4. Set the build command to 'npm run build'")
    print("5. Set publish directory to 'build'")
    print("6. Click 'Deploy site'")

if __name__ == "__main__":
    prepare_netlify()