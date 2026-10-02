```python
import streamlit as st

st.set_page_config(
    page_title="Sandal Recommendation",
    page_icon="🩴",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;700;800&family=Prompt:wght@300;400;500;600&display=swap');

:root {
    --burgundy-dark: #4A0E0E;
    --burgundy: #7A1616;
    --red: #A4161A;
    --cream: #FBF4E4;
    --cream-dark: #F0E3C4;
    --gold: #C9A227;
    --gold-light: #E6C766;
    --ink: #3B1F1F;
}

/* ---------- Main Background ---------- */

.stApp {
    background-color: var(--burgundy-dark);
    background-image:
        radial-gradient(
            circle at 20% 10%,
            rgba(201, 162, 39, 0.10) 0%,
            transparent 30%
        ),
        radial-gradient(
            circle at 80% 90%,
            rgba(164, 22, 26, 0.45) 0%,
            transparent 40%
        ),
        repeating-linear-gradient(
            45deg,
            rgba(255,255,255,0.015) 0 2px,
            transparent 2px 12px
        );
    background-attachment: fixed;
}

/* ---------- Font ---------- */

html, body, [class*="css"] {
    font-family: 'Prompt', 'Playfair Display', serif;
    color: var(--cream);
}

/* ---------- Hero ---------- */

.hero {
    text-align: center;
    padding: 46px 20px 24px 20px;
}

.hero .ornament {
    color: var(--gold);
    letter-spacing: 12px;
    font-size: 0.95rem;
    margin-bottom: 10px;
}

.hero h1 {
    font-family: 'Playfair Display', 'Prompt', serif;
    font-size: 3.4rem;
    font-weight: 800;
    color: var(--cream);
    margin: 0 0 12px 0;
    letter-spacing: 3px;
    line-height: 1.2;
    text-shadow: 0 2px 0 rgba(0, 0, 0, 0.35);
}

.hero .rule {
    width: 160px;
    height: 3px;
    margin: 0 auto 16px auto;
    background: linear-gradient(
        90deg,
        transparent,
        var(--gold),
        transparent
    );
}

.hero p {
    color: var(--cream-dark);
    font-size: 1.1rem;
    margin: 0;
    font-weight: 300;
    letter-spacing: 0.5px;
}

/* ---------- Section Title ---------- */

.section-title {
    text-align: center;
    color: var(--gold-light);
    font-size: 1.15rem;
    margin: 14px 0 28px 0;
    font-weight: 500;
    letter-spacing: 1px;
}

/* ---------- Cards ---------- */

.card {
    background: var(--cream);
    color: var(--ink);
    border: 2px solid var(--gold);
    outline: 1px solid rgba(201, 162, 39, 0.45);
    outline-offset: -8px;
    border-radius: 6px;
    padding: 32px 28px 26px 28px;
    min-height: 280px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    transition: all 0.3s ease;
    margin-bottom: 24px;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.35);
}

.card:hover {
    transform: translateY(-6px);
    box-shadow: 0 18px 32px rgba(0, 0, 0, 0.5);
    border-color: var(--gold-light);
}

.card .icon {
    font-size: 2.3rem;
    margin-bottom: 10px;
    display: inline-block;
}

.card h3 {
    font-family: 'Playfair Display', 'Prompt', serif;
    color: var(--burgundy);
    margin: 0 0 8px 0;
    font-size: 1.25rem;
    font-weight: 700;
}

.card p {
    color: #6B4A4A;
    font-size: 0.92rem;
    line-height: 1.6;
    margin: 0;
}

/* ---------- Button ---------- */

.btn {
    display: block;
    text-align: center;
    text-decoration: none !important;
    padding: 11px 20px;
    border-radius: 4px;
    font-weight: 600;
    font-size: 0.95rem;
    letter-spacing: 0.5px;
    color: var(--cream) !important;
    background: linear-gradient(
        180deg,
        var(--red) 0%,
        var(--burgundy) 100%
    );
    border: 1px solid var(--gold);
    transition: all 0.25s ease;
    box-shadow: 0 3px 8px rgba(122, 22, 22, 0.35);
}

.btn:hover {
    background: linear-gradient(
        180deg,
        #C1272D 0%,
        var(--red) 100%
    );
    color: #FFFFFF !important;
    box-shadow: 0 6px 14px rgba(164, 22, 26, 0.5);
    transform: translateY(-2px);
}

/* ---------- Footer ---------- */

.custom-footer {
    text-align: center;
    color: var(--gold-light);
    margin-top: 36px;
    padding: 28px 20px;
    font-size: 0.85rem;
    letter-spacing: 1px;
    border-top: 1px solid rgba(201, 162, 39, 0.35);
}

/* ---------- Hide Streamlit Default UI ---------- */

footer,
#MainMenu {
    visibility: hidden;
}

/* ---------- Sidebar ---------- */

[data-testid="stSidebar"] {
    background: var(--burgundy-dark) !important;
    border-right: 1px solid rgba(201, 162, 39, 0.35) !important;
}

/* ---------- Responsive ---------- */

@media (max-width: 768px) {

    .hero {
        padding: 30px 15px 20px 15px;
    }

    .hero h1 {
        font-size: 2.2rem;
        letter-spacing: 1px;
    }

    .hero p {
        font-size: 0.95rem;
    }

    .card {
        min-height: 260px;
        padding: 28px 22px 22px 22px;
    }
}
</style>

<div class="hero">
    <div class="ornament">✦ ✦ ✦</div>

    <h1>SANDAL RECOMMENDATION</h1>

    <div class="rule"></div>

    <p>
        ระบบแนะนำรองเท้าแตะด้วยกราฟความสัมพันธ์ระหว่าง User และ Sandal
    </p>
</div>
""", unsafe_allow_html=True)


# ============================================================
# SECTION TITLE
# ============================================================

st.markdown(
    """
    <div class="section-title">
        🩴 รวมโปรเจกต์ระบบ Sandal Recommendation ของเรา
    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# PROJECT LINKS
# ============================================================

APPS = [

    # 1. Data Structure
    (
        "🩴",
        "โครงสร้างข้อมูล User & Sandal",
        "จัดการข้อมูลผู้ใช้และรองเท้าแตะ 10 ยี่ห้อ "
        "ด้วยฐานข้อมูลกราฟ Neo4j",
        "https://colab.research.google.com/drive/"
        "1NRomg7CdW6GqtK2tJBSN-AJcFJlRWYEk?usp=sharing",
        "เปิดระบบ →",
    ),

    # 2. User Relationship
    (
        "👥",
        "วิเคราะห์ความสัมพันธ์ User",
        "วิเคราะห์ความสัมพันธ์ FRIEND_OF และประวัติการดู"
        "รองเท้าแตะ (WATCHED)",
        "https://colab.research.google.com/drive/"
        "18WJNzWq3B92QkilPjRKDrhpUji8O31SP?usp=sharing",
        "เปิดระบบ →",
    ),

    # 3. Recommendation System
    (
        "🎯",
        "ระบบแนะนำรองเท้าแตะ",
        "แนะนำรองเท้าแตะจากยี่ห้อที่เพื่อนเคยดู "
        "โดยคิดคะแนนจากจำนวนเพื่อน",
        "https://efkaprnnlkboqb3yt5abqw.streamlit.app/",
        "เปิดเว็บไซต์ →",
    ),

    # 4. Canva Presentation 1
    (
        "🎨",
        "Presentation Canva",
        "นำเสนอโปรเจกต์ Sandal Recommendation System",
        "https://canva.link/xylbgc73dbebx00",
        "เปิด Canva →",
    ),

    # 5. Canva Presentation 2
    (
        "📊",
        "Project Canva",
        "เอกสารและรายละเอียดเพิ่มเติมของโปรเจกต์",
        "https://canva.link/xylwnnpwgpwq9hf",
        "เปิด Canva →",
    ),
]


# ============================================================
# DISPLAY CARDS
# ============================================================

cols = st.columns(3)

for col, (icon, title, desc, url, label) in zip(
    cols * ((len(APPS) + 2) // 3),
    APPS
):
    with col:
        st.markdown(
            f"""
            <div class="card">

                <div>
                    <div class="icon">{icon}</div>

                    <h3>{title}</h3>

                    <p>{desc}</p>
                </div>

                <a
                    class="btn"
                    href="{url}"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    {label}
                </a>

            </div>
            """,
            unsafe_allow_html=True,
        )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="custom-footer">
        ✦ Made with ❤️ using Streamlit ·
        Sandal Recommendation System 2026 ✦
    </div>
    """,
    unsafe_allow_html=True,
)
```
