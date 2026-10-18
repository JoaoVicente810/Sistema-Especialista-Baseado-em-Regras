# Consultor Inteligente de Carreiras em TI

João Vicente Batista da Cunha

Sistema desenvolvido em Python que funciona como um teste vocacional para a área de Tecnologia. Através de 4 perguntas objetivas, o sistema recomenda uma entre 10 trilhas de carreira possíveis, utilizando o motor de regras lógicas *xperta e uma interface web limpa feita com Streamlit.

O sistema é capaz de identificar e recomendar as seguintes carreiras:
1. Desenvolvimento Back-end
2. Desenvolvimento Front-end & UI/UX
3. Ciência de Dados e Machine Learning
4. Engenharia de Dados
5. Cibersegurança (Security / Pentesting)
6. DevOps & SRE
7. Computação em Nuvem (Cloud Architecture)
8. Desenvolvimento Mobile
9. Engenharia de Qualidade e Testes (QA)
10. Gestão de Produtos (Product Management)

## Como rodar o projeto

1. Abra a pasta do projeto no VS Code e abra o terminal (`Ctrl` + `'` ou vá em *Terminal > New Terminal*).
2. Crie o ambiente virtual:
   ```powershell
   python -m venv .venv

3. Ativando o ambiente virtual liberando a execução de scripts:
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned; .\.venv\Scripts\Activate.ps1

4. Instale as dependências:
   pip install -r requirements.txt

5. Inicie: 
   python -m streamlit run app.py