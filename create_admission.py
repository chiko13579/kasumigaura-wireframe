import re
import os

html_file = 'about.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Update <title> and <h1>
content = re.sub(r'<title>.*?</title>', '<title>受験生案内 - 霞ヶ浦高等学校</title>', content)
content = re.sub(r'<h1>.*?</h1>', '<h1>受験生案内</h1>', content)

# Remove the hero image from about.html header
content = re.sub(r'<img src="img/facility.jpg".*?>', '<div class="main-hero-placeholder">受験生案内イメージ (学校案内パンフレット等)</div>', content, flags=re.DOTALL)

# Move active class
content = content.replace('class="active"', '')
content = re.sub(r'(<button>受験生案内</button>)', r'<button class="active">受験生案内</button>', content)

main_content = """
        <!-- Section 1: 学校案内・データブック -->
        <section class="course-section">
            <h2 class="course-title">学校案内・データブック</h2>
            <div class="content-block center-text">
                <div class="link-grid" style="grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px;">
                    <a href="#" style="padding: 20px; font-weight: bold; border: 2px solid #ddd;">■ スクールガイド 2026 (PDF)</a>
                    <a href="#" style="padding: 20px; font-weight: bold; border: 2px solid #ddd;">■ データブック 2026 (PDF)</a>
                    <a href="#" style="padding: 20px; font-weight: bold; border: 2px solid #ddd;">■ 令和8年度 入学試験要項 (PDF)</a>
                </div>
            </div>
        </section>

        <hr>

        <!-- Section 2: 出願 -->
        <section class="course-section">
            <h2 class="course-title">出願</h2>
            <div class="content-block center-text">
                <p>出願に関しては、入学試験要項を参照してください。</p>
                <div style="margin-top: 20px;">
                    <a href="#"><button style="padding: 15px 40px; font-size: 1.2em; font-weight: bold; cursor: pointer; background: #333; color: #fff; border: none; border-radius: 4px;">出願はこちら</button></a>
                </div>
            </div>
        </section>

        <hr>

        <!-- Section 3: 入試関係書類 -->
        <section class="course-section">
            <h2 class="course-title">入試関係書類</h2>
            <div class="content-block center-text">
                <div class="link-grid" style="grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px;">
                    <a href="#" style="padding: 20px; font-weight: bold; border: 2px solid #ddd;">■ 推薦書 (Excel)</a>
                    <a href="#" style="padding: 20px; font-weight: bold; border: 2px solid #ddd;">■ 調査書 (Excel)</a>
                </div>
            </div>
        </section>

        <hr>

        <!-- Section 4: 個別相談会日程 -->
        <section class="course-section">
            <h2 class="course-title">2025年度 個別相談会日程</h2>
            <div class="content-block center-text">
                <p>※日程は現在調整中です。<br>決まり次第、こちらに予約フォーム「お申し込み」ボタンを設置します。</p>
                <div class="link-grid" style="grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin-top: 20px;">
                     <a href="#" style="padding: 15px; background: #eee;">第1回 お申し込み</a>
                     <a href="#" style="padding: 15px; background: #eee;">第2回 お申し込み</a>
                     <a href="#" style="padding: 15px; background: #eee;">第3回 お申し込み</a>
                </div>
            </div>
        </section>

        <hr>

        <!-- Section 5: よくあるご質問 -->
        <section class="course-section">
            <h2 class="course-title">よくあるご質問</h2>
            <div class="content-block">
                <div class="grade-box" style="margin-bottom: 20px;">
                    <h4>入試について知りたい</h4>
                    <ul class="guidance-list">
                        <li>Q. 令和7年度の入試結果を教えてください。<br>A. オープンスクールや入試説明会等で詳細をご説明します。</li>
                        <li>Q. その他の入試に関する質問...<br>A. 回答が入ります。</li>
                    </ul>
                </div>
                
                <div class="grade-box" style="margin-bottom: 20px;">
                    <h4>学校生活について知りたい</h4>
                    <p style="margin-top: 10px;"><a href="school_life.html" style="color: #333; text-decoration: underline;">制服紹介ページへ</a></p>
                </div>

                <div class="grade-box" style="margin-bottom: 20px;">
                    <h4>毎日の学習について知りたい</h4>
                    <p style="margin-top: 10px;"><a href="index.html" style="color: #333; text-decoration: underline;">霞ヶ浦高等学校トップへ</a></p>
                </div>
            </div>
        </section>

        <hr>

        <!-- Section 6: 霞ヶ浦通信 -->
        <section class="course-section">
            <h2 class="course-title">霞ヶ浦通信（最近のお知らせ）</h2>
            <div class="content-block">
                <ul style="list-style: none; padding: 0;">
                    <li style="border-bottom: 1px dashed #ccc; padding: 15px 0;">
                        <span style="color: #666; font-size: 0.9em; margin-right: 15px;">2026年2月3日</span>
                        <a href="#" style="color: #333; text-decoration: none; font-weight: bold;">【チアダンス部よりお知らせ】</a>
                    </li>
                    <li style="border-bottom: 1px dashed #ccc; padding: 15px 0;">
                        <span style="color: #666; font-size: 0.9em; margin-right: 15px;">2026年2月3日</span>
                        <a href="#" style="color: #333; text-decoration: none; font-weight: bold;">【チアダンス部　活動報告】</a>
                    </li>
                    <li style="border-bottom: 1px dashed #ccc; padding: 15px 0;">
                        <span style="color: #666; font-size: 0.9em; margin-right: 15px;">2026年1月29日</span>
                        <a href="#" style="color: #333; text-decoration: none; font-weight: bold;">【男子ソフトテニス部　戦績報告】</a>
                    </li>
                    <li style="border-bottom: 1px dashed #ccc; padding: 15px 0;">
                        <span style="color: #666; font-size: 0.9em; margin-right: 15px;">2026年1月17日</span>
                        <a href="#" style="color: #333; text-decoration: none; font-weight: bold;">【新生徒会役員の任命式が行われました。】</a>
                    </li>
                    <li style="border-bottom: 1px dashed #ccc; padding: 15px 0;">
                        <span style="color: #666; font-size: 0.9em; margin-right: 15px;">2026年1月16日</span>
                        <a href="#" style="color: #333; text-decoration: none; font-weight: bold;">【JRCボランティア同好会　活動報告】</a>
                    </li>
                </ul>
            </div>
        </section>
"""

content = re.sub(r'<main class="container">.*?</main>', f'<main class="container">\n{main_content}\n    </main>', content, flags=re.DOTALL)

with open('admission.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Created admission.html")
