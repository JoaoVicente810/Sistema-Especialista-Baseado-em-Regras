# Fase 1: Engenharia de Conhecimento e Matriz de Decisão

Para esta primeira fase do projeto, estruturamos a nossa base de conhecimento em 4 perguntas principais (dimensões) que o usuário responde na entrevista. Cada resposta dispara regras no motor de inferência (Experta) e soma pontos para as trilhas de carreira. A trilha com a maior pontuação no final é a recomendada.

## Distribuição dos Pontos (Pesos)
* **Atividade diária (+6):** Maior peso, pois define a rotina de trabalho.
* **Entrega de valor (+5):** O que o usuário gosta de ver pronto no final do dia.
* **Combinação (Atividade + Entrega) (+4):** Bônus de coerência se as duas respostas principais apontarem para a mesma trilha.
* **Ferramenta/Tecnologia (+3):** Afinidade com as linguagens ou softwares da área.
* **Afinidade Matemática (+2):** Compatibilidade do nível de matemática (Baixa, Média, Alta) com a exigência real da trilha.
* **Bônus Especializado (+2):** Cruzamentos extras para perfis muito específicos (ex: Análise de Dados + Matemática Alta soma pontos extras para Ciência de Dados).

## Matriz de Decisão (Tabela de Regras)

Abaixo mostramos exatamente quais respostas ativam a pontuação para cada uma das 10 trilhas:

| Trilha | Atividade diária (+6) | Entrega de valor (+5) | Ferramentas associadas (+3) | Afinidade matemática (+2) |
|---|---|---|---|---|
| **Desenvolvimento Back-end** | Lógica no servidor | APIs e regras de negócio | Python, Java, SQL/BI | Média ou Alta |
| **Desenvolvimento Front-end** | Interfaces visuais | Experiência visual (UI/UX) | JavaScript/TypeScript, Figma | Baixa |
| **Ciência de Dados / ML** | Analisar dados | Insights e Modelos | Python, SQL/BI | Alta |
| **Engenharia de Dados** | Pipelines de dados | Dados confiáveis | SQL/BI, Python, Linux | Média ou Alta |
| **Cibersegurança** | Segurança e Pentest | Proteção de sistemas | Linux/Redes, Python | Média ou Alta |
| **DevOps & SRE** | Automatizar deploy | Automação e estabilidade | Docker/CI-CD, Linux | Média ou Alta |
| **Computação em Nuvem** | Infraestrutura Cloud | Escala e infraestrutura | AWS/Azure/GCP, Docker | Média ou Alta |
| **Desenvolvimento Mobile** | Criar apps mobile | Aplicativo móvel rodando | Flutter/Kotlin, JS/TS | Baixa |
| **Engenharia de Qualidade (QA)**| Testar qualidade | Confiabilidade (sem bugs)| Ferramentas de Teste, Python | Média ou Alta |
| **Gestão de Produtos (PM)** | Produto e negócio | Estratégia de produto | Jira/Agile, Figma | Baixa ou Média |

### Critério de Desempate
Se houver empate na pontuação final entre duas ou mais carreiras, o nosso sistema desempata seguindo rigorosamente esta ordem de prioridade:
1. Atividade diária preferida.
2. Tipo de entrega de valor.
3. Ferramenta de maior afinidade.
4. Ordem fixa desta tabela.