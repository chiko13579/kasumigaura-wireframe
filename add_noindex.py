import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

meta_noindex = '    <meta name="robots" content="noindex, nofollow">\n'

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already has noindex
    if 'name="robots" content="noindex' in content:
        continue
        
    # Inject right after <head> or <meta charset="UTF-8">
    content = re.sub(
        r'(<meta charset="UTF-8">)',
        r'\1\n' + meta_noindex,
        content,
        count=1
    )
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Added noindex to all HTML files.")
