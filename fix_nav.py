import os
import glob
import re

html_files = glob.glob('*.html')

for filepath in html_files:
    if filepath == 'raw.html':
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the dropdown menu for school_life
    # Replace '<a href="school_life.html#uniform">制服</a>' with 
    # '<a href="school_life.html#uniform">制服</a>\n                            <a href="school_life.html#daily_schedule">在校生の1日のスケジュール</a>'
    
    new_content = content.replace(
        '<a href="school_life.html#uniform">制服</a>',
        '<a href="school_life.html#uniform">制服</a>\n                            <a href="school_life.html#daily_schedule">在校生の1日のスケジュール</a>'
    )
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

print("Done replacing.")
