# 🌟 **Chat Bot con Configuración Dinámica por Rol** 🌟

[![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge)](https://streamlit.io/)  
[![Cohere](https://img.shields.io/badge/Cohere-API-blue?style=for-the-badge)](https://cohere.ai/)  
[![Python](https://img.shields.io/badge/Python-3.8%2B-yellow?style=for-the-badge)](https://www.python.org/)

## ✨ **Descripción del Proyecto**

¡Bienvenido al **Chat Bot con Configuración Dinámica por Rol**! 🚀  
Este proyecto permite configurar dinámicamente un chatbot con roles personalizados. Define un rol, responde preguntas específicas y obtén una experiencia de interacción adaptada a tus necesidades.

---

## 🛠️ **Características**

- **🎭 Configuración de Roles Personalizados**  
  Define un rol para la IA, desde un médico hasta un paciente, ¡o cualquier otro!  
  Ejemplo: "paciente con fiebre", "ingeniero", "escritor creativo".

- **❓ Preguntas Dinámicas**  
  La aplicación genera preguntas específicas basadas en el rol seleccionado.  
  Ejemplo:  
  - "¿En qué área me especializo?"  
  - "¿Cómo prefiero responder?"

- **💬 Chat Interactivo**  
  Una vez configurado, interactúa con la IA en tiempo real, obteniendo respuestas adaptadas al contexto.

- **⚡ Potenciado por Cohere y Streamlit**  
  Utilizamos la API de Cohere para generar contenido contextual y Streamlit para la interfaz interactiva.

---

## 🚀 **Cómo Usarlo**

1. **Configura el Rol**  
   Selecciona un rol único para la IA ingresando un texto descriptivo, como:  
   `"médico especializado en cardiología"` o `"paciente con gripe"`.

2. **Responde Preguntas**  
   La IA te hará preguntas relacionadas con el rol para personalizar la experiencia.

3. **Interactúa**  
   ¡Comienza el chat y obtén respuestas adaptadas a tus necesidades específicas!

---

## 🖥️ **Requisitos**

### 📦 **Dependencias**

- [Python 3.8+](https://www.python.org/)  
- [Streamlit](https://streamlit.io/)  
- [Cohere API Key](https://cohere.ai/)

### 🔧 **Instalación**

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio
   pip install -r requirements.txt
   [secrets]
   COHERE_API_KEY = "tu_clave_api"
   streamlit run app.py
   
## 🧩 Estructura del Proyecto   
```bash 
      📂 Proyecto
      │
      ├── app.py                  # Código principal de la aplicación
      ├── requirements.txt        # Lista de dependencias
      ├── .streamlit/             # Configuración de Streamlit
      │   └── secrets.toml        # Almacén de claves API
      └── README.md               # Este archivo



