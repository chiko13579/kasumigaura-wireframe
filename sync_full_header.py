import os
import re

with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

# Capture from <div class="top-header"> down to the end of </nav> and the closing divs
nav_match = re.search(r'(<div class="top-header">.*?</nav>\s*</div>\s*</div>)', idx_content, re.DOTALL)
if not nav_match:
    print("Could not find nav in index.html")
    exit(1)

nav_idx = nav_match.group(1)

html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html' and f != 'raw.html']

count = 0
for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the matching section in the target file
    new_content = re.sub(
        r'<div class="top-header">.*?</nav>\s*</div>\s*</div>',
        lambda m: nav_idx,
        content,
        flags=re.DOTALL
    )
    
    if new_content != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f"Updated nav in {filename}")

print(f"Sync complete. Updated {count} files.")
