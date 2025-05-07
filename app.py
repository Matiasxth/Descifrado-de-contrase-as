import streamlit as st
from cryptography.fernet import Fernet
from io import BytesIO

st.set_page_config(page_title="Gestor de Contraseñas", layout="centered")
st.title("🔐 Gestor de Contraseñas con Cifrado")

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

            # Crear archivo en memoria
            buffer = BytesIO()
            buffer.write(texto_cifrado)
            buffer.seek(0)

            st.success("✅ Contraseña cifrada correctamente.")
            st.download_button(
                label="⬇️ Descargar archivo cifrado",
                data=buffer,
                file_name="clave_cifrada.txt",
                mime="text/plain"
            )
            st.code(clave.decode(), language="text")
            st.info("⚠️ Guarda esta clave secreta. Es obligatoria para descifrar.")
        else:
            st.warning("⚠️ Debes ingresar una contraseña primero.")

# === DESCIFRAR CONTRASEÑA ===
elif modo == "Descifrar contraseña":
    st.subheader("🔓 Recuperar contraseña")

    clave_ingresada = st.text_input("Ingresa la clave secreta", type="password")
    archivo_subido = st.file_uploader("Sube el archivo cifrado (.txt)", type=["txt"])

    if st.button("🔍 Descifrar"):
        if clave_ingresada and archivo_subido is not None:
            try:
                datos_cifrados = archivo_subido.read()
                cipher = Fernet(clave_ingresada.encode())
                texto_descifrado = cipher.decrypt(datos_cifrados).decode()
                st.success("✅ Contraseña recuperada:")
                st.code(texto_descifrado, language="text")
            except Exception as e:
                st.error("❌ Error: Clave incorrecta o archivo inválido.")
        else:
            st.warning("⚠️ Debes ingresar la clave y subir el archivo cifrado.")
