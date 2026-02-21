import re

with open('raw.html', 'r', encoding='utf-8') as f:
    raw_content = f.read()

# 1. Extract CSS
css_start = raw_content.find('<style id="sccss">')
if css_start != -1:
    css_start += len('<style id="sccss">')
    css_end = raw_content.find('</style>', css_start)
    css_text = raw_content[css_start:css_end]
    
    with open('style.css', 'a', encoding='utf-8') as f:
        f.write("\n/* Extracted from Kasumigaura live site */\n" + css_text + "\n")
    print("Injected CSS")

# 2. Extract HTML content
html_start_str = '<div class="entry-content cf" itemprop="mainEntityOfPage">'
html_end_str = '<footer class="article-footer entry-footer">'

h_start = raw_content.find(html_start_str)
if h_start != -1:
    h_start += len(html_start_str)
    h_end = raw_content.find(html_end_str, h_start)
    if h_end != -1:
        extracted_html = raw_content[h_start:h_end]
        extracted_html = extracted_html.replace('src="https://www.kasumi.ed.jp/wp-content/', 'src="https://www.kasumi.ed.jp/wp-content/')
        
        # We also need to add a wrapper so the custom CSS styles apply nicely
        # The live site uses h2#danraku2, dl.qa, etc.
        
        # 3. Inject into admission.html
        with open('admission.html', 'r', encoding='utf-8') as f:
            admin_content = f.read()
            
        # Replace what's inside <main class="container"> ... </main>
        pattern = re.compile(r'(<main class="container">).*?(</main>)', re.DOTALL)
        
        # Give it an extra class to scope any potential generic rules, or just use content-block
        new_main = r'\1' + '\n<div class="kasumi-live-content" style="padding: 20px; text-align: left;">\n' + extracted_html + '\n</div>\n' + r'\2'
        
        admin_content = pattern.sub(new_main, admin_content)
        
        with open('admission.html', 'w', encoding='utf-8') as f:
            f.write(admin_content)
        print("Injected HTML")
    else:
        print("Could not find end of html")
else:
    print("Could not find start of html")
