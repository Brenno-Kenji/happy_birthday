import streamlit as st
import time

st.set_page_config(
    page_title="Parabéns Luisinha!",
    layout="centered",
    page_icon="🎉",
)

# CSS customizado
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to bottom right, #ffe0f0, #fff4d6);
    }
    .title-container {
        text-align: center;
        margin-top: 30px;
    }
    .subtitle {
        font-size: 20px;
        margin-bottom: 40px;
        color: #555;
    }
    .centered-button {
        display: flex;
        justify-content: center;
        margin: 20px auto 40px auto;
    }
    .video-row {
        display: flex;
        justify-content: center;
        gap: 40px;
        margin-top: 30px;
    }
    img, video {
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
        width: 100%;
        height: auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título e mensagem
st.markdown(
    """
    <div class="title-container">
        <h1>🎁 Presente para a 2ª melhor pessoa do mundo 🎁</h1>
        <p class="subtitle">De: Melhor pessoa do mundo &nbsp;&nbsp;&nbsp; Para: 2ª melhor pessoa do mundo 💖</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Estado do botão
if "show" not in st.session_state:
    st.session_state["show"] = False

# Função para mostrar as imagens e vídeos
def show_celebration():
    with st.container():
        cols = st.columns(2)
        with cols[0]:
            st.image("img/img1.jpg")
        with cols[1]:
            st.image("img/img2.jpg")

        time.sleep(1)
        with cols[0]:
            st.image("img/img3.jpg")
        with cols[1]:
            st.image("img/img4.jpg")

        time.sleep(1)
        st.markdown('<div class="video-row">', unsafe_allow_html=True)
        st.video("videos/video1.mp4")
        st.video("videos/video2.mp4")
        st.markdown('</div>', unsafe_allow_html=True)

# Botão centralizado mais para cima
st.markdown('<div class="centered-button">', unsafe_allow_html=True)
if not st.session_state["show"]:
    if st.button("Deseje parabéns para Luisinha 🎉"):
        st.session_state["show"] = True
        show_celebration()
else:
    show_celebration()
st.markdown('</div>', unsafe_allow_html=True)
