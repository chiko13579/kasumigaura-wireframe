import os
import glob

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # We want to replace "卒業生の声" with "在校生/卒業生の声" specifically in the nav areas
    new_content = content.replace('<button>卒業生の声</button>', '<button>在校生/卒業生の声</button>')
    new_content = new_content.replace('>卒業生の声</a>', '>在校生/卒業生の声</a>')
    
    # In case there's an h1 or something we also want updated, maybe the user meant all instances
    # Let's just do everywhere it is the link text or button text.
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

print("Done replacing.")
