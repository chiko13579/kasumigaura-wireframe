import os
import re

def update_css():
    with open('style.css', 'r', encoding='utf-8') as f:
        c = f.read()

    # Remove all box-shadow properties
    c = re.sub(r'\s*box-shadow:[^;]+;', '', c)
    c = re.sub(r'\s*box-shadow:[^\n]+', '', c) # In case it's on a single line without semicolon at the end
    
    # Change light grey backgrounds to white
    light_greys = ['#f9f9f9', '#f5f5f5', '#eee', '#eaeaea', '#f0f0f0']
    for color in light_greys:
        c = re.sub(r'background-color:\s*' + color, 'background-color: #fff', c, flags=re.IGNORECASE)
        c = re.sub(r'background:\s*' + color, 'background: #fff', c, flags=re.IGNORECASE)
        
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(c)

def update_html():
    html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'raw.html']
    light_greys = ['#f9f9f9', '#f5f5f5', '#eee', '#eaeaea', '#f0f0f0']
    
    for filename in html_files:
        with open(filename, 'r', encoding='utf-8') as f:
            c = f.read()
            
        # specifically inline box-shadows
        c = re.sub(r'box-shadow:[^;"]+;?', '', c)
            
        for color in light_greys:
            c = re.sub(r'background-color:\s*' + color, 'background-color: #fff', c, flags=re.IGNORECASE)
            c = re.sub(r'background:\s*' + color, 'background: #fff', c, flags=re.IGNORECASE)
            
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(c)

update_css()
update_html()
print("Flattening completed.")
