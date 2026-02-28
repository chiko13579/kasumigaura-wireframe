import os
import re

# Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Find the .image-placeholder block and ensure it has background-color: #eee;
# Currently it might have background-color: #fff; due to the previous flattening.
# Let's just explicitly replace it or add it.
image_placeholder_rule = re.search(r'\.image-placeholder\s*\{([^}]+)\}', css_content)
if image_placeholder_rule:
    inner_css = image_placeholder_rule.group(1)
    inner_css = re.sub(r'background-color:\s*#[0-9a-fA-F]+;', '', inner_css) # remove existing
    new_rule = f'.image-placeholder {{{inner_css}    background-color: #eee;\n}}'
    css_content = css_content.replace(image_placeholder_rule.group(0), new_rule)
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css_content)

# Update HTML files
html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'raw.html']
for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to replace the text inside <div class="image-placeholder"...> ... </div>
    # and also <div class="main-hero-placeholder"> ... </div> ?
    # The prompt says "写真入れるところは...すべてここに写真を入れるイメージと書いて"
    # Let's do both .image-placeholder and .main-hero-placeholder, or just anything with "placeholder".
    
    # Replace contents of <div class="image-placeholder"...>
    # Handle optional style attributes
    content = re.sub(
        r'(<div[^>]*class="[^"]*image-placeholder[^"]*"[^>]*>).*?(</div>)',
        r'\1ここに写真を入れるイメージ\2',
        content,
        flags=re.DOTALL
    )
    
    content = re.sub(
        r'(<div[^>]*class="[^"]*main-hero-placeholder[^"]*"[^>]*>).*?(</div>)',
        r'\1ここに写真を入れるイメージ\2',
        content,
        flags=re.DOTALL
    )
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done")
