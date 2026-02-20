import os
import glob
import re

dir_path = "/Users/saeki/Downloads/img/ワイヤーフレーム_デザイン/implementation/"
html_files = glob.glob(os.path.join(dir_path, "*.html"))

new_nav_item = '                <a href="admission.html"><button>受験生案内</button></a>'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Avoid duplicate addition
    if 'href="admission.html"' not in content:
        # Add after "news.html" link or "index.html" link
        if 'href="news.html"' in content:
            content = re.sub(
                r'(<a href="news\.html"><button[^>]*>お知らせ</button></a>)',
                r'\1\n' + new_nav_item,
                content
            )
        else:
            content = re.sub(
                r'(<a href="index\.html"><button[^>]*>トップ</button></a>)',
                r'\1\n' + new_nav_item,
                content
            )

        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print("Nav updated in all files")
