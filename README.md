# 🔐 Gestor de Contraseñas con Cifrado

Este proyecto es una aplicación web simple creada con **Streamlit** que permite:

- Cifrar contraseñas con seguridad usando el algoritmo **Fernet (de `cryptography`)**
- Descargar el archivo cifrado (`.txt`) con la contraseña encriptada
- Recuperar una contraseña mediante la clave secreta y el archivo cifrado

---

## 🚀 ¿Cómo funciona?

### 🔏 Cifrar una contraseña:
1. Ingresa una contraseña en el campo de texto.
2. Haz clic en **“Cifrar y generar archivo”**.
3. La app:
   - Cifra la contraseña.
   - Genera una **clave secreta única** (en base64).
   - Te permite descargar el archivo cifrado (`clave_cifrada.txt`).
   - Te muestra la clave secreta (guárdala bien).

### 🔓 Descifrar una contraseña:
1. Ingresa la clave secreta generada anteriormente.
2. Sube el archivo `clave_cifrada.txt`.
3. Haz clic en **“Descifrar”**.
4. Si todo coincide, se mostrará la contraseña original.

🔐 Seguridad
No se guarda nada en servidores. Todo se cifra/descifra localmente en el navegador o backend.

La clave secreta es obligatoria para descifrar. Si la pierdes, no podrás recuperar tu contraseña.

El archivo cifrado no contiene la clave secreta, solo el contenido cifrado.

---

## ⚙️ Requisitos

Instala las dependencias con:

```bash
pip install -r requirements.txt
