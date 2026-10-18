# Consultor Inteligente de Carreiras em TI

Sistema especialista em Python que entrevista a pessoa usuária e recomenda uma entre 10 trilhas de carreira em Tecnologia da Informação. O motor de inferência utiliza **Experta** (`Fact`, `KnowledgeEngine` e decoradores `@Rule`) e a interface é feita em **Streamlit**.

## Funcionalidades

- Entrevista com seis dimensões: afinidade matemática/estatística, atividade diária preferida, ferramenta/tecnologia de maior afinidade, tipo de entrega de valor, experiência atual e objetivo profissional.
- Base de conhecimento com **75 regras explícitas `@Rule`**, das quais 25 combinam múltiplas respostas.
- Pontuação acumulada por trilha e justificativas textuais para as regras disparadas.
- Comparativo de pontuações das dez trilhas.
- Critério de desempate documentado: preferência diária, entrega de valor, ferramenta principal e, por último, ordem estável da matriz.
- Testes automatizados com cinco personas que representam perfis diferentes.

## Trilhas avaliadas

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

## Requisitos

- Python 3.10 ou superior (Python 3.10 é recomendado para minimizar diferenças de compatibilidade com a biblioteca Experta, que tem uma versão antiga).
- `pip`.

> Observação de compatibilidade: o projeto inclui um pequeno ajuste para os aliases antigos de `collections` usados pela dependência `frozendict` da Experta. Isso evita um erro conhecido em versões modernas de Python sem modificar o pacote instalado.

## Instalação e execução no Windows / PyCharm

1. Extraia o ZIP e abra a pasta `consultor_carreiras_ti` no PyCharm.
2. Abra o terminal integrado do PyCharm na pasta do projeto.
3. Crie um ambiente virtual (recomendado):

   ```powershell
   python -m venv .venv
   ```

4. Ative o ambiente virtual:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

   Se o PowerShell bloquear a ativação, use o terminal CMD e execute ` .venv\Scripts\activate.bat `, ou instale as dependências usando o interpretador configurado no projeto pelo PyCharm.

5. Instale as dependências:

   ```powershell
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```

6. Inicie a aplicação web:

   ```powershell
   python -m streamlit run app.py
   ```

7. O Streamlit indicará um endereço local (geralmente `http://localhost:8501`) e abrirá a aplicação no navegador.

### Executar pelo terminal sem ativar o ambiente manualmente

Se você já instalou as dependências no interpretador selecionado no PyCharm, execute `python -m streamlit run app.py` no terminal aberto na pasta do projeto.

## Executar os testes das personas

No terminal, na raiz do projeto:

```powershell
python -m unittest discover -s tests -v
```

As personas cobrem perfis de ciência de dados, engenharia de dados, cibersegurança, front-end/UI/UX e gestão de produtos. Os testes validam a trilha resultante e a existência de justificativas geradas pelo motor de regras.

## Estrutura do projeto

```text
consultor_carreiras_ti/
├── app.py                 # Interface Streamlit
├── decision_data.py       # Opções da entrevista e dados das 10 trilhas
├── expert_system.py       # Classes Fact, motor Experta e regras @Rule
├── decision_matrix.md     # Matriz de decisão e explicação da pontuação
├── requirements.txt       # Dependências Python
├── tests/
│   └── test_personas.py   # Testes automatizados das personas
├── .gitignore
└── README.md
```

## Como funciona a inferência

Cada regra disparada atribui pontos à trilha correspondente e registra uma justificativa:

| Evidência | Pontos |
|---|---:|
| Preferência de atividade diária | +6 |
| Tipo de entrega de valor | +5 |
| Afinidade com tecnologia/ferramenta relacionada | +3 |
| Combinação de atividade diária + entrega de valor | +4 adicionais |
| Cruzamentos especializados (atividade + matemática/ferramenta) em perfis-chave | +2 adicionais |
| Afinidade matemática/estatística compatível com a trilha | +2 |
| Objetivo profissional relacionado | +2 |
| Ferramenta principal + experiência intermediária/avançada | +1 adicional |

O maior total é recomendado. Em caso de empate, o sistema tenta escolher a trilha ligada à atividade diária selecionada; se não houver uma finalista correspondente, usa entrega de valor, ferramenta principal e a ordem fixa da matriz. O critério é informado no resultado.

## Publicar no GitHub

1. Crie um repositório novo no GitHub.
2. Coloque os arquivos desta pasta no repositório.
3. Faça o commit e o push pelo terminal do PyCharm ou pela interface do Git.
4. Para executar localmente, siga os comandos da seção de instalação. Para publicação online, configure um serviço compatível com Streamlit e instale as dependências listadas em `requirements.txt`.

## Limitações

Esta é uma ferramenta acadêmica baseada em regras definidas manualmente, não um teste psicométrico validado nem uma garantia de sucesso profissional. A pontuação reflete a matriz projetada; a pessoa usuária deve comparar a recomendação com projetos práticos, pesquisa e orientação profissional.
