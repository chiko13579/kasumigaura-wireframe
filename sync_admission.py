import re
import os

html_file = 'admission.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

main_content = """        <!-- Section 1: 学校案内・データブック -->
        <section class="course-section">
            <h2 class="course-title">学校案内・データブック</h2>
            <div class="content-block center-text">
                <div class="link-grid" style="grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px;">
                    <a href="https://www.kasumi.ed.jp/wp-content/uploads/2025/06/e5ae4bbd3b319b45b67ffc8ce259311b.pdf" target="_blank" style="padding: 20px; font-weight: bold; border: 2px solid #ddd;">■ スクールガイド ２０２６</a>
                    <a href="https://www.kasumi.ed.jp/wp-content/uploads/2025/06/ce85256ba72a0e2ca72d55f48593dea7.pdf" target="_blank" style="padding: 20px; font-weight: bold; border: 2px solid #ddd;">■ データブック ２０２６</a>
                    <a href="https://www.kasumi.ed.jp/wp-content/uploads/2025/10/a4d63b51a13ebd3de2cf783bf286f264.pdf" target="_blank" style="padding: 20px; font-weight: bold; border: 2px solid #ddd;">■ 令和８年度　入学試験要項</a>
                </div>
            </div>
        </section>

        <hr>

        <!-- Section 2: 出願 -->
        <section class="course-section">
            <h2 class="course-title">出願</h2>
            <div class="content-block center-text">
                <div style="margin-bottom: 20px;">
                    <a href="https://mirai-compass.net/usr/kasumih/common/login.jsf" target="_blank"><button style="padding: 15px 40px; font-size: 1.2em; font-weight: bold; cursor: pointer; background: #333; color: #fff; border: none; border-radius: 4px;">出 願 は こ ち ら</button></a>
                </div>
                <p>出願に関しては、入学試験要項を参照してください。</p>
            </div>
        </section>

        <hr>

        <!-- Section 3: 入試関係書類 -->
        <section class="course-section">
            <h2 class="course-title">入試関係書類</h2>
            <div class="content-block center-text">
                <div class="link-grid" style="grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px;">
                    <a href="https://www.kasumi.ed.jp/wp-content/uploads/2025/10/4f8e1cd2405eed5d204ed3280cb20159.xlsx" target="_blank" style="padding: 20px; font-weight: bold; border: 2px solid #ddd;">■ 推薦書</a>
                    <a href="https://www.kasumi.ed.jp/wp-content/uploads/2025/10/20af271b900571542c8b579a7b09ba65.xlsx" target="_blank" style="padding: 20px; font-weight: bold; border: 2px solid #ddd;">■ 調査書</a>
                </div>
            </div>
        </section>

        <hr>

        <!-- Section 4: 個別相談会日程 -->
        <section class="course-section">
            <h2 class="course-title">2025年度　個別相談会日程</h2>
            <div class="content-block center-text">
                <div class="link-grid" style="grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin-top: 20px;">
                     <a href="https://mirai-compass.net/usr/kasumih/event/evtIndex.jsf" target="_blank" style="padding: 15px; background: #eee;">お申し込み</a>
                     <a href="https://mirai-compass.net/usr/kasumih/event/evtIndex.jsf" target="_blank" style="padding: 15px; background: #eee;">お申し込み</a>
                     <a href="https://mirai-compass.net/usr/kasumih/event/evtIndex.jsf" target="_blank" style="padding: 15px; background: #eee;">お申し込み</a>
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
                </div>
                
                <div class="grade-box" style="margin-bottom: 20px;">
                    <h4>学校生活について知りたい</h4>
                    <p style="margin-top: 10px;"><a href="https://www.kasumi.ed.jp/?page_id=1194#seikatu2" target="_blank" style="color: #333; text-decoration: underline;">制服紹介ページ</a></p>
                </div>

                <div class="grade-box" style="margin-bottom: 20px;">
                    <h4>毎日の学習について知りたい</h4>
                    <p style="margin-top: 10px;"><a href="https://www.kasumi.ed.jp" target="_blank" style="color: #333; text-decoration: underline;">霞ヶ浦高等学校</a></p>
                </div>
            </div>
        </section>

        <hr>

        <!-- Section 6: 霞ヶ浦通信 -->
        <section class="course-section">
            <h2 class="course-title">霞ヶ浦通信</h2>
            <div class="content-block">
                <ul style="list-style: none; padding: 0;">
                    <li style="border-bottom: 1px dashed #ccc; padding: 15px 0;">
                        <span style="color: #666; font-size: 0.9em; margin-right: 15px;">2026年2月3日</span>
                        <a href="https://www.kasumi.ed.jp/%e3%80%90%e3%83%81%e3%82%a2%e3%83%80%e3%83%b3%e3%82%b9%e9%83%a8%e3%82%88%e3%82%8a%e3%81%8a%e7%9f%a5%e3%82%89%e3%81%9b%e3%80%91/" target="_blank" style="color: #333; text-decoration: none; font-weight: bold;">【チアダンス部よりお知らせ】</a>
                    </li>
                    <li style="border-bottom: 1px dashed #ccc; padding: 15px 0;">
                        <span style="color: #666; font-size: 0.9em; margin-right: 15px;">2026年2月3日</span>
                        <a href="https://www.kasumi.ed.jp/%e3%80%90%e3%83%81%e3%82%a2%e3%83%80%e3%83%b3%e3%82%b9%e9%83%a8%e3%80%80%e6%b4%bb%e5%8b%95%e5%a0%b1%e5%91%8a%e3%80%91-12/" target="_blank" style="color: #333; text-decoration: none; font-weight: bold;">【チアダンス部　活動報告】</a>
                    </li>
                    <li style="border-bottom: 1px dashed #ccc; padding: 15px 0;">
                        <span style="color: #666; font-size: 0.9em; margin-right: 15px;">2026年1月29日</span>
                        <a href="https://www.kasumi.ed.jp/%e3%80%90%e7%94%b7%e5%ad%90%e3%82%bd%e3%83%95%e3%83%88%e3%83%86%e3%83%8b%e3%82%b9%e9%83%a8%e3%80%80%e6%88%a6%e7%b8%be%e5%a0%b1%e5%91%8a%e3%80%91-10/" target="_blank" style="color: #333; text-decoration: none; font-weight: bold;">【男子ソフトテニス部　戦績報告】</a>
                    </li>
                    <li style="border-bottom: 1px dashed #ccc; padding: 15px 0;">
                        <span style="color: #666; font-size: 0.9em; margin-right: 15px;">2026年1月17日</span>
                        <a href="https://www.kasumi.ed.jp/%e3%80%90%e6%96%b0%e7%94%9f%e5%be%92%e4%bc%9a%e5%bd%b9%e5%93%a1%e3%81%ae%e4%bb%bb%e5%91%bd%e5%bc%8f%e3%81%8c%e8%a1%8c%e3%82%8f%e3%82%8c%e3%81%be%e3%81%97%e3%81%9f%e3%80%82%e3%80%91/" target="_blank" style="color: #333; text-decoration: none; font-weight: bold;">【新生徒会役員の任命式が行われました。】</a>
                    </li>
                    <li style="border-bottom: 1px dashed #ccc; padding: 15px 0;">
                        <span style="color: #666; font-size: 0.9em; margin-right: 15px;">2026年1月16日</span>
                        <a href="https://www.kasumi.ed.jp/%e3%80%90jrc%e3%83%9c%e3%83%a9%e3%83%b3%e3%83%86%e3%82%a3%e3%82%a2%e5%90%8c%e5%a5%bd%e4%bc%9a%e3%80%80%e6%b4%bb%e5%8b%95%e5%a0%b1%e5%91%8a%e3%80%91-9/" target="_blank" style="color: #333; text-decoration: none; font-weight: bold;">【JRCボランティア同好会　活動報告】</a>
                    </li>
                </ul>
            </div>
        </section>"""

content = re.sub(r'<main class="container">.*?</main>', f'<main class="container">\n{main_content}\n    </main>', content, flags=re.DOTALL)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated admission.html")
