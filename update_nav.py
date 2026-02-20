import os
import glob
import re

dir_path = "/Users/saeki/Downloads/img/ワイヤーフレーム_デザイン/implementation/"

html_files = glob.glob(os.path.join(dir_path, "*.html"))

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if 'お知らせ' is already there to avoid duplicates
    if 'href="news.html"' not in content:
        # We find: <a href="index.html"><button...>トップ</button></a>
        # and append <a href="news.html"><button>お知らせ</button></a>
        content = re.sub(
            r'(<a href="index\.html"><button[^>]*>トップ</button></a>)',
            r'\1\n                <a href="news.html"><button>お知らせ</button></a>',
            content
        )
    
    # Update teacher recruitment link
    content = re.sub(
        r'<a href="#"><button([^>]*)>教員採用</button></a>',
        r'<a href="recruit.html"><button\1>教員採用</button></a>',
        content
    )
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Nav updated in all files")
