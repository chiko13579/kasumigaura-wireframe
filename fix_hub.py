import re

hub_files = {
    'hub_admission.html': '受験生の方へ',
    'hub_parents.html': '在校生・保護者の方へ',
    'hub_alumni.html': '卒業生の方へ'
}

for filepath, target_title in hub_files.items():
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content.replace('<h1>霞ヶ浦高等学校</h1>', f'<h1>{target_title}</h1>')
    
    # Also remove the hero placeholder on these hub pages if they exist under the H1
    new_content = re.sub(
        r'(<h1>.*?</h1>\s*)<div class="main-hero-placeholder">ここに写真を入れるイメージ</div>',
        r'\1',
        new_content
    )
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated H1 and placeholder in {filepath} to '{target_title}'")
