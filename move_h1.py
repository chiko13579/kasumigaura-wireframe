import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'raw.html']
count = 0

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the H1 inside main-header
    # It looks like:
    # <div class="main-header">... <nav>...</nav> ... <h1>TITLE</h1> ... </div>
    # Then <div class="container" style="padding-top: 0;">
    #   <div class="main-hero-placeholder">...
    
    # We will find the <h1> tag
    h1_match = re.search(r'(<h1[^>]*>.*?</h1>)', content, re.DOTALL)
    if not h1_match:
        print(f"Skipping {filename}: no H1 found")
        continue
    h1_tag = h1_match.group(1)
    
    # Remove H1 from its current position
    content_without_h1 = content[:h1_match.start()] + content[h1_match.end():]
    
    # Now find the place to insert it: just before the main visual or the sub-nav if there's no visual.
    # The structure below main-header is typically:
    # <div class="container" style="padding-top: 0;">
    #     <div class="main-hero-placeholder">
    # OR <img src="img/facility.jpg" ...>
    
    # Let's look for `<div class="container" style="padding-top: 0;">`
    # and insert the h1 just inside it.
    
    insert_pattern = r'(<div class="container" style="padding-top: 0;">\s*)'
    insert_match = re.search(insert_pattern, content_without_h1)
    
    if insert_match:
        new_content = content_without_h1[:insert_match.end()] + h1_tag + '\n            ' + content_without_h1[insert_match.end():]
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f"Updated {filename}")
    else:
        print(f"Could not find lower container in {filename}")

print(f"Total files updated: {count}")
