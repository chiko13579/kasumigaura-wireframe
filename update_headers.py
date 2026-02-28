import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html') and f not in ('index.html', 'raw.html')]

with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract the new header template up to the end of main-nav
# From <header> down to </nav>\s*</div>\s*</div>
template_match = re.search(r'(<header>.*?</nav>\s*</div>\s*</div>)', index_content, re.DOTALL)
if not template_match:
    print("Could not find template in index.html")
    exit(1)
template = template_match.group(1)

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find old header: <header> ... </nav> ... <h1>TITLE</h1>
    old_header_match = re.search(r'<header>.*?</nav>\s*(<h1[^>]*>.*?</h1>)', content, re.DOTALL)
    if not old_header_match:
        print(f"Skipping {filename}: no header pattern match")
        continue

    # Find the nav block to find active class
    nav_match = re.search(r'<nav class="main-nav">(.*?)</nav>', old_header_match.group(0), re.DOTALL)
    active_href = None
    if nav_match:
        active_btn_match = re.search(r'<a href="([^"]+)"><button(?:\s+class="active")?>', nav_match.group(1))
        if active_btn_match:
            active_href = active_btn_match.group(1)
            
        # also check for <button class="active"> inside a tag
        alt_match = re.search(r'<a href="([^"]+)"><button class="active">', nav_match.group(1))
        if alt_match:
            active_href = alt_match.group(1)

    old_h1 = old_header_match.group(1)
    
    # In old files, the structure is:
    # <header> ... <div class="container"> ... <nav> ... </nav> ... <h1>...</h1> ... <div class="main-hero-placeholder"> ... </div>
    # OR <nav class="sub-nav"> etc.
    # We will replace from <header> up to </h1> with the new template (which includes <h1> inside .main-header .container)
    # AND we need to wrap the rest (from below <h1>) in <div class="container" style="padding-top: 0;"> ... </div> if it's not already.
    # Wait, the old structure has <div class="container"> that wraps EVERYTHING in the <header>.
    # So if we replace <header> ... </h1> with our new header, we need to balance the tags.
    # Our new template includes <header> ... </div></div>
    # The old file still has <div class="main-hero-placeholder"> ... </div> (and maybe sub-nav) and then </header>.
    # We should add <div class="container" style="padding-top: 0;"> before the rest of the header content.

    # Let's cleanly replace the entire <header>...</header> block.
    full_header_match = re.search(r'<header>.*?</header>', content, re.DOTALL)
    if not full_header_match:
        print(f"Skipping {filename}: no full header match")
        continue

    # Extract the part after <h1> up to </header>
    after_h1_match = re.search(r'</h1>(.*)</header>', full_header_match.group(0), re.DOTALL)
    if not after_h1_match:
        print(f"Skipping {filename}: no after h1 match")
        continue
    after_h1 = after_h1_match.group(1).strip()
    
    # If the after_h1 part starts with </div> (to close the old container), we remove it, or we just wrap whatever is useful.
    # Actually, in the old file, the container is closed inside </header>.
    # In course.html: 
    #   <h1>...</h1>
    #   <div class="main-hero-placeholder">...</div>
    #   <nav class="sub-nav">...</nav>
    #   </div> <!-- closes container -->
    # </header>
    # Let's extract everything inside the old container after h1
    inner_content_match = re.search(r'</h1>(.*)</div>\s*</header>', full_header_match.group(0), re.DOTALL)
    if inner_content_match:
        after_h1 = inner_content_match.group(1).strip()
    
    # Construct new header
    new_header = template
    new_header = re.sub(r'<h1>.*?</h1>', old_h1, new_header)
    
    new_header = new_header.replace('<button class="active">', '<button>')
    if active_href:
        new_header = re.sub(rf'(<a href="{active_href}"><button)', r'\1 class="active"', new_header)

    new_full_header = new_header + '\n        <div class="container" style="padding-top: 0;">\n            ' + after_h1 + '\n        </div>\n    </header>'

    new_content = content[:full_header_match.start()] + new_full_header + content[full_header_match.end():]

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Updated {filename}")
