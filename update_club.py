import re

html_file = 'club.html'
css_file = 'style.css'

with open(html_file, 'r', encoding='utf-8') as f:
    html_content = f.read()

new_content = """            <div class="club-list-container">
                <a href="#" class="club-button">レスリング部</a>
                <a href="#" class="club-button">硬式野球部</a>
                <a href="#" class="club-button">バレーボール部</a>
                <a href="#" class="club-button">女子バレーボール部</a>
                <a href="#" class="club-button">テニス部</a>
                <a href="#" class="club-button">チア・ダンス部</a>
                <a href="#" class="club-button">ヨット部</a>
                <a href="#" class="club-button">陸上部</a>
                <a href="#" class="club-button">軟式野球部</a>
                <a href="#" class="club-button">ハンドボール部</a>
                <a href="#" class="club-button">バドミントン部</a>
                <a href="#" class="club-button">卓球部</a>
                <a href="#" class="club-button">男子ソフトテニス部</a>
                <a href="#" class="club-button">女子ソフトテニス部</a>
                <a href="#" class="club-button">男子バスケットボール部</a>
                <a href="#" class="club-button">女子バスケットボール部</a>
                <a href="#" class="club-button">柔道部</a>
                <a href="#" class="club-button">剣道部</a>
                <a href="#" class="club-button">弓道部</a>
                <a href="#" class="club-button">男サッカー部</a>
                <a href="#" class="club-button">女サッカー部</a>
                <a href="#" class="club-button">水泳部</a>
            </div>"""

html_content = re.sub(
    r'<div class="image-placeholder" style="height: 150px;">部活動一覧リスト</div>',
    new_content,
    html_content
)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

with open(css_file, 'a', encoding='utf-8') as f:
    f.write('''
/* Club List Buttons */
.club-list-container {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    justify-content: center;
    margin-top: 20px;
}

.club-button {
    background-color: #3562a6;
    color: #fff;
    padding: 10px 15px;
    border-radius: 4px;
    text-decoration: none;
    font-size: 14px;
    transition: background-color 0.2s ease, transform 0.2s ease;
}

.club-button:hover {
    background-color: #1a407a;
    transform: translateY(-2px);
}
''')

print("Updated club.html and style.css")
