import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'raw.html']

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        c = f.read()

    title_match = re.search(r'<title>(.*?)</title>', c)
    if not title_match:
        continue
    
    full_title = title_match.group(1)
    page_title = full_title.split(' - ')[0]
    
    # We want to replace <h1>霞ヶ浦高等学校</h1> inside <div class="container" style="padding-top: 0;">
    # with <h1>{page_title}</h1>
    
    pattern = r'(<div class="container" style="padding-top: 0;">\s*)<h1>霞ヶ浦高等学校</h1>'
    new_c = re.sub(pattern, r'\g<1><h1>' + page_title + r'</h1>', c)
    
    if new_c != c:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_c)
        print(f"Fixed h1 in {filename}")

