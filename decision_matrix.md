# Fase 1 — Matriz de decisão

A base de conhecimento usa seis respostas de entrevista. Cada trilha tem sete regras gerais: preferência diária (+6), tipo de entrega (+5), ferramenta/tecnologia (+3), cruzamento entre atividade e entrega (+4), afinidade matemática (+2), objetivo profissional (+2) e ferramenta principal combinada com experiência intermediária/avançada (+1). Cinco regras cruzadas especializadas (+2) relacionam atividade + matemática ou atividade + ferramenta para perfis-chave, totalizando 75 regras e 25 regras com condições cruzadas.

As regras são cumulativas: uma pessoa pode ativar regras de mais de uma trilha. A pontuação total, e não uma única resposta isolada, determina a recomendação. O critério de desempate está descrito no README.

| Trilha | Atividade diária (+6) | Entrega de valor (+5) | Ferramentas associadas (+3) | Afinidade matemática (+2) | Objetivo (+2) | Regra cruzada (+4) |
|---|---|---|---|---|---|---|
| Desenvolvimento Back-end | `logica_servidor` | `api_regras` | Python, Java, SQL/BI | Média ou alta | `resolver_problemas` | `logica_servidor` + `api_regras` |
| Desenvolvimento Front-end & UI/UX | `interfaces_visuais` | `experiencia_visual` | JavaScript/TypeScript, Design/Figma | Baixa | `criatividade` | `interfaces_visuais` + `experiencia_visual` |
| Ciência de Dados e Machine Learning | `analisar_dados` | `insights_modelos` | Python, SQL/BI | Alta | `investigacao` | `analisar_dados` + `insights_modelos` |
| Engenharia de Dados | `pipelines_dados` | `dados_confiaveis` | SQL/BI, Python, Linux/Redes | Média ou alta | `automacao` | `pipelines_dados` + `dados_confiaveis` |
| Cibersegurança (Security / Pentesting) | `seguranca` | `protecao` | Linux/Redes, Python | Média ou alta | `protecao` | `seguranca` + `protecao` |
| DevOps & SRE | `automatizar_deploy` | `automacao_estabilidade` | Docker/Git/CI-CD, Linux/Redes | Média ou alta | `confiabilidade` | `automatizar_deploy` + `automacao_estabilidade` |
| Computação em Nuvem (Cloud Architecture) | `infraestrutura_cloud` | `infraestrutura_escala` | AWS/Azure/GCP, Docker/Git/CI-CD | Média ou alta | `escalabilidade` | `infraestrutura_cloud` + `infraestrutura_escala` |
| Desenvolvimento Mobile | `apps_mobile` | `app_mobile` | Flutter/Kotlin/Swift, JavaScript/TypeScript | Baixa | `impacto_usuario` | `apps_mobile` + `app_mobile` |
| Engenharia de Qualidade e Testes (QA) | `testar_qualidade` | `confiabilidade` | Ferramentas de testes automatizados, Python, JavaScript/TypeScript | Média ou alta | `confiabilidade` | `testar_qualidade` + `confiabilidade` |
| Gestão de Produtos (Product Management) | `produto_negocio` | `estrategia_produto` | Jira/Notion/Agile, Design/Figma | Baixa ou média | `lideranca_estrategia` | `produto_negocio` + `estrategia_produto` |

## Mapeamento das perguntas

- **Afinidade matemática:** Baixa, Média ou Alta.
- **Atividade diária:** uma das dez atividades codificadas em `DAILY_OPTIONS` no arquivo `decision_data.py`.
- **Ferramenta/tecnologia:** Python; Java; JavaScript/TypeScript; SQL/BI; Linux/Redes; Docker/Git/CI-CD; AWS/Azure/GCP; Design/Figma; Flutter/Kotlin/Swift; ferramentas de testes automatizados; Jira/Notion/Agile; ou nenhuma/iniciante.
- **Entrega de valor:** uma das dez entregas codificadas em `VALUE_OPTIONS`.
- **Experiência:** Iniciante, Intermediário ou Avançado. Apenas nível Intermediário/Avançado com a ferramenta principal da trilha gera o bônus de +1.
- **Objetivo profissional:** uma das dez motivações de `GOAL_OPTIONS`.
- **Cruzamentos especializados:** análise de dados + matemática alta; pipelines + SQL/BI; segurança + Linux/redes; automação de entrega + Docker/Git/CI-CD; infraestrutura cloud + AWS/Azure/GCP. Cada combinação exata adiciona +2 pontos à trilha associada.

## Regras cruzadas e diferenciação entre perfis parecidos

**Ciência de Dados vs. Engenharia de Dados:** Ciência de Dados ganha evidência específica por análise de dados, insights/modelos, afinidade matemática alta e investigação. Engenharia de Dados ganha evidência específica por pipelines, dados confiáveis, SQL/BI, automação e afinidade matemática média/alta. Ambas podem reconhecer Python e SQL/BI como tecnologias relacionadas, mas os objetivos e a combinação diária + entrega de valor aumentam a precisão.

**DevOps/SRE vs. Cloud:** DevOps/SRE privilegia automação de deploy, automação/confiabilidade e Docker/Git/CI-CD; Cloud privilegia arquitetura de infraestrutura, escalabilidade e AWS/Azure/GCP.

**Front-end vs. Mobile:** Front-end privilegia interfaces web, experiência visual, JavaScript/TypeScript e criatividade; Mobile privilegia aplicativos móveis, entrega de apps móveis, Flutter/Kotlin/Swift e impacto no usuário.

**Back-end vs. Product Management:** Back-end privilegia algoritmos, APIs e regras de negócio; Product Management privilegia entendimento das necessidades, estratégia de produto, priorização e ferramentas de gestão ágil.

## Observação sobre a implementação

As regras estão declaradas explicitamente com `@Rule` em `expert_system.py`. Para manter a explicação auditável, a aplicação mostra as justificativas armazenadas por cada regra disparada. O sistema usa encadeamento para frente: respostas são declaradas como um fato `UserProfile`, o motor encontra regras compatíveis e acumula evidências e pontos.
