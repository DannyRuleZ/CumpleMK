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
Quería hacerte algo diferente, algo que pudieras abrir justo a medianoche
y que te sacara una sonrisa aunque sea pequeñita.
</p>

<p>
No soy muy bueno expresando todo lo que siento,
pero quiero que sepas que eres una personita muy especial para mí.
</p>

<p>
Y aunque a veces no te lo diga tanto...
me encanta decirte <b>mi vida</b> ❤️
</p>

<p>
Espero que hoy tengas un cumpleaños hermoso,
lleno de momentos bonitos, abrazos sinceros
y muchas razones para sonreír.
</p>

<h3>
Feliz cumpleaños, mi niña bonita 🌹
</h3>
</div>
""", unsafe_allow_html=True)

st.write("")

# ---------- BOTON ----------
if st.button("Presiona aquí 🎁"):

    with st.spinner("Preparando una sorpresa para mi niña bonita..."):
        time.sleep(2)

    st.balloons()

    # AUDIO AUTOMATICO
    audio_html = """
    <audio autoplay>
      <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mp3">
    </audio>
    """

    st.components.v1.html(audio_html, height=0)

    # MENSAJE SORPRESA
    st.markdown("""
    <div class="card">

    <h2>❤️ Para ti ❤️</h2>

    <p>
    Gracias por aparecer en mi vida.
    </p>

    <p>
    Me gusta muchísimo pasar tiempo contigo,
    hablar contigo y simplemente verte feliz.
    </p>

    <p>
    Tal vez esta página no sea perfecta,
    pero la hice pensando en ti...
    y eso la hace especial para mí.
    </p>

    <p>
    Ojalá este nuevo año de vida te traiga
    muchas alegrías, metas cumplidas
    y personas que te quieran tan bonito
    como mereces.
    </p>

    <h3>
    Te quiero muchísimo ❤️
    </h3>

    </div>
    """, unsafe_allow_html=True)

# ---------- FINAL ----------
st.write("---")

st.markdown("""
<h4 style='text-align:center;'>
Hecho con cariño para alguien muy especial 🌹
</h4>
""", unsafe_allow_html=True)
