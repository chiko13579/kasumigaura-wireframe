import os
import re

# Read index.html nav
with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

nav_match = re.search(r'(<nav class="main-nav">.*?</nav>)', idx_content, re.DOTALL)
if not nav_match:
    print("Could not find nav in index.html")
    exit(1)

nav_idx = nav_match.group(1)

html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html' and f != 'raw.html']

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the nav in this file
    new_content = re.sub(r'<nav class="main-nav">.*?</nav>', nav_idx, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated nav in {filename}")

print("Sync complete.")
