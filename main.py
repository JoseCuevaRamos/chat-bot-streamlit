import streamlit as st
import time as t
import cohere

st.title("Chat Bot con Configuración Dinámica por Rol")

# Configuración inicial del rol de la IA
if "role_configured" not in st.session_state:
    st.session_state["role_configured"] = False

if not st.session_state["role_configured"]:
    with st.form("role_form"):
        st.subheader("Configurar el rol de la IA")

        # Pregunta principal: Selección del rol
        role = st.text_input("1. ¿Qué rol quieres que desempeñe la IA? (ej. 'paciente con fiebre', 'médico', 'ingeniero'):").strip()

        submit_role = st.form_submit_button("Configurar Rol")

        if submit_role and role:
            # Llamada a Cohere para generar preguntas relacionadas al rol
            co = cohere.Client(api_key=st.secrets["COHERE_API_KEY"])
            if "paciente" in role.lower():
                prompt = (
                    f"Eres un sistema experto en generación de roles. Si el rol proporcionado menciona una enfermedad explícita "
                    f"(como 'paciente con fiebre'), solo pregunta por el estado emocional. Si no menciona una enfermedad, "
                    f"pregunta por los sintomas y el estado emocional. El rol proporcionado es '{role}'. "
                    f"Genera preguntas claras y en primera persona como por ejemplo ¿Cual es mi estado de salud? no me preguntes a mi sino  para ti, sin explicaciones ni texto adicional."
                )
            else:
                prompt = (
                    f"Eres un sistema experto en generación de roles. El rol proporcionado es '{role}'. Si el rol corresponde a una "
                    f"profesión, genera dos preguntas: una para preguntar la especialidad y otra para el tipo de respuestas que prefiere "
                    f"(el usuario puede elegir entre 'creativa', 'formal', etc.). Genera preguntas claras en primera persona dicendo que son para ti como por ejemplo ¿En que area me especializo? en tiempo presente no en termino futuro, "
                    f"sin explicaciones ni texto adicional."
                )

            response = co.generate(
                model="command-xlarge-nightly",
                prompt=prompt,
                max_tokens=50,
                temperature=0.7
            )

            # Procesar las preguntas generadas
            questions = response.generations[0].text.strip().split("\n")
            st.session_state["ia_role"] = role
            st.session_state["role_questions"] = [q.strip("- ") for q in questions if q.strip()]
            st.session_state["role_configured"] = True

            st.success(f"¡Rol configurado como **{role}**!")
else:
    st.write(f"### Configuración actual de la IA:")
    st.write(f"- **Rol:** {st.session_state['ia_role']}")
    st.write(f"### Preguntas generadas para el rol:")
    for i, q in enumerate(st.session_state["role_questions"], 1):
        st.write(f"{i}. {q}")

# Responder preguntas generadas
if st.session_state["role_configured"]:
    with st.form("additional_info_form"):
        st.subheader("Responde las preguntas para personalizar la IA")

        # Mostrar preguntas generadas y capturar respuestas
        answers = {}
        for i, question in enumerate(st.session_state["role_questions"], 1):
            answers[f"q{i}"] = st.text_input(question)

        submit_answers = st.form_submit_button("Enviar Respuestas")

        if submit_answers:
            st.session_state["role_answers"] = answers
            st.success("¡Respuestas registradas! Ahora puedes comenzar a interactuar con la IA.")

# Chatbot interactivo
if "role_answers" in st.session_state:
    cont = st.container()

    ## Setting API key
    co = cohere.Client(api_key=st.secrets["COHERE_API_KEY"])

    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    with cont:
        for m in st.session_state["messages"]:
            if m["role"] == 'user':
                st.chat_message("user").write(m["content"])
            if m["role"] == "assistant":
                st.chat_message("assistant").write(m["content"])

    prompt = st.chat_input("Ingresa tu mensaje:")

    if prompt:
        st.session_state["messages"].append({
            "role": "user",
            "content": prompt
        })
        st.chat_message("user").write(prompt)

        # Crear el mensaje inicial con contexto personalizado
        context_message = f"Eres un {st.session_state['ia_role']}."
        for key, value in st.session_state["role_answers"].items():
            if value:
                context_message += f" {key}: {value}."

        context_message += f" Responde al usuario: {prompt}"

        stream = co.chat_stream(message=context_message)

        asst = st.chat_message("assistant")
        res_cont = asst.empty()

        res = ""

        for event in stream:
            if event.event_type == "text-generation":
                res += event.text
                res_cont.write(res)
                t.sleep(0.02)

        st.session_state["messages"].append({
            "role": "assistant",
            "content": res
        })

    st.markdown(
        """
        <style>
        /* Adjust padding for the container */
        @media only screen and (max-width: 600px) {
        .st-emotion-cache-1eo1tir {
                padding-left: 0px; /* Adjust padding as needed */
                padding-right:0px
            }
        }
        
        </style>
        """,
        unsafe_allow_html=True
    )
