import os
import glob
import re

# Mapping of file names to their correct H1 titles as seen in the navigation
page_titles = {
    'admission.html': '受験生案内',
    'course.html': 'コース紹介',
    'about.html': '学校紹介',
    'school_life.html': '学校生活',
    'career.html': '進路指導',
    #'club.html': '部活動(運動部)', # Skipped as it has a specific title that we just edited
    'news.html': 'お知らせ',
    'recruit.html': '教員採用情報',
    'interview.html': '卒業生の声',
    'contact.html': 'お問合せ',
    'contact_admission.html': 'お問合せ(受験生の方へ)',
    'contact_parents.html': 'お問合せ(在校生・保護者の方へ)',
    'contact_alumni.html': 'お問合せ(卒業生の方へ)',
    'interview_detail.html': '卒業生インタビュー詳細'
}

html_files = glob.glob('*.html')

for filepath in html_files:
    if filepath not in page_titles:
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the H1 right after the <div class="container" style="padding-top: 0;"> inside the header
    # and replace "霞ヶ浦高等学校" or whatever it is with the correct title.
    # Note: Using regex to replace the first <h1>...</h1> after <div class="container" style="padding-top: 0;">
    
    target_title = page_titles[filepath]
    
    # Let's replace <h1>霞ヶ浦高等学校</h1> with <h1>{target_title}</h1>
    # We will just replace it if it exists.
    new_content = content.replace('<h1>霞ヶ浦高等学校</h1>', f'<h1>{target_title}</h1>')
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated H1 in {filepath} to '{target_title}'")
    else:
        # Check if maybe it's not "霞ヶ浦高等学校" but something else, or already fixed
        match = re.search(r'<div class="container" style="padding-top: 0;">\s*<h1(.*?)>(.*?)</h1', content)
        if match:
            current_h1 = match.group(2)
            if current_h1 != target_title:
                new_content = re.sub(
                    r'(<div class="container" style="padding-top: 0;">\s*<h1.*?>).*?(</h1)',
                    fr'\1{target_title}\2',
                    content,
                    count=1
                )
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Regex Updated H1 in {filepath} from '{current_h1}' to '{target_title}'")

print("Finished changing H1 titles.")
