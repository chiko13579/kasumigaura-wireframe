import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'raw.html' and f != 'header_template.html' and f != 'index.html']

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract the <title> tag content
    title_match = re.search(r'<title>(.*?)</title>', content)
    if not title_match:
        continue
        
    page_title = title_match.group(1).split(' - ')[0].strip()
    
    # Find the H1 inside the main-header or generally right above the main-hero-placeholder
    # The header sync might have made it:
    # <div class="container" style="padding-top: 0;">
    #     <h1>霞ヶ浦高等学校</h1>
    #     <div class="main-hero-placeholder">ここに写真を入れるイメージ</div>
    # </div>
    
    content = re.sub(
        r'(<div class="container" style="padding-top: 0;">\s*)<h1>[^<]*</h1>',
        r'\1<h1>' + page_title + r'</h1>',
        content,
        count=1
    )
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("H1 titles updated.")
