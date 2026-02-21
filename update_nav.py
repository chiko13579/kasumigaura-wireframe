import re

html_file = 'index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

new_nav = """            <nav class="main-nav">
                <div class="nav-item"><a href="index.html"><button class="active">トップ</button></a></div>
                <div class="nav-item"><a href="news.html"><button>お知らせ</button></a></div>
                
                <div class="nav-item has-dropdown">
                    <a href="admission.html"><button>受験生案内 <span class="dropdown-arrow">▼</span></button></a>
                    <div class="dropdown-menu">
                        <a href="admission.html#guide">学校案内・データブック</a>
                        <a href="admission.html#application">出願・入試関係書類</a>
                        <a href="admission.html#consultation">個別相談会日程</a>
                        <a href="admission.html#faq">よくあるご質問</a>
                    </div>
                </div>

                <div class="nav-item has-dropdown">
                    <a href="course.html"><button>コース紹介 <span class="dropdown-arrow">▼</span></button></a>
                    <div class="dropdown-menu">
                        <a href="course.html#tokushin_senbatsu">特進選抜コース</a>
                        <a href="course.html#tokushin">特進コース</a>
                        <a href="course.html#sogo">総合進学コース</a>
                    </div>
                </div>

                <div class="nav-item has-dropdown">
                    <a href="about.html"><button>学校紹介 <span class="dropdown-arrow">▼</span></button></a>
                    <div class="dropdown-menu">
                        <a href="about.html#history">校長挨拶・沿革</a>
                        <a href="about.html#learning_center">学習センター</a>
                        <a href="about.html#facilities">施設・設備</a>
                    </div>
                </div>

                <div class="nav-item has-dropdown">
                    <a href="school_life.html"><button>学校生活 <span class="dropdown-arrow">▼</span></button></a>
                    <div class="dropdown-menu">
                        <a href="school_life.html#annual_events">年間スケジュール</a>
                        <a href="school_life.html#uniform">制服</a>
                        <a href="school_life.html#anti_bullying">いじめ防止基本方針</a>
                        <a href="school_life.html#anti_truancy">不登校未然防止方針</a>
                    </div>
                </div>

                <div class="nav-item has-dropdown">
                    <a href="career.html"><button>進路指導 <span class="dropdown-arrow">▼</span></button></a>
                    <div class="dropdown-menu">
                        <a href="career.html#career_path">進路指導体制</a>
                        <a href="career.html#results">大学合格実績</a>
                        <a href="career.html#interview">卒業生の声</a>
                    </div>
                </div>

                <div class="nav-item has-dropdown">
                    <a href="club.html"><button>部活動 <span class="dropdown-arrow">▼</span></button></a>
                    <div class="dropdown-menu">
                        <a href="club.html#sports">運動部</a>
                        <a href="club.html#culture">文化部</a>
                        <a href="club.html#records">主な戦績</a>
                    </div>
                </div>

                <div class="nav-item"><a href="interview.html"><button>卒業生の声</button></a></div>
                <div class="nav-item"><a href="recruit.html"><button>教員採用</button></a></div>
            </nav>"""

content = re.sub(r'<nav class="main-nav">.*?</nav>', new_nav, content, flags=re.DOTALL)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

# Now update CSS
css = """
/* Dropdown Navigation Styles */
.main-nav {
    display: flex;
    justify-content: center;
    gap: 10px;
    margin-bottom: 20px;
    align-items: center;
}

.main-nav .nav-item {
    position: relative;
    display: inline-block;
}

.main-nav .nav-item a button {
    display: flex;
    align-items: center;
    gap: 5px;
}

.dropdown-arrow {
    font-size: 0.7em;
    color: #888;
}

.dropdown-menu {
    display: none;
    position: absolute;
    top: 100%;
    left: 0;
    min-width: 220px;
    background-color: #2b4b6f; /* Dark blue matching visual */
    z-index: 1000;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

/* Show dropdown on hover */
.nav-item.has-dropdown:hover .dropdown-menu {
    display: block;
}

/* Dropdown items */
.dropdown-menu a {
    display: block;
    color: #fff;
    padding: 15px 20px;
    text-decoration: none;
    font-size: 15px;
    border-bottom: 1px solid #ffffff; /* White separator line */
    transition: background-color 0.2s;
    text-align: left;
}

.dropdown-menu a:last-child {
    border-bottom: none;
}

.dropdown-menu a:hover {
    background-color: #3f668f;
    color: #fff;
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css)

print("Navigation updated.")
