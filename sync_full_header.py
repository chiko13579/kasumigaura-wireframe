import os
import re

with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

header_match = re.search(r'(<header>.*?</header>)', idx_content, re.DOTALL)
if not header_match:
    print("Could not find header in index.html")
    exit(1)

header_idx = header_match.group(1)

html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html' and f != 'raw.html']

count = 0
for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = re.sub(r'<header>.*?</header>', lambda m: header_idx, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f"Updated full header in {filename}")

print(f"Sync complete. Updated {count} files.")
