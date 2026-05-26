import streamlit as st
import time

st.set_page_config(
    page_title="Feliz Cumpleaños ❤️",
    page_icon="🎂",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #ffdde1, #ee9ca7);
    color: #4a1c2a;
}
h1, h2, h3 {
    text-align: center;
}
.card {
    background-color: rgba(255,255,255,0.75);
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>🎂 Feliz cumpleaños, mi niña ❤️</h1>", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h2>Hoy es un día especial</h2>
<p>
Mañana cumple años una personita muy especial para mí.
No sabía exactamente cómo sorprenderte, pero quise hacerte algo diferente,
algo hecho por mí, con cariño y pensando en ti.
</p>
<p>
Espero que esta pequeña página te saque una sonrisa ❤️
</p>
</div>
""", unsafe_allow_html=True)

st.write("")

if st.button("Haz clic aquí para tu sorpresa 🎁"):
    with st.spinner("Preparando algo bonito..."):
        time.sleep(2)

    st.balloons()

    st.markdown("""
    <div class="card">
    <h2>💖 Quiero decirte algo...</h2>
    <p>
    Me encanta tu forma de ser, tu sonrisa y esa energía bonita que tienes.
    Tal vez no siempre sepa cómo expresarlo, pero me importas mucho.
    </p>
    <p>
    Hoy solo quiero desearte un cumpleaños hermoso, lleno de alegría,
    amor y momentos que recuerdes con una sonrisa.
    </p>
    <h3>Feliz cumpleaños ❤️</h3>
    </div>
    """, unsafe_allow_html=True)

st.write("---")

st.subheader("🎶 Una canción para ti")

st.video("https://www.youtube.com/watch?v=QJO3ROT-A4E")  # puedes cambiarlo por un mariachi

st.write("---")

st.subheader("🌹 Cosas que me gustan de ti")

frases = [
    "Tu sonrisa.",
    "Tu forma de hablar.",
    "Lo especial que eres.",
    "La paz que transmites.",
    "Cómo haces que todo se sienta más bonito."
]

for frase in frases:
    st.write(f"❤️ {frase}")

st.write("---")

st.markdown("""
<h3 style='text-align:center;'>Con cariño, de alguien que te quiere mucho ❤️</h3>
""", unsafe_allow_html=True)