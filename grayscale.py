with open('consultation.html', 'r', encoding='utf-8') as f:
    c = f.read()

# CSS changes
c = c.replace('border-left: 5px solid #235194;', 'border-left: 5px solid #666;')
c = c.replace('background-color: #f9f9f9;', 'background-color: #f2f2f2;')
c = c.replace('border-left: 4px solid #6b9e7d;', 'border-left: 4px solid #999;')

# HTML inline style changes
c = c.replace(
    '<img src="img/image.png" alt="笑顔の先生や、明るい校舎"\n                style="width: 100%; max-width: 1200px; height: auto; display: block; margin: 0 auto 40px auto; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">',
    '<div style="width: 100%; max-width: 1200px; height: 400px; background-color: #ddd; display: flex; align-items: center; justify-content: center; margin: 0 auto 40px auto; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); color: #666; font-size: 1.5em; font-weight: bold;">📸 笑顔の先生や、明るい校舎</div>'
)

c = c.replace('background-color: #fcebeb;', 'background-color: #f2f2f2;')
c = c.replace('color: #c00;', 'color: #333;')
c = c.replace('background-color: #d14141;', 'background-color: #555;')
c = c.replace('background-color: #eef5ff;', 'background-color: #f2f2f2;')
c = c.replace('border-left-color: #c00;', 'border-left-color: #666;')
c = c.replace('color: #235194;', 'color: #333;')

with open('consultation.html', 'w', encoding='utf-8') as f:
    f.write(c)
