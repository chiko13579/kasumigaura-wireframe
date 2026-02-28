import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'raw.html']
count = 0

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # Replace the links
    new_c = c.replace('<a href="#">受験生の方へ</a>', '<a href="hub_admission.html">受験生の方へ</a>')
    new_c = new_c.replace('<a href="#">在校生・保護者の方へ</a>', '<a href="hub_parents.html">在校生・保護者の方へ</a>')
    new_c = new_c.replace('<a href="#">卒業生の方へ</a>', '<a href="hub_alumni.html">卒業生の方へ</a>')
    
    if new_c != c:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_c)
        count += 1
        print(f"Updated links in {filename}")

print(f"Total files updated: {count}")
