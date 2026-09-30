import streamlit as st
from dotenv import load_dotenv
import os
from google import genai

# ==========================================
# LOAD API KEY
# ==========================================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Gemini AI",
    page_icon="✨",
    layout="centered"
)


# ==========================================
# PREMIUM CSS
# ==========================================

st.markdown("""
<style>

/* ==========================================
   GLOBAL
   ========================================== */

.stApp {
    background:
        radial-gradient(
            circle at 15% 15%,
            rgba(124, 58, 237, 0.22),
            transparent 28%
        ),
        radial-gradient(
            circle at 85% 20%,
            rgba(59, 130, 246, 0.18),
            transparent 28%
        ),
        radial-gradient(
            circle at 50% 100%,
            rgba(236, 72, 153, 0.13),
            transparent 35%
        ),
        #050509;

    color: white;
}


/* Remove Streamlit top bar */

header {
    visibility: hidden;
}


/* Main container */

.block-container {
    max-width: 900px;
    padding-top: 45px;
    padding-bottom: 60px;
}


/* ==========================================
   ANIMATED BACKGROUND GLOW
   ========================================== */

.stApp::before {
    content: "";
    position: fixed;

    width: 350px;
    height: 350px;

    top: 10%;
    left: -150px;

    background: rgba(139, 92, 246, 0.12);

    filter: blur(100px);

    border-radius: 50%;

    animation: floatGlow 8s infinite alternate ease-in-out;

    pointer-events: none;
}

@keyframes floatGlow {

    from {
        transform: translateY(0px);
    }

    to {
        transform: translateY(100px);
    }

}


/* ==========================================
   TOP BADGE
   ========================================== */

.ai-badge {

    width: fit-content;

    margin: auto;

    padding: 8px 18px;

    border-radius: 50px;

    background:
        linear-gradient(
            135deg,
            rgba(139,92,246,0.15),
            rgba(59,130,246,0.12)
        );

    border: 1px solid rgba(167,139,250,0.25);

    color: #c4b5fd;

    font-size: 12px;

    font-weight: 700;

    letter-spacing: 1.5px;

    box-shadow:
        0 0 30px rgba(139,92,246,0.12);
}


/* ==========================================
   MAIN TITLE
   ========================================== */

.main-title {

    text-align: center;

    margin-top: 22px;

    font-size: 58px;

    line-height: 1.1;

    font-weight: 900;

    letter-spacing: -2px;

    background:
        linear-gradient(
            90deg,
            #ffffff,
            #c4b5fd,
            #93c5fd,
            #f0abfc,
            #ffffff
        );

    background-size: 300% auto;

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;

    animation: gradientMove 5s linear infinite;
}


@keyframes gradientMove {

    0% {
        background-position: 0% center;
    }

    100% {
        background-position: 300% center;
    }

}


/* ==========================================
   SUBTITLE
   ========================================== */

.subtitle {

    text-align: center;

    margin-top: 12px;

    color: #94a3b8;

    font-size: 17px;

    letter-spacing: 0.3px;
}


/* ==========================================
   FEATURE CARDS
   ========================================== */

.features {

    display: flex;

    justify-content: center;

    gap: 12px;

    margin-top: 28px;

    margin-bottom: 30px;

    flex-wrap: wrap;
}


.feature {

    padding: 9px 15px;

    border-radius: 50px;

    background: rgba(255,255,255,0.035);

    border: 1px solid rgba(255,255,255,0.08);

    color: #cbd5e1;

    font-size: 12px;

    backdrop-filter: blur(12px);

    transition: 0.3s;
}


.feature:hover {

    transform: translateY(-3px);

    border-color: rgba(167,139,250,0.35);

    background: rgba(139,92,246,0.08);
}


/* ==========================================
   PROMPT CARD
   ========================================== */

.prompt-card {

    padding: 24px;

    border-radius: 24px;

    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,0.055),
            rgba(255,255,255,0.018)
        );

    border: 1px solid rgba(255,255,255,0.10);

    backdrop-filter: blur(25px);

    box-shadow:
        0 25px 70px rgba(0,0,0,0.45),
        inset 0 1px 0 rgba(255,255,255,0.06);
}


/* ==========================================
   TEXT AREA
   ========================================== */

textarea {

    background: rgba(5,5,12,0.75) !important;

    color: #f8fafc !important;

    border: 1px solid rgba(255,255,255,0.10) !important;

    border-radius: 17px !important;

    padding: 18px !important;

    font-size: 16px !important;

    line-height: 1.6 !important;

    transition: 0.3s !important;
}


textarea:focus {

    border-color: #8b5cf6 !important;

    box-shadow:
        0 0 0 1px rgba(139,92,246,0.35),
        0 0 30px rgba(139,92,246,0.12) !important;
}


/* Label */

label {

    color: #e2e8f0 !important;

    font-weight: 600 !important;
}


/* ==========================================
   GENERATE BUTTON
   ========================================== */

.stButton {

    margin-top: 16px;
}


.stButton > button {

    width: 100%;

    height: 54px;

    border: none;

    border-radius: 16px;

    color: white;

    font-size: 16px;

    font-weight: 700;

    letter-spacing: 0.3px;

    background:
        linear-gradient(
            100deg,
            #6366f1,
            #8b5cf6,
            #a855f7,
            #6366f1
        );

    background-size: 250% auto;

    box-shadow:
        0 12px 35px rgba(124,58,237,0.30);

    transition: all 0.3s ease;
}


.stButton > button:hover {

    transform: translateY(-3px);

    background-position: right center;

    box-shadow:
        0 18px 45px rgba(139,92,246,0.45);
}


.stButton > button:active {

    transform: scale(0.98);
}


/* ==========================================
   RESPONSE
   ========================================== */

.response-box {

    margin-top: 30px;

    padding: 26px;

    border-radius: 22px;

    background:
        linear-gradient(
            145deg,
            rgba(139,92,246,0.08),
            rgba(15,23,42,0.75)
        );

    border: 1px solid rgba(167,139,250,0.18);

    box-shadow:
        0 20px 60px rgba(0,0,0,0.35);

    animation: responseAppear 0.5s ease;
}


@keyframes responseAppear {

    from {

        opacity: 0;

        transform: translateY(15px);

    }

    to {

        opacity: 1;

        transform: translateY(0);

    }

}


/* Response heading */

.response-title {

    display: flex;

    align-items: center;

    gap: 10px;

    color: #c4b5fd;

    font-size: 18px;

    font-weight: 800;

    margin-bottom: 15px;
}


/* ==========================================
   FOOTER
   ========================================== */

.footer {

    text-align: center;

    margin-top: 45px;

    color: #64748b;

    font-size: 12px;

    letter-spacing: 0.5px;
}


/* ==========================================
   MOBILE
   ========================================== */

@media (max-width: 600px) {

    .main-title {

        font-size: 42px;

    }

    .subtitle {

        font-size: 15px;

    }

    .prompt-card {

        padding: 16px;

    }

}

</style>
""", unsafe_allow_html=True)


