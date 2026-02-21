import os
import re

def add_ids_to_h2():
    files = [
        'about.html',
        'admission.html',
        'career.html',
        'club.html',
        'course.html',
        'school_life.html'
    ]
    
    # Mapping of h2 text to id
    id_map = {
        '学校案内・データブック': 'guide',
        '出願': 'application',
        '入試関係書類': 'documents',
        '2025年度　個別相談会日程': 'consultation',
        'よくあるご質問': 'faq',
        '特進選抜': 'tokushin_senbatsu',
        '特進': 'tokushin',
        '総合進学': 'sogo',
        '学習センター': 'learning_center',
        '校長・沿革': 'history',
        'Annual Events <年間行事>': 'annual_events',
        'School Uniform <制服紹介>': 'uniform',
        'いじめ防止基本方針': 'anti_bullying',
        '不登校未然防止の基本方針': 'anti_truancy',
        'キャリアを拓く3年間': 'career_path',
        '最近５年間の合格大学（浪人含む）': 'results',
        '卒業生の声': 'interview',
        '運動部': 'sports',
        '文化部': 'culture',
        '主な戦績': 'records',
        'レスリング部': 'wrestling',
        '剣道部': 'kendo'
    }
    
    for filename in files:
        if not os.path.exists(filename):
            continue
            
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Very simple regex to inject id into h2 if it contains the text
        for text, dom_id in id_map.items():
            # If the text is in an h2
            pattern = re.compile(f'(<h2[^>]*?)(>\\s*{re.escape(text)}\\s*</h2>)', re.IGNORECASE)
            
            def repl(m):
                # If there's already an id, let's just rely on that or add a data-id
                if 'id=' in m.group(1):
                    # just replace the existing id
                    return re.sub(r'id="[^"]+"', f'id="{dom_id}"', m.group(1)) + m.group(2)
                else:
                    return m.group(1) + f' id="{dom_id}"' + m.group(2)
            
            content = pattern.sub(repl, content)
            
            # Additional fallback for complex inner HTML like in admission.html
            pattern2 = re.compile(f'(<h2[^>]*?>\\s*<span[^>]*?>\\s*{re.escape(text)}\\s*</span>\\s*</h2>)', re.IGNORECASE)
            def repl2(m):
                return m.group(1).replace('<h2', f'<h2 id="{dom_id}"')
            if 'id=' not in content and text in content:
                 content = pattern2.sub(repl2, content)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

if __name__ == '__main__':
    add_ids_to_h2()

