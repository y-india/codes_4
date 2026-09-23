import streamlit as st

st.set_page_config(
    page_title="ValidationLoop",
    page_icon="✓",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    '''
    <style>
        :root {
            --bg: #111317;
            --text: #f3f6fa;
            --muted: #949cab;
            --blue: #2f7cff;
        }

        .stApp {
            background:
                radial-gradient(circle at 50% 0%, rgba(47,124,255,0.08), transparent 34%),
                radial-gradient(circle at 88% 70%, rgba(255,59,157,0.04), transparent 28%),
                var(--bg);
            color: var(--text);
        }

        .block-container {
            max-width: 980px;
            padding-top: 2.2rem;
            padding-bottom: 3rem;
        }

        [data-testid="stHeader"] {
            background: transparent;
        }

        [data-testid="stToolbar"] {
            visibility: hidden;
            height: 0;
        }

        .brand {
            display: flex;
            justify-content: center;
            margin: 0.8rem 0 2rem 0;
        }

        .brand-name {
            color: var(--blue);
            font-size: 2.55rem;
            font-weight: 800;
            letter-spacing: -0.04em;
            line-height: 1;
        }

        .idea-box {
            background: rgba(92, 101, 116, 0.10);
            border: 1px solid rgba(148, 156, 171, 0.22);
            border-radius: 22px;
            padding: 1.45rem 1.55rem 1.25rem 1.55rem;
            box-shadow:
                inset 0 1px 0 rgba(255,255,255,0.02),
                0 12px 36px rgba(0,0,0,0.12);
        }

        .idea-title {
            color: var(--text);
            font-size: 1.12rem;
            font-weight: 750;
            margin-bottom: 0.5rem;
        }

        .idea-helper {
            color: var(--muted);
            font-size: 0.91rem;
            line-height: 1.55;
        }

        .side-box {
            min-height: 116px;
            background: rgba(17,19,23,0.52);
            border: 1px solid #2c333e;
            border-radius: 18px;
            padding: 1rem 1.05rem;
            box-sizing: border-box;
        }

        .side-title {
            font-size: 0.88rem;
            font-weight: 750;
            margin-bottom: 0.5rem;
        }

        .side-text {
            color: #9199a7;
            font-size: 0.78rem;
            line-height: 1.55;
            margin: 0;
        }

        div[data-testid="stTextArea"] textarea {
            background: #15191f !important;
            color: var(--text) !important;
            border: 1px solid #303743 !important;
            border-radius: 17px !important;
            min-height: 145px !important;
            padding: 1rem !important;
            font-size: 0.98rem !important;
            line-height: 1.55 !important;
            resize: vertical !important;
        }

        div[data-testid="stTextArea"] textarea:focus {
            border: 1px solid var(--blue) !important;
            box-shadow: 0 0 0 1px rgba(47,124,255,0.18) !important;
        }

        div[data-testid="stTextArea"] textarea::placeholder {
            color: #6f7785 !important;
        }

        /* Research card */
        div[data-testid="stCheckbox"] {
            min-height: 116px;
            background: rgba(17,19,23,0.52);
            border: 1px solid #2c333e;
            border-radius: 18px;
            padding: 1rem 1.05rem;
            box-sizing: border-box;
            display: flex;
            align-items: center;
        }

        div[data-testid="stCheckbox"] label {
            width: 100%;
            color: #dfe5ed !important;
            font-size: 0.88rem !important;
            line-height: 1.5 !important;
        }

        div[data-testid="stCheckbox"] label p {
            margin: 0 !important;
        }

        div[data-testid="stCheckbox"] label p::before {
            content: "Internet research";
            display: block;
            color: #f3f6fa;
            font-size: 0.88rem;
            font-weight: 750;
            margin-bottom: 0.5rem;
        }

        div.stButton > button {
            width: 100%;
            min-height: 48px;
            border-radius: 14px;
            border: 1px solid var(--blue);
            background: var(--blue);
            color: #ffffff;
            font-weight: 750;
            box-shadow: 0 8px 24px rgba(47,124,255,0.20);
        }

        div.stButton > button:hover {
            background: #236ee7;
            border-color: #236ee7;
            box-shadow: 0 10px 28px rgba(47,124,255,0.28);
        }

        .status {
            margin-top: 1rem;
            padding: 0.85rem 1rem;
            border-radius: 12px;
            border: 1px solid rgba(88,160,255,0.25);
            background: rgba(47,124,255,0.07);
            color: #cfe2ff;
            font-size: 0.86rem;
        }

        .footer {
            color: #687180;
            text-align: center;
            font-size: 0.73rem;
            margin-top: 1.5rem;
        }

        @media (max-width: 780px) {
            .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
            }

            .brand-name {
                font-size: 2.1rem;
            }

            .idea-box {
                padding: 1.1rem;
                border-radius: 18px;
            }
        }
    </style>
    ''',
    unsafe_allow_html=True,
)

st.markdown(
    '''
    <div class="brand">
        <div class="brand-name">ValidationLoop</div>
    </div>
    ''',
    unsafe_allow_html=True,
)

st.markdown(
    '''
    <div class="idea-box">
        <div class="idea-title">Describe your idea</div>
        <div class="idea-helper">
            Give as much detail as you like. You can even use a story to explain how the idea
            works, who it is for, and what problem it solves.
        </div>
    </div>
    ''',
    unsafe_allow_html=True,
)

left, right = st.columns(2, gap="large")

with left:
    st.markdown(
        '''
        <div class="side-box">
            <div class="side-title">Note</div>
            <p class="side-text">
                My role is to offer guidance; the execution and final decisions are entirely yours.
            </p>
        </div>
        ''',
        unsafe_allow_html=True,
    )

with right:
    find_similar = st.checkbox(
        "Also find similar products already like this on Internet",
        value=False,
    )

st.markdown("<div style='height: 1rem'></div>", unsafe_allow_html=True)

idea_prompt = st.text_area(
    "Your idea",
    placeholder=(
        "Tell me about your idea...\n\n"
        "You can describe the problem, target users, how it works, "
        "your story, important features, or anything else you think matters."
    ),
    height=160,
    label_visibility="collapsed",
)

st.markdown("<div style='height: 0.35rem'></div>", unsafe_allow_html=True)

send_clicked = st.button(
    "SEND",
    type="primary",
    use_container_width=True,
)

if send_clicked:
    clean_idea = idea_prompt.strip()

    if not clean_idea:
        st.error("Please describe your idea before sending.")
    else:
        st.session_state["last_idea"] = clean_idea
        st.session_state["find_similar"] = find_similar

        st.markdown(
            '''
            <div class="status">
                Your idea has been received. Validation can now begin.
            </div>
            ''',
            unsafe_allow_html=True,
        )

st.markdown(
    '<div class="footer">ValidationLoop • Validate before you build.</div>',
    unsafe_allow_html=True,
)