# ==========================================
# HEADER
# ==========================================

st.markdown(
    '<div class="ai-badge">✦ NEXT-GENERATION AI ASSISTANT</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-title">Gemini AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Think smarter. Create faster. Discover more.'
    '</div>',
    unsafe_allow_html=True
)


# ==========================================
# FEATURES
# ==========================================

st.markdown("""
<div class="features">

    <div class="feature">⚡ Fast Responses</div>

    <div class="feature">🧠 Intelligent AI</div>

    <div class="feature">✨ Creative Answers</div>

    <div class="feature">🔒 Secure Experience</div>

</div>
""", unsafe_allow_html=True)


# ==========================================
# PROMPT SECTION
# ==========================================

st.markdown('<div class="prompt-card">', unsafe_allow_html=True)

prompt = st.text_area(
    "💬 What would you like to know?",
    placeholder=
    "Ask me anything...\n\n"
    "For example: Explain Artificial Intelligence in simple words.",
    height=170
)

if st.button("✨  Generate Response"):

    if prompt.strip():

        with st.spinner("✦ Gemini is thinking..."):

            response = client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=prompt
            )

        st.markdown(
            '<div class="response-box">'
            '<div class="response-title">'
            '🤖 Gemini Response'
            '</div>',
            unsafe_allow_html=True
        )

        st.write(response.text)

        st.markdown('</div>', unsafe_allow_html=True)

    else:

        st.warning("Please enter a prompt first.")

st.markdown('</div>', unsafe_allow_html=True)


# ==========================================
# FOOTER
# ==========================================

st.markdown(
    '<div class="footer">'
    'POWERED BY GEMINI AI • BUILT WITH STREAMLIT'
    '</div>',
    unsafe_allow_html=True
)