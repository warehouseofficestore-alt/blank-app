import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st

st.title("💧 AquaCheck")
st.write("Bienvenido a tu plataforma de control y análisis de calidad del agua.")

# Sección de monetización o apoyo al proyecto
st.markdown("---")
st.subheader("¿Te ha sido útil esta aplicación?")
st.write("Puedes apoyar el mantenimiento y desarrollo continuo de AquaCheck invitándonos a un café:")

# Botón visual con enlace externo (reemplaza el enlace por el de tu cuenta de PayPal, Buy Me a Coffee, etc.)
st.markdown(
        """
            <a href="https://www.buymeacoffee.com" target="_blank">
                    <button style="background-color: #FFDD00; color: #000000; padding: 10px 20px; border: none; border-radius: 5px; font-weight: bold; cursor: pointer;">
                                ☕ Invítanos a un café (Donar)
                                        </button>
                                            </a>
                                                """,
                                                    unsafe_allow_html=True
)

"
)