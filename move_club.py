import re

html_file = 'club.html'

with open(html_file, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Extract the block
pattern = r'(\s*<div class="club-list-container">.*?</div>)'
match = re.search(pattern, html_content, flags=re.DOTALL)

if match:
    block = match.group(1)
    
    # Remove from original location
    html_content = html_content.replace(block, '\n                <div class="image-placeholder" style="height: 150px;">部活動一覧リスト</div>')
    
    # Insert right after main-hero-placeholder
    insert_pattern = r'(<div class="main-hero-placeholder">.*?</div>\n\s*</div>\n\s*</header>\n\n\s*<main class="container">)'
    
    html_content = re.sub(
        insert_pattern,
        r'\1' + '\n' + block + '\n',
        html_content
    )
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("Moved block.")
else:
    print("Block not found.")
