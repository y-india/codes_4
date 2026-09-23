
import re
import streamlit as st

st.set_page_config(
    page_title="ValidationLoop",
    page_icon="✓",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -----------------------------
# Theme / UX
# -----------------------------
st.markdown(
    """
    <style>
        :root {
            --bg: #111317;
            --panel: #1a1e24;
            --panel-2: #20252d;
            --border: #2d3440;
            --text: #f3f6fa;
            --muted: #949cab;
            --blue: #2f7cff;
            --blue-2: #58a0ff;
            --pink: #ff3b9d;
            --success: #62d39b;
        }

        .stApp {
            background:
                radial-gradient(circle at 50% 0%, rgba(47,124,255,0.08), transparent 34%),
                radial-gradient(circle at 88% 70%, rgba(255,59,157,0.045), transparent 28%),
                var(--bg);
            color: var(--text);
        }

        .block-container {
            max-width: 1180px;
            padding-top: 2.0rem;
            padding-bottom: 2rem;
        }

        /* Remove extra Streamlit chrome */
        [data-testid="stHeader"] {
            background: transparent;
        }

        [data-testid="stToolbar"] {
            visibility: hidden;
            height: 0;
        }

        /* Header */
        .brand-wrap {
            display: flex;
            justify-content: center;
            text-align: center;
            margin: 1rem auto 2.2rem auto;
        }

        .brand {
            display: inline-flex;
            flex-direction: column;
            align-items: center;
            gap: 0.35rem;
        }

        .brand-name {
            color: var(--blue);
            font-size: 2.45rem;
            font-weight: 800;
            letter-spacing: -0.04em;
            line-height: 1;
        }

        .brand-tagline {
            color: var(--muted);
            font-size: 1.0rem;
            font-weight: 500;
            letter-spacing: 0.01em;
        }

        .brand-tagline span {
            color: var(--blue-2);
        }

        /* Intro area */
        /* Intro content sits inside the transparent box above the form */
        .intro-box {
            min-height: 126px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            padding: 1.45rem 1.65rem;
            margin-bottom: 1.55rem;
            border-radius: 22px;
            border: 1px solid rgba(148,156,171,0.17);
            background: rgba(92,101,116,0.10);
            box-shadow:
                inset 0 1px 0 rgba(255,255,255,0.02),
                0 12px 36px rgba(0,0,0,0.12);
        }

        .intro-title {
            color: var(--text);
            font-size: 1.22rem;
            font-weight: 750;
            letter-spacing: -0.02em;
            margin: 0 0 0.3rem 0;
        }

        .intro-subtitle {
            color: var(--muted);
            font-size: 0.91rem;
            line-height: 1.5;
            margin: 0;
        }

        .field-label {
            color: #dfe5ed;
            font-size: 0.88rem;
            font-weight: 650;
            margin-bottom: 0.3rem;
        }

        /* Streamlit inputs */
        div[data-testid="stTextInput"] > div > div,
        div[data-testid="stTextInput"] input,
        div[data-testid="stTextInput"] input:focus {
            border-radius: 12px !important;
        }

        div[data-testid="stTextInput"] input {
            background: #15191f !important;
            color: var(--text) !important;
            border: 1px solid #303743 !important;
            min-height: 46px !important;
        }

        div[data-testid="stTextInput"] input:focus {
            border: 1px solid var(--blue) !important;
            box-shadow: 0 0 0 1px rgba(47,124,255,0.18) !important;
        }

        div[data-testid="stTextInput"] input::placeholder {
            color: #6f7785 !important;
        }

        /* Buttons */
        div.stButton > button {
            width: 100%;
            min-height: 46px;
            border-radius: 12px;
            border: 1px solid #34404d;
            background: #1d232b;
            color: #eaf0f7;
            font-weight: 700;
            transition: all 0.16s ease;
        }

        div.stButton > button:hover {
            border-color: var(--blue);
            color: #ffffff;
            transform: translateY(-1px);
        }

        div.stButton > button[kind="primary"] {
            background: var(--blue);
            border-color: var(--blue);
            color: #ffffff;
            box-shadow: 0 8px 24px rgba(47,124,255,0.22);
        }

        div.stButton > button[kind="primary"]:hover {
            background: #236ee7;
            border-color: #236ee7;
            box-shadow: 0 10px 28px rgba(47,124,255,0.30);
        }

        div.stButton > button:disabled {
            opacity: 0.42;
            cursor: not-allowed;
            transform: none !important;
        }

        /* Explanations */
        .explain-card {
            height: 100%;
            background: rgba(17,19,23,0.58);
            border: 1px solid #2c333e;
            border-radius: 18px;
            padding: 1rem 1.05rem;
        }

        .explain-title {
            font-size: 0.9rem;
            font-weight: 750;
            margin-bottom: 0.35rem;
        }

        .explain-title.login {
            color: var(--muted);
        }

        .explain-title.signin {
            color: var(--blue-2);
        }

        .explain-text {
            color: #9199a7;
            font-size: 0.79rem;
            line-height: 1.55;
            margin: 0;
        }

        /* Status */
        .status-success {
            margin-top: 1rem;
            padding: 0.85rem 1rem;
            border: 1px solid rgba(98,211,155,0.28);
            background: rgba(98,211,155,0.08);
            border-radius: 12px;
            color: #bbf1d6;
            font-size: 0.88rem;
        }

        .status-error {
            margin-top: 1rem;
            padding: 0.85rem 1rem;
            border: 1px solid rgba(255,59,157,0.24);
            background: rgba(255,59,157,0.07);
            border-radius: 12px;
            color: #ffd0e8;
            font-size: 0.88rem;
        }

        .helper {
            color: #6f7785;
            text-align: center;
            font-size: 0.75rem;
            margin-top: 1rem;
        }

        /* Decorative line */
        .accent-line {
            height: 2px;
            width: 78px;
            border-radius: 999px;
            background: linear-gradient(90deg, var(--blue), var(--pink));
            margin: 0.65rem 0 1.25rem 0;
        }

        @media (max-width: 780px) {
            .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
            }

            .intro-box {
                min-height: 110px;
                padding: 1.1rem 1.15rem;
                border-radius: 17px;
            }

            .brand-name {
                font-size: 2rem;
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Header
# -----------------------------
st.markdown(
    """
    <div class="brand-wrap">
        <div class="brand">
            <div class="brand-name">ValidationLoop</div>
            <div class="brand-tagline"><span>Validate</span> before you build.</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# State
# -----------------------------
if "signin_message" not in st.session_state:
    st.session_state.signin_message = ""
if "signin_error" not in st.session_state:
    st.session_state.signin_error = ""

# -----------------------------
# Authentication form
# -----------------------------

st.markdown(
    '''
    <div class="intro-box">
        <div class="intro-title">Welcome to ValidationLoop</div>
        <p class="intro-subtitle">
            Create your account to validate ideas before you build them.
        </p>
    </div>
    ''',
    unsafe_allow_html=True,
)

st.markdown('<div class="accent-line"></div>', unsafe_allow_html=True)

name = st.text_input("Name", placeholder="Enter your name", label_visibility="visible")
email = st.text_input("Email address", placeholder="you@example.com", label_visibility="visible")
password = st.text_input(
    "Password",
    type="password",
    placeholder="Create a password",
    label_visibility="visible",
)

st.markdown("<div style='height: 0.35rem'></div>", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")
with col1:
    # Intentionally disabled because the requested Login button should not work.
    st.button("Login", disabled=True, use_container_width=True)

with col2:
    signin_clicked = st.button("Sign In", type="primary", use_container_width=True)

# -----------------------------
# Sign-in behavior
# -----------------------------
if signin_clicked:
    st.session_state.signin_message = ""
    st.session_state.signin_error = ""

    clean_name = name.strip()
    clean_email = email.strip()

    if not clean_name or not clean_email or not password:
        st.session_state.signin_error = "Please fill in name, email address, and password."
    elif not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", clean_email):
        st.session_state.signin_error = "Please enter a valid email address."
    elif len(password) < 6:
        st.session_state.signin_error = "Password must be at least 6 characters."
    else:
        st.session_state.signin_message = (
            f"Sign in request received for {clean_name}. "
            "This demo does not create a real account or store credentials."
        )

if st.session_state.signin_error:
    st.markdown(
        f'<div class="status-error">{st.session_state.signin_error}</div>',
        unsafe_allow_html=True,
    )

if st.session_state.signin_message:
    st.markdown(
        f'<div class="status-success">{st.session_state.signin_message}</div>',
        unsafe_allow_html=True,
    )

st.markdown("<div style='height: 1.2rem'></div>", unsafe_allow_html=True)

ex1, ex2 = st.columns(2, gap="large")
with ex1:
    st.markdown(
        """
        <div class="explain-card">
            <div class="explain-title login">What is Login?</div>
            <p class="explain-text">
                Login is for an existing user. It verifies credentials and opens the account that
                has already been created. In this demo, the Login button is intentionally disabled.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with ex2:
    st.markdown(
        """
        <div class="explain-card">
            <div class="explain-title signin">What is Sign In?</div>
            <p class="explain-text">
                Sign In creates or starts access for a user who is entering their details for the
                first time. Here it validates the form fields and shows a demo confirmation.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    '<div class="helper">UI prototype • No credentials are stored.</div>',
    unsafe_allow_html=True,
)

