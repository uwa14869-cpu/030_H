import base64
from pathlib import Path
 
import streamlit as st
 
st.set_page_config(
    page_title="ผู้พัฒนา | Sandal Recommendation",
    page_icon="🧑‍💻",
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
 
.stApp {
    background-color: var(--burgundy-dark);
    background-image:
        radial-gradient(circle at 20% 10%, rgba(201, 162, 39, 0.10) 0%, transparent 30%),
        radial-gradient(circle at 80% 90%, rgba(164, 22, 26, 0.45) 0%, transparent 40%),
        repeating-linear-gradient(45deg, rgba(255,255,255,0.015) 0 2px, transparent 2px 12px);
    background-attachment: fixed;
}
 
html, body, [class*="css"] {
    font-family: 'Prompt', 'Playfair Display', serif;
    color: var(--cream);
}
 
/* ---------- Hero ---------- */
.hero { text-align: center; padding: 46px 20px 20px 20px; }
.hero .ornament { color: var(--gold); letter-spacing: 12px; font-size: 0.95rem; margin-bottom: 10px; }
.hero h1 {
    font-family: 'Playfair Display', 'Prompt', serif;
    font-size: 3rem;
    font-weight: 800;
    color: var(--cream);
    margin: 0 0 12px 0;
    letter-spacing: 3px;
    text-shadow: 0 2px 0 rgba(0, 0, 0, 0.35);
}
.hero .rule {
    width: 160px; height: 3px; margin: 0 auto 16px auto;
    background: linear-gradient(90deg, transparent, var(--gold), transparent);
}
.hero p { color: var(--cream-dark); font-size: 1.05rem; margin: 0; font-weight: 300; letter-spacing: 0.5px; }
 
/* ---------- Two-column layout: photo left, card right ---------- */
.profile-layout {
    max-width: 920px;
    margin: 36px auto 0 auto;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: center;
    gap: 40px;
}
 
/* Framed portrait */
.photo-frame {
    flex: 0 0 auto;
    padding: 12px;
    background: var(--cream);
    border: 2px solid var(--gold);
    border-radius: 6px;
    box-shadow: 0 14px 30px rgba(0, 0, 0, 0.5);
    position: relative;
    transition: transform 0.3s ease;
}
.photo-frame::after {
    content: "";
    position: absolute;
    inset: 5px;
    border: 1px solid rgba(201, 162, 39, 0.6);
    pointer-events: none;
}
.photo-frame:hover { transform: translateY(-4px); }
.photo-frame img,
.photo-frame .placeholder {
    display: block;
    width: 260px;
    height: 330px;
    object-fit: cover;
    border-radius: 2px;
}
.photo-frame .placeholder {
    background: var(--cream-dark);
    color: var(--burgundy);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 4.5rem;
}
 
/* Profile card */
.profile-card {
    flex: 1 1 340px;
    max-width: 460px;
    background: var(--cream);
    color: var(--ink);
    border: 2px solid var(--gold);
    outline: 1px solid rgba(201, 162, 39, 0.45);
    outline-offset: -8px;
    border-radius: 6px;
    padding: 36px 36px 28px 36px;
    box-shadow: 0 14px 30px rgba(0, 0, 0, 0.5);
}
.profile-card .tag {
    color: var(--gold);
    font-size: 0.8rem;
    letter-spacing: 4px;
    font-weight: 600;
    margin-bottom: 8px;
}
.profile-card h2 {
    font-family: 'Playfair Display', 'Prompt', serif;
    color: var(--burgundy);
    font-size: 1.6rem;
    font-weight: 700;
    margin: 0 0 14px 0;
    line-height: 1.35;
}
.profile-card .divider {
    height: 2px; width: 70px; margin-bottom: 10px;
    background: linear-gradient(90deg, var(--gold), transparent);
}
.info-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 14px 4px;
    border-top: 1px dashed rgba(122, 22, 22, 0.25);
    font-size: 1rem;
}
.info-row:first-of-type { border-top: none; }
.info-row span.label { color: #7C5C5C; font-weight: 400; }
.info-row span.value { font-weight: 600; color: var(--red); letter-spacing: 0.5px; }
 
/* ---------- Streamlit chrome ---------- */
footer, #MainMenu { visibility: hidden; }
[data-testid="stSidebar"], [data-testid="stSidebarCollapsedControl"] { visibility: visible !important; }
 
[data-testid="stSidebar"] {
    background: var(--burgundy-dark) !important;
    border-right: 1px solid rgba(201, 162, 39, 0.35) !important;
}
[data-testid="stSidebarNav"] { padding-top: 20px; }
[data-testid="stSidebarNav"]::before {
    content: "SANDAL RECOMMENDATION";
    display: block;
    margin: 0 20px 20px 20px;
    padding-bottom: 16px;
    border-bottom: 1px solid rgba(201, 162, 39, 0.35);
    font-family: 'Playfair Display', serif;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 2px;
    color: var(--gold-light);
}
[data-testid="stSidebarNav"] a {
    margin: 4px 12px !important;
    padding: 12px 16px !important;
    border-radius: 4px;
    color: var(--cream-dark) !important;
    font-family: 'Prompt', sans-serif;
    font-weight: 500;
    font-size: 0.95rem;
    transition: all 0.2s ease;
    background: transparent !important;
}
[data-testid="stSidebarNav"] a:hover {
    background: rgba(201, 162, 39, 0.15) !important;
    color: #FFFFFF !important;
}
[data-testid="stSidebarNav"] a[aria-current="page"] {
    background: linear-gradient(90deg, rgba(164, 22, 26, 0.7) 0%, transparent 100%) !important;
    color: var(--gold-light) !important;
    border-left: 3px solid var(--gold);
    font-weight: 600;
}
 
/* เปลี่ยนข้อความเมนู: app -> หน้าหลัก, about -> ผู้พัฒนา */
[data-testid="stSidebarNav"] li:nth-child(1) a * { font-size: 0 !important; }
[data-testid="stSidebarNav"] li:nth-child(1) a::after { content: "🏠 หน้าหลัก"; font-size: 0.95rem !important; }
[data-testid="stSidebarNav"] li:nth-child(2) a * { font-size: 0 !important; }
[data-testid="stSidebarNav"] li:nth-child(2) a::after { content: "🧑‍💻 ผู้พัฒนา"; font-size: 0.95rem !important; }
 
/* ---------- Footer ---------- */
.custom-footer {
    text-align: center;
    color: var(--gold-light);
    margin-top: 50px;
    padding: 28px 20px;
    font-size: 0.85rem;
    letter-spacing: 1px;
    border-top: 1px solid rgba(201, 162, 39, 0.35);
}
</style>
 
<div class="hero">
    <div class="ornament">✦ ✦ ✦</div>
    <h1>ผู้พัฒนา</h1>
    <div class="rule"></div>
    <p>ข้อมูลผู้จัดทำโปรเจค Sandal Recommendation</p>
</div>
""", unsafe_allow_html=True)
 
# โหลดรูปภาพ (ตรวจสอบให้แน่ใจว่าไฟล์ assets/1.jpg มีอยู่จริง)
photo_path = Path(__file__).resolve().parent.parent / "assets" / "1.jpg"
try:
    photo_b64 = base64.b64encode(photo_path.read_bytes()).decode()
    photo_html = f'<img src="data:image/jpeg;base64,{photo_b64}" alt="Profile Photo">'
except FileNotFoundError:
    photo_html = '<div class="placeholder">🧑‍💻</div>'
 
st.markdown(
    f"""
<div class="profile-layout">
    <div class="photo-frame">{photo_html}</div>
    <div class="profile-card">
        <div class="tag">DEVELOPER</div>
        <h2>ภาณุพงศ์ ภุ่มพันธ์วงค์</h2>
        <div class="divider"></div>
        <div class="info-row">
            <span class="label">รหัสนักศึกษา</span>
            <span class="value">664245030</span>
        </div>
        <div class="info-row">
            <span class="label">หมู่เรียน</span>
            <span class="value">Sec. 66/43</span>
        </div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)
 
st.markdown("""
<div class="custom-footer">
    ✦ Sandal Recommendation Projects 2026 ✦
</div>
""", unsafe_allow_html=True)
 