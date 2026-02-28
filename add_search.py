import os, re

html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'raw.html']

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        c = f.read()
    
    new_btn = '''<div class="top-search">
                        <span class="search-icon">🔍</span>
                        <input type="text" placeholder="検索" readonly>
                    </div>
                    <a href="contact.html" class="top-contact-btn">資料請求・お問い合わせ</a>'''
    
    # Replace the old contact button
    c = re.sub(r'<a href="contact.html" class="top-contact-btn">お問合せ</a>', new_btn, c)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(c)

