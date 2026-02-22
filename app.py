import streamlit as st
import requests
import os
import json
from datetime import datetime
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

# ─────────────────────────────────────────────
# Page Config
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Brand Catalyst - The Social Lab",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────────
# Styling
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Manrope:wght@300;400;500;600;700;800&display=swap');
html, body, [class*="css"] { font-family: 'Manrope', sans-serif; }

.stApp {
background: linear-gradient(135deg, #0f172a 0%, #0b1f3a 50%, #000000 100%);

    background-attachment: fixed;
}

.brand-title {
    font-family: 'Manrope', sans-serif;
    font-weight: 800;
    font-size: 3rem;
background: linear-gradient(135deg, #dbeeff 0%, #9fd0ff 50%, #4da6ff 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.2;
    margin: 0;
}

.brand-accent {
background: linear-gradient(135deg, #dbeeff 0%, #9fd0ff 50%, #4da6ff 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.tagline {
    font-family: 'Space Mono', monospace;
    color: #9fd0ff;
    font-size: 0.95rem;
    letter-spacing: 3px;
    margin-top: 4px;
}

.section-header {
    color: white;
    font-size: 1.2rem;
    font-weight: 700;
    margin: 28px 0 14px 0;
    padding-left: 14px;
    border-left: 4px solid #667eea;
}

.caption-card {
    background: linear-gradient(135deg, rgba(102,126,234,0.12) 0%, rgba(240,147,251,0.08) 100%);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 14px;
    padding: 20px 22px;
    margin: 12px 0;
    color: #f0f0f0;
    line-height: 1.7;
    font-size: 1rem;
}

.badge {
    background: rgba(102,126,234,0.25);
    color: #c4b5fd;
    padding: 4px 14px;
    border-radius: 20px;
    font-size: 0.82rem;
    font-family: 'Space Mono', monospace;
    border: 1px solid rgba(102,126,234,0.3);
}

.char-count {
    color: rgba(255,255,255,0.4);
    font-size: 0.82rem;
    font-family: 'Space Mono', monospace;
}

.metric-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 14px;
    margin: 16px 0;
}

.metric-card {
    background: linear-gradient(135deg, rgba(102,126,234,0.18) 0%, rgba(118,75,162,0.18) 100%);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 12px;
    padding: 18px;
    text-align: center;
    
}

.metric-value {
    color: #4da6ff;
    font-size: 1.6rem;
    font-weight: 800;
    font-family: 'Space Mono', monospace;
}

.metric-label {
    color: rgba(255,255,255,0.6);
    font-size: 0.82rem;
    margin-top: 4px;
}

.success-banner {
    background: linear-gradient(135deg, #10b981 0%, #059669 100%);
    color: white;
    padding: 16px 24px;
    border-radius: 12px;
    margin: 18px 0;
    text-align: center;
    font-weight: 700;
    font-size: 1.05rem;
}

.error-banner {
    background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
    color: white;
    padding: 16px 24px;
    border-radius: 12px;
    margin: 18px 0;
    font-weight: 600;
}

.stButton > button {
    background: linear-gradient(135deg, #0f172a 0%, #0b1f3a 50%) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 14px 28px !important;
    font-weight: 700 !important;
    font-size: 1.05rem !important;
    width: 100% !important;
    letter-spacing: 0.5px;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 30px rgba(102,126,234,0.45) !important;
}
.stAppHeader, .stAppToolbar{
background: linear-gradient(135deg, #0f172a 0%, #0b1f3a 50%);
}
.stTextInput > div > div > input,
.stTextArea > div > div > textarea {
    background: linear-gradient(135deg, #111827 0%, #0b1220 50%, #000000 100%) !important;
    border: 1.5px solid rgba(255,255,255,0.18) !important;
    border-radius: 10px !important;
    color: white !important;
}

label { color: #9fd0ff !important; font-weight: 600 !important; font-size: 0.92rem !important; }

.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    background: linear-gradient(135deg, #111827 0%, #0b1220 50%, #000000 100%)
    padding: 8px;
    border-radius: 14px;
    border: 1px solid rgba(255,255,255,0.08);
}

.stTabs [data-baseweb="tab"] {
    background: transparent;
    border-radius: 10px;
    color: rgba(255,255,255,0.55);
    font-weight: 600;
    padding: 10px 22px;
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #111827 0%, #0b1220 50%, #000000 100%) !important;
    color: white !important;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(135deg, #111827 0%, #0b1220 50%, #000000 100%) !important;
    border-right: 1px solid rgba(255,255,255,0.08);
}

.prompt-box {
    background: rgba(0,0,0,0.35);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 10px;
    padding: 16px;
    color: rgba(255,255,255,0.7);
    font-family: 'Space Mono', monospace;
    font-size: 0.8rem;
    line-height: 1.6;
    white-space: pre-wrap;
}

.platform-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(102,126,234,0.2);
    border: 1px solid rgba(102,126,234,0.35);
    color: #c4b5fd;
    padding: 6px 18px;
    border-radius: 30px;
    font-weight: 700;
    font-size: 0.95rem;
    margin-bottom: 8px;
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# Session State
# ─────────────────────────────────────────────
if "result"          not in st.session_state: st.session_state.result          = None
if "form_snapshot"   not in st.session_state: st.session_state.form_snapshot   = {}
if "generated_at"    not in st.session_state: st.session_state.generated_at    = ""

# ─────────────────────────────────────────────
# Sidebar
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='padding:10px 0 20px 0;'>
        <p class='brand-title' style='font-size:1.4rem;'>✨ Brand Catalyst</p>
        <p class='tagline' style='font-size:0.72rem; letter-spacing:2px;'>THE SOCIAL LAB</p>
    </div>
    """, unsafe_allow_html=True)
    
   
    st.markdown("---")
    st.markdown("### 📖 How it Works")
    st.markdown("""
1. Fill in campaign details  
2. Choose captions / images  
3. Click **Generate**  
4. Frontend → FastAPI → OpenAI  
5. Results appear instantly!
    """)

    st.markdown("---")
    st.markdown("### 🎯 Platforms")
    for p, e in [("Instagram","📷"),("LinkedIn","💼"),("Twitter / X","🐦"),("Facebook","👥")]:
        st.markdown(f"{e} &nbsp; {p}")

    st.markdown("---")
    st.markdown("### 👥 Team")
    for name in ["Alex Jefferson","Lindsay Stephenson","Iyanu Kofoworade",
                  "Anudnya Khandekar","Aarya Joshi","Yogith Sai Meda"]:
        st.markdown(f"• {name}")
    st.markdown("---")

    st.markdown("### ⚙️ Backend Config")
    backend_url = st.text_input(
        "FastAPI Endpoint",
        value="http://localhost:8000",
        help="Where your FastAPI backend (main.py) is running"
    )

    if st.button("🔌 Test Connection", use_container_width=True):
        try:
            r = requests.get(f"{backend_url}/docs", timeout=4)
            st.success("✅ Backend connected!") if r.status_code == 200 else st.warning(f"⚠️ Status {r.status_code}")
        except Exception:
            st.error("❌ Cannot reach backend.\nRun: uvicorn main:app --reload")
    st.markdown("---")

    st.caption("Georgia State University · CIS Dept")

# ─────────────────────────────────────────────
# Header
# ─────────────────────────────────────────────
st.markdown("""
<div style='text-align:center; padding:36px 0 24px 0;'>
    <p class='brand-title'>✨ Brand Catalyst <span class='brand-accent'>- The Social Lab</span></p>
    <p class='tagline'>CREATE SMART. MARKET FASTER. GROW BIGGER.</p>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# Tabs
# ─────────────────────────────────────────────
tab1, tab2 = st.tabs(["🎨  Create Campaign", "📱  Generated Content"])

# ══════════════════════════════════════════════
# TAB 1  —  CAMPAIGN FORM
# ══════════════════════════════════════════════
with tab1:

    st.markdown("<p class='section-header'>Campaign Basics</p>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        username = st.text_input("👤 Username *",              placeholder="Username/ Name")
        company  = st.text_input("🏢 Company / Brand Name *",  placeholder="Brand Name")
        event    = st.text_input("🎉 Campaign Event *",        placeholder="Campaign Event - e.g. New Skincare Launch Campaign")
        title    = st.text_input("📝 Campaign Title *",        placeholder="Campaign Title - e.g. Glow That Speaks.")
    with c2:
        platform = st.selectbox(
            "🌐 Platform *",
            ["instagram","linkedin","twitter","facebook"],
            format_func=lambda x: {"instagram":"📷  Instagram","linkedin":"💼  LinkedIn",
                                    "twitter":"🐦  Twitter / X","facebook":"👥  Facebook"}[x]
        )
        product_description = st.text_area(
            "📋 Product Description *",
            placeholder="Describe your product — features, benefits, what makes it special...",
            height=220
        )

    st.markdown("<p class='section-header'>Creative Direction</p>", unsafe_allow_html=True)
    c3, c4 = st.columns(2)
    with c3:
        target_audience  = st.text_input("🎯 Target Audience",  placeholder="Traget audience - e.g. Women aged 18–35, skincare enthusiasts")
        product_type     = st.text_input("💎 Product",          placeholder="Product to highlight - e.g. Hydrating serum & glow-enhancing collection")
        style            = st.text_input("🎨 Visual Style",     placeholder="Visual feel - e.g. modern beauty brand aesthetic, clean luxury")
        color            = st.text_input("🖌️ Color Palette",    placeholder="Backgroud color - e.g. soft peach, nude pink, warm beige")
    with c4:
        campaign_message = st.text_input("💬 Campaign Message", placeholder="Campign message - e.g. Hydrate. Glow. Repeat.")
        mood             = st.text_input("😊 Mood & Tone",      placeholder="Tone of the content - e.g. confident, radiant, fresh, luxurious")
        cta              = st.text_input("📣 Call to Action",   placeholder="Campaign goal - e.g. Shop Now")
        layout           = st.text_area("🖼️ Layout",           placeholder="Layout brief if any - e.g. product close-up, soft lighting, smooth background...", height=114)

    st.markdown("<p class='section-header'>Product Features</p>", unsafe_allow_html=True)
    num_feat  = st.number_input("How many features?", min_value=1, max_value=10, value=4, step=1)
    features  = []
    feat_cols = st.columns(2)
    for i in range(int(num_feat)):
        with feat_cols[i % 2]:
            v = st.text_input(f"Feature {i+1}", placeholder="", key=f"feat_{i}")
            if v.strip():
                features.append(v.strip())

    st.markdown("<p class='section-header'>Content Options</p>", unsafe_allow_html=True)
    c5, c6 = st.columns(2)
    with c5:
        st.markdown("**What to generate:**")
        want_captions = st.checkbox("✍️  Generate Captions (OpenAI gpt-4o-mini)", value=True)
        want_images   = st.checkbox("🖼️  Generate Images (OpenAI gpt-image-1)", value=False)
    with c6:
        num_captions = st.slider("Number of Captions", 0, 6, 4)
        num_images   = st.slider("Number of Images",   0,  4, 2,
                                  help="Each image costs OpenAI credits — max 4")

    # Required field check
    required_ok = all([username.strip(), company.strip(), event.strip(),
                       title.strip(), product_description.strip()])
    nothing_selected = not want_captions and not want_images

    if not required_ok:
        st.info("⚠️  Fields marked * are required.")
    if nothing_selected:
        st.warning("⚠️  Select at least one: Captions or Images.")

    st.markdown("<br>", unsafe_allow_html=True)
    generate_clicked = st.button(
        "✨  Generate Content",
        use_container_width=True,
        disabled=(not required_ok or nothing_selected)
    )

    if generate_clicked:
        # Exact schema match with models.py → GenerateRequest
        payload = {
            "username":            username.strip(),
            "platform":            platform,
            "company":             company.strip(),
            "event":               event.strip(),
            "title":               title.strip(),
            "product_description": product_description.strip(),
            "num_images":          int(num_images),
            "num_captions":        int(num_captions),
            "brand_name":          company.strip(),
            "color":               color.strip()            or None,
            "want_images":         want_images,
            "want_captions":       want_captions,
            "Target_audience":     target_audience.strip()  or None,
            "Product":             product_type.strip()     or None,
            "Style":               style.strip()            or None,
            "campaign_message":    campaign_message.strip() or None,
            "features":            features                 or None,
            "layout":              layout.strip()           or None,
            "mood":                mood.strip()             or None,
            "call_to_action":      cta.strip()              or None,
        }

        with st.spinner("🤖 AI is crafting your content — images may take 20–40 sec..."):
            try:
                resp = requests.post(f"{backend_url}/generate", json=payload, timeout=120)

                if resp.status_code == 200:
                    st.session_state.result        = resp.json()
                    st.session_state.form_snapshot = payload
                    st.session_state.generated_at  = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    st.markdown("<div class='success-banner'>🎉 Content Generated Successfully!</div>",
                                unsafe_allow_html=True)
                    st.info("👉 Switch to the **Generated Content** tab to view results!")

                elif resp.status_code == 400:
                    detail = resp.json().get("detail","Bad request")
                    st.markdown(f"<div class='error-banner'>⚠️ {detail}</div>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<div class='error-banner'>❌ Backend error {resp.status_code}</div>",
                                unsafe_allow_html=True)

            except requests.exceptions.ConnectionError:
                st.markdown("""
                <div class='error-banner'>
                ❌ <b>Cannot connect to backend.</b><br>
                Start your FastAPI server:<br>
                <code style='background:rgba(0,0,0,0.3);padding:2px 6px;border-radius:4px;'>
                uvicorn main:app --reload
                </code>
                </div>""", unsafe_allow_html=True)

            except requests.exceptions.Timeout:
                st.markdown("""
                <div class='error-banner'>
                ⏱️ <b>Request timed out.</b>
                Image generation can take up to 60 s. Try fewer images or captions only.
                </div>""", unsafe_allow_html=True)

            except Exception as e:
                st.markdown(f"<div class='error-banner'>❌ Unexpected error: {e}</div>",
                            unsafe_allow_html=True)

# ══════════════════════════════════════════════
# TAB 2  —  RESULTS
# ══════════════════════════════════════════════
with tab2:

    if not st.session_state.result:
        st.markdown("""
        <div style='text-align:center; padding:70px 20px; color:rgba(255,255,255,0.45);'>
            <div style='font-size:3rem; margin-bottom:16px;'>🎨</div>
            <h3 style='color:rgba(255,255,255,0.7);'>Nothing generated yet</h3>
            <p style='font-size:1rem; margin-top:10px;'>
                Fill in the form and click
                <strong style='color:#c4b5fd;'>Generate Content</strong>.
            </p>
        </div>""", unsafe_allow_html=True)

    else:
        result   = st.session_state.result
        snap     = st.session_state.form_snapshot
        plat     = snap.get("platform","")

        p_emoji  = {"instagram":"📷","linkedin":"💼","twitter":"🐦","facebook":"👥"}.get(plat,"📱")
        p_color  = {"instagram":"#E1306C","linkedin":"#0077B5","twitter":"#1DA1F2","facebook":"#4267B2"}.get(plat,"#667eea")

        # Campaign header card
        st.markdown(f"""
        <div style='background:linear-gradient(135deg,{p_color}22,{p_color}3a);
                    padding:28px 32px; border-radius:16px; margin-bottom:24px;
                    border:1.5px solid {p_color}44;'>
            <span class='platform-pill'>{p_emoji} {plat.capitalize()}</span>
            <h2 style='color:white; margin:6px 0 4px 0; font-size:1.8rem;'>
                {snap.get("title","Campaign")}
            </h2>
            <p style='color:#c4b5fd; margin:0; font-family:"Space Mono",monospace; font-size:0.82rem;'>
                {snap.get("company","")} &nbsp;·&nbsp; {st.session_state.generated_at}
            </p>
        </div>""", unsafe_allow_html=True)

        # Metrics
        captions_out = result.get("captions", [])
        images_out   = result.get("images",   [])
        avg_chars    = round(sum(len(c) for c in captions_out) / max(len(captions_out), 1))

        st.markdown(f"""
        <div class='metric-row'>
            <div class='metric-card'>
                <div class='metric-value'>{len(captions_out)}</div>
                <div class='metric-label'>Captions</div>
            </div>
            <div class='metric-card'>
                <div class='metric-value'>{len(images_out)}</div>
                <div class='metric-label'>Images</div>
            </div>
            <div class='metric-card'>
                <div class='metric-value'>{avg_chars}</div>
                <div class='metric-label'>Avg. Characters</div>
            </div>
            <div class='metric-card'>
                <div class='metric-value'>{plat.capitalize()}</div>
                <div class='metric-label'>Platform</div>
            </div>
        </div>""", unsafe_allow_html=True)

        # ── Captions ─────────────────────────────────
        if captions_out:
           
            st.markdown("<p class='section-header'>✍️ Generated Captions</p>", unsafe_allow_html=True)
            for idx, caption in enumerate(captions_out):
                safe = caption.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
                st.markdown(f"""
                <div class='caption-card'>
                    <p style='margin:0; white-space:pre-wrap;'>{safe}</p>
                    <div style='display:flex; gap:10px; margin-top:12px; align-items:center;'>
                        <span class='badge'>Caption {idx+1}</span>
                        <span class='char-count'>{len(caption)} chars</span>
                    </div>
                </div>""", unsafe_allow_html=True)
                if st.button(f"📋  Copy Caption {idx+1}", key=f"copy_{idx}"):
                    st.code(caption, language=None)

        # ── Images ───────────────────────────────────
        if images_out:
            st.markdown("<p class='section-header'>🖼️ Generated Images</p>", unsafe_allow_html=True)
            username_val = snap.get("username","")
            safe_user = username_val.replace(" ", "_")
            image_dir = os.path.join("generated_images", safe_user)

            cols = st.columns(min(len(images_out), 3))
            for idx, filename in enumerate(images_out):
                file_only = os.path.basename(str(filename))      
                filepath  = os.path.join(image_dir, file_only)   

                with cols[idx % 3]:
                    if os.path.exists(filepath):
                        img = Image.open(filepath)
                        st.image(img, caption=f"Image {idx+1}", width=250)

                        with open(filepath, "rb") as f:
                            st.download_button(
                                label=f"⬇️ Download Image {idx+1}",
                                data=f.read(),
                                file_name=filename,
                                mime="image/png",
                                key=f"dl_img_{idx}",
                                use_container_width=True
                            )
                    else:
                        st.warning(f"File not found: `{filepath}`\n\nRun frontend from the same folder as your backend.")
        

        # ── Export ────────────────────────────────────
        st.markdown("<p class='section-header'>💾 Export</p>", unsafe_allow_html=True)
        col_a, col_b = st.columns(2)

        with col_a:
            st.download_button(
                label="📥 Download Full Campaign JSON",
                data=json.dumps({"input": snap, "output": result,
                                 "generated_at": st.session_state.generated_at}, indent=2),
                file_name=f"campaign_{plat}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json",
                use_container_width=True
            )
        with col_b:
            if captions_out:
                txt = "\n\n---\n\n".join([f"Caption {i+1}:\n{c}" for i, c in enumerate(captions_out)])
                st.download_button(
                    label="📄 Download Captions as .txt",
                    data=txt,
                    file_name=f"captions_{plat}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                    mime="text/plain",
                    use_container_width=True
                )
