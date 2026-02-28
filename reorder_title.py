import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'raw.html']
count = 0

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find <h1>...</h1> followed by <nav class="main-nav">...</nav>
    pattern = r'(<h1[^>]*>.*?</h1>)(\s*)(<nav class="main-nav">.*?</nav>)'
    
    match = re.search(pattern, content, re.DOTALL)
    if match:
        # Swap them
        new_content = content[:match.start()] + match.group(3) + match.group(2) + match.group(1) + content[match.end():]
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f"Reordered {filename}")
    else:
        print(f"Pattern not found in {filename}")

print(f"Total files reordered: {count}")
