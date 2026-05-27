import streamlit as st
import time

st.set_page_config(
    page_title="Feliz cumpleaños ❤️",
    page_icon="🎂",
    layout="centered"
)

# ---------- ESTILOS ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #ffd1dc, #ffe6eb);
    color: #4a1c2a;
}

h1, h2, h3, p {
    text-align: center;
}

.card {
    background-color: rgba(255,255,255,0.82);
    padding: 30px;
    border-radius: 25px;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.15);
    margin-top: 20px;
}

button[kind="secondary"] {
    border-radius: 15px;
}
</style>
""", unsafe_allow_html=True)

# ---------- TITULO ----------
st.markdown("""
<h1>🎂 Feliz cumpleaños, mi niña bonita ❤️</h1>
""", unsafe_allow_html=True)

# ---------- MENSAJE INICIAL ----------
st.markdown("""
<div class="card">
<p>
Hoy no quería darte algo común...
</p>

<p>
Quería hacerte algo diferente, que te sacara una sonrisa aunque sea pequeñita.
</p>

<p>
No soy muy bueno expresando todo lo que siento,
pero quiero que sepas que eres una personita muy especial para mí.
</p>

<h3>
Feliz cumpleaños, mi niña bonita 🌹
</h3>
</div>
""", unsafe_allow_html=True)

st.write("")

# ---------- BOTON ----------
st.markdown("""
<p style='text-align:center; font-size:18px; color:#6b2d3e;'>
🎧 Pequeña recomendación:
ajusta un poquito el volumen antes de abrir tu sorpresa ❤️
</p>
""", unsafe_allow_html=True)

if st.button("Presiona aquí 🎁"):

    with st.spinner("Preparando una sorpresa para mi niña bonita..."):
        time.sleep(2)

    st.balloons()

    # AUDIO AUTOMATICO
    with open("Chino & Nacho - Niña Bonita (Original Version).mp3", "rb") as audio_file:
        audio_bytes = audio_file.read()

    st.audio(audio_bytes, format="audio/mp3", autoplay=True)

    # MENSAJE SORPRESA
    st.markdown("""
    <div class="card">

    <h2>❤️ Para Mika ❤️</h2>

    <p>
    Espero que hoy tengas un cumpleaños hermoso,
    lleno de momentos bonitos, muchas razones para 
    sonreír y que sepas que hay alguien te que quiere
    </p>
    
    <p>
    Y aunque a veces no te lo diga tanto...
    me encanta decirte <b>mi vida</b> ❤️
    </p>

    <p>
    Me gusta muchísimo pasar tiempo contigo,
    hablar contigo y simplemente verte feliz
    </p>

    <p>
    Tal vez esta página no sea perfecta,
    pero la hice pensando en ti...
    y eso la hace especial para mí
    </p>

    <p>
    Ojalá este nuevo año de vida te traiga
    muchas alegrías, metas cumplidas
    y personas que te quieran tan bonito
    como mereces
    </p>
    
    <h3>
    Gracias por aparecer en mi vida
    </h3>

    </div>
    """, unsafe_allow_html=True)

# ---------- FINAL ----------
st.write("---")

st.markdown("""
<h4 style='text-align:center;'>
TU te mereces todo lo mejor 🌹
</h4>
""", unsafe_allow_html=True)
