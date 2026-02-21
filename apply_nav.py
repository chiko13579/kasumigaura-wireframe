import glob
import re

def update_global_nav():
    # Read the updated master nav from index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        index_content = f.read()
    
    # Extract the <nav class="main-nav"> block from index.html
    nav_match = re.search(r'<nav class="main-nav">.*?</nav>', index_content, re.DOTALL)
    if not nav_match:
        print("Could not find main-nav in index.html")
        return
        
    master_nav = nav_match.group(0)
    
    # Remove the "主な戦績" link
    master_nav = re.sub(r'<a href="club\.html#records">主な戦績</a>\s*', '', master_nav)
    
    # Write it back to index.html
    new_index_content = index_content[:nav_match.start()] + master_nav + index_content[nav_match.end():]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_index_content)
        
    # Apply to all other html files
    for filepath in glob.glob('*.html'):
        if filepath == 'index.html':
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if '<nav class="main-nav">' in content:
            # We need to correctly handle the "active" button state for the current page
            # 1. Inject the master nav
            new_content = re.sub(r'<nav class="main-nav">.*?</nav>', master_nav, content, flags=re.DOTALL)
            
            # 2. Fix the active state
            # Remove active class from index.html link
            new_content = new_content.replace('<button class="active">トップ</button>', '<button>トップ</button>')
            
            # Add active class to the current page's button
            # We can map filenames to button texts
            page_to_button = {
                'news.html': 'お知らせ',
                'admission.html': '受験生案内',
                'course.html': 'コース紹介',
                'about.html': '学校紹介',
                'school_life.html': '学校生活',
                'career.html': '進路指導',
                'club.html': '部活動',
                'interview.html': '卒業生の声',
                'recruit.html': '教員採用',
                # skip abstract ones like message.html if they don't have a button
            }
            
            if filepath in page_to_button:
                btn_text = page_to_button[filepath]
                # In the nav, it looks like: <button>受験生案内 <span
                # or just <button>お知らせ</button>
                
                # Careful regex to find the button for this page and add class="active"
                def repl_active(m):
                    return m.group(1) + ' class="active"' + m.group(2)
                    
                # Match <button>Text...
                new_content = re.sub(f'(<button)(>{btn_text})', repl_active, new_content)
                
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
                
    print("Nav applied to all pages successfully")

if __name__ == '__main__':
    update_global_nav()
