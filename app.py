import streamlit as st

from decision_data import (
    DAILY_OPTIONS,
    MATH_OPTIONS,
    STACK_OPTIONS,
    VALUE_OPTIONS
)
from expert_system import recommend

st.set_page_config(
    page_title="Consultor de Carreiras em TI",
    layout="wide"
)

st.title("Consultor Inteligente de Carreiras em TI")

with st.form("career_interview"):
    st.subheader("Entrevista Dinamica")
    
    math_answer = st.radio(
        "Como voce avalia sua afinidade com matematica e estatistica?",
        options=list(MATH_OPTIONS),
        format_func=lambda item: MATH_OPTIONS[item],
        index=1,
    )
    
    stack_answer = st.selectbox(
        "Qual linguagem ou ferramenta de maior afinidade atual?",
        options=list(STACK_OPTIONS),
        format_func=lambda item: STACK_OPTIONS[item],
        index=0,
    )
    
    daily_answer = st.selectbox(
        "Qual atividade voce mais gostaria de fazer no dia a dia?",
        options=list(DAILY_OPTIONS),
        format_func=lambda item: DAILY_OPTIONS[item],
        index=0,
    )
    
    value_answer = st.selectbox(
        "Qual tipo de entrega de valor mais lhe da satisfacao?",
        options=list(VALUE_OPTIONS),
        format_func=lambda item: VALUE_OPTIONS[item],
        index=0,
    )
    
    submitted = st.form_submit_button("Analisar meu perfil")

if submitted:
    profile = {
        "math": math_answer,
        "daily": daily_answer,
        "stack": stack_answer,
        "value": value_answer,
    }
    
    try:
        result = recommend(profile)
        track = result["track"]
        
        st.subheader("Resultado da analise")
        st.success("Trilha recomendada: " + track["name"])
        st.write(track["description"])
        
        st.write("Justificativa e regras disparadas:")
        if result["evidence"]:
            for item in result["evidence"]:
                st.write(str(item["points"]) + " pontos ganhos: " + item["reason"])
        else:
            st.write("Nenhuma regra foi disparada.")
            
    except Exception as exc:
        st.error("Nao foi possivel concluir a analise.")
        st.exception(exc)