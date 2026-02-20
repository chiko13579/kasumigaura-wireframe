import re

def update_interview():
    filename = 'interview.html'
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    main_content = """
        <section class="course-section">
            <div class="interview-list" style="display: flex; flex-wrap: wrap; gap: 20px;">
                <!-- Person 1 -->
                <div class="interview-card" style="width: calc(50% - 10px); border: 1px solid #ddd; padding: 20px; box-sizing: border-box;">
                    <div class="image-placeholder" style="height: 200px; margin-bottom: 15px;">卒業生A（特進コース）</div>
                    <h3>茨城大学 合格</h3>
                    <p>明確な目標を立て、最後まで諦めずに努力しました。</p>
                    <a href="interview_detail.html" style="display: inline-block; margin-top: 10px; color: #333; text-decoration: underline;">インタビューを読む</a>
                </div>
                <!-- Person 2 -->
                <div class="interview-card" style="width: calc(50% - 10px); border: 1px solid #ddd; padding: 20px; box-sizing: border-box;">
                    <div class="image-placeholder" style="height: 200px; margin-bottom: 15px;">卒業生B（総合進学コース）</div>
                    <h3>〇〇大学 合格</h3>
                    <p>部活と両立しながら第一志望に合格することができました。</p>
                    <a href="interview_detail.html" style="display: inline-block; margin-top: 10px; color: #333; text-decoration: underline;">インタビューを読む</a>
                </div>
                <!-- Person 3 -->
                <div class="interview-card" style="width: calc(50% - 10px); border: 1px solid #ddd; padding: 20px; box-sizing: border-box;">
                    <div class="image-placeholder" style="height: 200px; margin-bottom: 15px;">卒業生C（総合進学コース）</div>
                    <h3>地元優良企業へ就職</h3>
                    <p>資格取得や面接対策など、手厚いサポートに感謝しています。</p>
                    <a href="interview_detail.html" style="display: inline-block; margin-top: 10px; color: #333; text-decoration: underline;">インタビューを読む</a>
                </div>
                <!-- Person 4 -->
                <div class="interview-card" style="width: calc(50% - 10px); border: 1px solid #ddd; padding: 20px; box-sizing: border-box;">
                    <div class="image-placeholder" style="height: 200px; margin-bottom: 15px;">卒業生D（特進コース）</div>
                    <h3>△△大学 合格</h3>
                    <p>先生方との距離が近く、気軽に相談できたのがよかったです。</p>
                    <a href="interview_detail.html" style="display: inline-block; margin-top: 10px; color: #333; text-decoration: underline;">インタビューを読む</a>
                </div>
            </div>
        </section>
"""
    # Replace <main class="container">...</main>
    new_main = f'<main class="container">\n{main_content}\n    </main>'
    content = re.sub(r'<main class="container">.*?</main>', new_main, content, flags=re.DOTALL)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

update_interview()
