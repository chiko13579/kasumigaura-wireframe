import re

def update_page(filename, title, active_button_text, main_content):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update <title> and <h1>
    content = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', content)
    content = re.sub(r'<h1>.*?</h1>', f'<h1>{title}</h1>', content)

    # Remove the hero image from about.html header
    content = re.sub(r'<img src="img/facility.jpg".*?>', '', content, flags=re.DOTALL)

    # Move active class
    content = content.replace('class="active"', '')
    content = re.sub(f'(<button>){active_button_text}(</button>)', f'<button class="active">{active_button_text}</button>', content)

    # Replace <main>...</main>
    new_main = f'<main class="container">\n{main_content}\n</main>'
    content = re.sub(r'<main class="container">.*?</main>', new_main, content, flags=re.DOTALL)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

# news.html
news_main = """
        <section class="course-section">
            <h2 class="course-title">お知らせ一覧</h2>
            <div class="content-block">
                <ul>
                    <li>2024.04.01 - 入学式のお知らせ</li>
                    <li>2024.05.10 - 体育祭について</li>
                    <li>2024.06.20 - オープンスクール予約開始</li>
                </ul>
            </div>
        </section>
"""
update_page('news.html', 'お知らせ', 'お知らせ', news_main)

# recruit.html
recruit_main = """
        <section class="course-section">
            <h2 class="course-title">教員採用情報</h2>
            <div class="content-block center-text">
                <p>本校の教員採用に関する情報は以下のPDFをご確認ください。</p>
                <!-- 教員採用ページは、 PDFを入れる と記載して -->
                <p style="font-weight: bold; margin-top: 20px;">PDFを入れる</p>
            </div>
        </section>
"""
update_page('recruit.html', '教員採用', '教員採用', recruit_main)
