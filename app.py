import streamlit as st
from cryptography.fernet import Fernet

st.set_page_config(page_title="Gestor de Contraseñas", layout="centered")
st.title("🔐 Gestor de Contraseñas con Cifrado")

# Opción del usuario
modo = st.radio("¿Qué deseas hacer?", ("Cifrar contraseña", "Descifrar contraseña"))

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

elif modo == "Descifrar contraseña":
    st.subheader("🔓 Recuperar contraseña")
    clave_ingresada = st.text_input("Ingresa la clave secreta", type="password")
    archivo_subido = st.file_uploader("Sube el archivo cifrado (.txt)", type=["txt"])

    if clave_ingresada and archivo_subido:
        try:
            cipher = Fernet(clave_ingresada.encode())
            datos = archivo_subido.read()
            texto_descifrado = cipher.decrypt(datos).decode()
            st.success("✅ Contraseña recuperada:")
            st.code(texto_descifrado, language="text")
        except Exception as e:
            st.error("❌ Error: Clave incorrecta o archivo inválido.")
