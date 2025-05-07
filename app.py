import streamlit as st
from cryptography.fernet import Fernet

st.set_page_config(page_title="Gestor de Contraseñas", layout="centered")
st.title("🔐 Gestor de Contraseñas con Cifrado")

# --- Elegir modo ---
modo = st.radio("¿Qué deseas hacer?", ("Cifrar contraseña", "Descifrar contraseña"))

# === CIFRAR CONTRASEÑA ===
if modo == "Cifrar contraseña":
    st.subheader("🔏 Ingresar contraseña para cifrar")
    texto = st.text_input("Escribe la contraseña que deseas guardar", type="password")

    if st.button("Cifrar y generar archivo"):
        if texto:
            clave = Fernet.generate_key()
            cipher = Fernet(clave)
            texto_cifrado = cipher.encrypt(texto.encode())

            # Guardar archivo cifrado
            with open("clave_cifrada.txt", "wb") as f:
                f.write(texto_cifrado)

            st.success("✅ Contraseña cifrada y archivo generado.")
            st.download_button("⬇️ Descargar archivo cifrado", data=texto_cifrado, file_name="clave_cifrada.txt")
            st.code(clave.decode(), language="text")
            st.info("⚠️ Guarda esta clave secreta. La necesitarás para descifrar.")

        else:
            st.warning("⚠️ Debes ingresar una contraseña primero.")

# === DESCIFRAR CONTRASEÑA ===
elif modo == "Descifrar contraseña":
    st.subheader("🔓 Recuperar contraseña")

    # Ingreso de clave secreta
    clave_ingresada = st.text_input("Ingresa la clave secreta", type="password")

    # Subida de archivo
    archivo_subido = st.file_uploader("Sube el archivo cifrado (.txt)", type=["txt"])

    # Guardar archivo en session_state si se sube
    if archivo_subido is not None:
        st.session_state['datos_cifrados'] = archivo_subido.read()

    # Botón para descifrar
    if st.button("🔍 Descifrar"):
        if clave_ingresada and 'datos_cifrados' in st.session_state:
            try:
                cipher = Fernet(clave_ingresada.encode())
                texto_descifrado = cipher.decrypt(st.session_state['datos_cifrados']).decode()
                st.success("✅ Contraseña recuperada:")
                st.code(texto_descifrado, language="text")
            except Exception:
                st.error("❌ Error: Clave incorrecta o archivo inválido.")
        else:
            st.warning("⚠️ Debes ingresar la clave y subir el archivo cifrado.")

