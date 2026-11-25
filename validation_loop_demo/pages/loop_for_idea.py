import streamlit as st

st.set_page_config(
    page_title="ValidationLoop",
    page_icon="✓",
    layout="wide",
    initial_sidebar_state="collapsed",
)



# this was only for making youtube pretotype
# =========================================================
# Theme / UX
# =========================================================
st.markdown(
    """
    <style>
        :root {
            --bg: #111317;
            --panel: #1a1e24;
            --panel-2: #15191f;
            --border: #2d3440;
            --border-soft: rgba(148,156,171,0.18);
            --text: #f3f6fa;
            --muted: #949cab;
            --blue: #2f7cff;
        }

        .stApp {
            background:
                radial-gradient(circle at 50% 0%, rgba(47,124,255,0.08), transparent 34%),
                radial-gradient(circle at 90% 70%, rgba(255,59,157,0.035), transparent 28%),
                var(--bg);
            color: var(--text);
        }

        .block-container {
            max-width: 1080px;
            padding-top: 1.9rem;
            padding-bottom: 3rem;
        }

        [data-testid="stHeader"] {
            background: transparent;
        }

        [data-testid="stToolbar"] {
            visibility: hidden;
            height: 0;
        }

        /* =================================================
           Header
           ================================================= */
        .header-brand {
            color: var(--blue);
            font-size: 2.5rem;
            font-weight: 800;
            letter-spacing: -0.045em;
            line-height: 1;
            margin-top: 0.35rem;
        }

        /* =================================================
           Main instruction card
           ================================================= */
        .instruction-card {
            background: rgba(92,101,116,0.10);
            border: 1px solid var(--border-soft);
            border-radius: 22px;
            padding: 1.55rem 1.7rem 1.55rem 1.7rem;
            box-shadow:
                inset 0 1px 0 rgba(255,255,255,0.02),
                0 14px 40px rgba(0,0,0,0.14);
        }

        .instruction-heading {
            color: var(--text);
            font-size: 1.12rem;
            font-weight: 760;
            margin: 0 0 1.15rem 0;
        }

        .instruction-text {
            color: #d7dde6;
            font-size: 0.93rem;
            line-height: 1.76;
            margin: 0;
        }

        .instruction-text p {
            margin: 0 0 1.15rem 0;
        }

        .instruction-text p:last-child {
            margin-bottom: 0;
        }

        .instruction-text strong {
            color: #f3f6fa;
            font-weight: 720;
        }

        .instruction-text .mom-test {
            margin: 0.2rem 0 1.15rem 0;
            padding: 0.9rem 1rem;
            border-left: 3px solid var(--blue);
            background: rgba(47,124,255,0.055);
            border-radius: 0 12px 12px 0;
        }

        .instruction-text .mom-test-text {
            color: #aeb7c5;
            font-size: 0.88rem;
            line-height: 1.72;
        }

        .instruction-text .target-line {
            padding: 0.78rem 0.95rem;
            margin: 0 0 1.15rem 0;
            background: rgba(255,255,255,0.025);
            border: 1px solid rgba(148,156,171,0.12);
            border-radius: 12px;
        }

        /* =================================================
           Excel upload
           ================================================= */
        [data-testid="stFileUploader"] {
            margin-top: 0 !important;
        }

        [data-testid="stFileUploader"] section {
            background: var(--panel-2) !important;
            border: 1px dashed #3a4452 !important;
            border-radius: 14px !important;
            padding: 0.55rem 0.7rem !important;
        }

        [data-testid="stFileUploader"] section:hover {
            border-color: var(--blue) !important;
        }

        [data-testid="stFileUploader"] button {
            min-height: 36px !important;
            border-radius: 10px !important;
            padding: 0 0.9rem !important;
        }

        [data-testid="stFileUploader"] small {
            color: #707989 !important;
        }

        .upload-status {
            margin-top: 0.75rem;
            padding: 0.72rem 0.9rem;
            border-radius: 11px;
            border: 1px solid rgba(98,211,155,0.24);
            background: rgba(98,211,155,0.06);
            color: #bcefd5;
            font-size: 0.84rem;
        }

        /* =================================================
           Ask question
           ================================================= */
        .ask-label {
            color: #cfd6df;
            font-size: 0.85rem;
            font-weight: 700;
            margin: 1.7rem 0 0.5rem 0;
        }

        div[data-testid="stTextArea"] textarea {
            background: #15191f !important;
            color: var(--text) !important;
            border: 1px solid #303743 !important;
            border-radius: 15px !important;
            min-height: 105px !important;
            padding: 0.95rem 1rem !important;
            font-size: 0.94rem !important;
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

        .send-arrow button {
            min-height: 48px !important;
            height: 48px !important;
            width: 48px !important;
            padding: 0 !important;
            margin-top: 1.95rem !important;
            border-radius: 14px !important;
            font-size: 1.25rem !important;
            font-weight: 800 !important;
            background: var(--blue) !important;
            border-color: var(--blue) !important;
            color: white !important;
            box-shadow: 0 8px 24px rgba(47,124,255,0.18);
        }

        .send-arrow button:hover {
            background: #236ee7 !important;
            border-color: #236ee7 !important;
        }

        .question-status {
            margin-top: 0.7rem;
            padding: 0.7rem 0.9rem;
            border-radius: 11px;
            border: 1px solid rgba(88,160,255,0.24);
            background: rgba(47,124,255,0.06);
            color: #cfe2ff;
            font-size: 0.83rem;
        }

        .helper {
            color: #687180;
            text-align: center;
            font-size: 0.73rem;
            margin-top: 1.4rem;
        }

        @media (max-width: 780px) {
            .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
            }

            .header-brand {
                font-size: 2.05rem;
            }

            .instruction-card {
                padding: 1.15rem;
                border-radius: 18px;
            }

            .instruction-text {
                font-size: 0.9rem;
                line-height: 1.65;
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# Header
# =========================================================
header_left, header_right = st.columns([4.5, 1.5], gap="large")

with header_left:
    st.markdown(
        '<div class="header-brand">ValidationLoop</div>',
        unsafe_allow_html=True,
    )

with header_right:
    # Clickable for now, intentionally no action.
    modify_clicked = st.button(
        "Modify you idea",
        use_container_width=True,
    )

if modify_clicked:
    pass

# =========================================================
# Instruction card
# =========================================================
st.markdown("<div style='height: 1rem'></div>", unsafe_allow_html=True)

# The content is intentionally arranged like an AI-generated response:
# clear lead-in, separated actions, a target callout, and a Mom Test note.
instruction_html = """<div class="instruction-card"><div class="instruction-heading">Your validation step</div><div class="instruction-text"><p><strong>First try to collect emails of job seekers/data analysts:</strong>  -> You can find them on LinkedIn [best], GitHub, or through your friends.    Use an AI chatbot to help you with this.</p><div class="target-line"><strong>Your target is to find 20 emails or LinkedIn profiles</strong> of people who are looking for Data Analyst / Data-related roles.</div><p><strong>Then we will use The Mom Test on those people.</strong></p><div class="mom-test"><div class="mom-test-text">(It’s basically a practical framework for asking people the right questions so you can get honest feedback about a business idea, instead of people just saying nice things. I’ll help you with this...)</div></div><p><strong>If you don't prefer talking with people directly,</strong> there are other ways too like making a landing page, etc...  But first, you need to find relevant emails or profiles.</p><p><strong>Important:</strong> Add those profiles with their Education, Experience, what role they are looking for, etc.  Use Excel to organize everything. You can also ask an AI chatbot for help with using Excel.</p></div></div>"""

st.markdown(instruction_html, unsafe_allow_html=True)

# =========================================================
# Excel upload
# =========================================================
st.markdown("<div style='height: 0.8rem'></div>", unsafe_allow_html=True)

upload_left, upload_center, upload_right = st.columns([3.6, 1.8, 3.6], gap="large")

with upload_center:
    uploaded_file = st.file_uploader(
        "Upload your Excel file",
        type=["xlsx", "xls"],
        label_visibility="collapsed",
    )

if uploaded_file is not None:
    st.markdown(
        f"""
        <div class="upload-status">
            Excel file uploaded: <strong>{uploaded_file.name}</strong>
        </div>
        """,
        unsafe_allow_html=True,
    )

# =========================================================
# ChatGPT-style "Ask question" prompt
# =========================================================
st.markdown(
    '<div class="ask-label">Ask question</div>',
    unsafe_allow_html=True,
)

question_col, send_col = st.columns([12, 1], gap="small")

with question_col:
    question = st.text_area(
        "Ask question",
        placeholder=(
            "Ask anything about your validation step, the people you should talk to, "
            "how to organize your Excel file, or what to do next..."
        ),
        height=105,
        label_visibility="collapsed",
    )

with send_col:
    st.markdown('<div class="send-arrow">', unsafe_allow_html=True)
    ask_clicked = st.button("➜", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

if ask_clicked:
    clean_question = question.strip()

    if clean_question:
        st.session_state["last_question"] = clean_question
        st.markdown(
            """
            <div class="question-status">
                Your question has been received.
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.warning("Please enter a question first.")

# =========================================================
# Footer
# =========================================================
st.markdown(
    '<div class="helper">ValidationLoop • Validate before you build.</div>',
    unsafe_allow_html=True,
)
