import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'raw.html']

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # Remove search box and "資料請求・お問い合わせ"
    old_btn = r'<div class="top-search">\s*<span class="search-icon">🔍</span>\s*<input type="text" placeholder="検索" readonly>\s*</div>\s*<a href="contact.html" class="top-contact-btn">資料請求・お問い合わせ</a>'
    new_btn = '<a href="contact.html" class="top-contact-btn">お問合せ</a>'
    
    c = re.sub(old_btn, new_btn, c)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(c)

print("Removed search box and updated contact button text in all HTML files.")
