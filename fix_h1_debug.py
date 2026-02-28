import re
with open('hub_admission.html', 'r', encoding='utf-8') as f:
    c = f.read()

pattern = r'(<div class="container" style="padding-top: 0;">\s*)<h1>霞ヶ浦高等学校</h1>'
print(bool(re.search(pattern, c)))
