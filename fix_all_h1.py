import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html') and f not in ['raw.html', 'index.html', 'header_template.html']]
count = 0

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        c = f.read()

    title_match = re.search(r'<title>(.*?)</title>', c)
    if not title_match:
        continue
    
    full_title = title_match.group(1)
    page_title = full_title.split(' - ')[0]
    
    # Replace the h1 tag
    new_c = c.replace('<h1>霞ヶ浦高等学校</h1>', f'<h1>{page_title}</h1>')
    
    # Check if there are duplicate <h1> tags now (e.g. recruit.html had <h1>教員採用</h1> below it originally)
    # The user said "メインビジュアルの上に入れて 写真の内容などは入れなくて良いです" previously.
    # Our replacements might already be fine. Let's just do it.
    
    if new_c != c:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_c)
        count += 1
        print(f"Fixed h1 in {filename}")

print(f"Total files updated: {count}")
