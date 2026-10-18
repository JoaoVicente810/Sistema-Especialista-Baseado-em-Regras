MATH_OPTIONS = {
    "Baixa": "Baixa",
    "Média": "Média",
    "Alta": "Alta",
}

DAILY_OPTIONS = {
    "logica_servidor": "Escrever algoritmos, APIs e regras de negócio",
    "interfaces_visuais": "Criar interfaces, layouts e experiências visuais",
    "analisar_dados": "Analisar dados, encontrar padrões e testar hipóteses",
    "pipelines_dados": "Organizar grandes volumes de dados e criar pipelines",
    "seguranca": "Investigar vulnerabilidades e proteger sistemas",
    "automatizar_deploy": "Automatizar entregas, ambientes e processos de software",
    "infraestrutura_cloud": "Planejar servidores e infraestrutura escalável na nuvem",
    "apps_mobile": "Criar aplicativos para celulares e tablets",
    "testar_qualidade": "Testar sistemas, encontrar falhas e melhorar a qualidade",
    "produto_negocio": "Entender usuários, priorizar funcionalidades e alinhar equipes",
}

STACK_OPTIONS = {
    "Python": "Python",
    "Java": "Java",
    "JavaScript/TypeScript": "JavaScript / TypeScript",
    "SQL/BI": "SQL / ferramentas de BI",
    "Linux/Redes": "Linux / redes",
    "Docker/Git/CI-CD": "Docker / Git / CI/CD",
    "AWS/Azure/GCP": "AWS / Azure / Google Cloud",
    "Design/Figma": "Design / Figma",
    "Flutter/Kotlin/Swift": "Flutter / Kotlin / Swift",
    "Ferramentas de testes automatizados": "Ferramentas de testes automatizados",
    "Jira/Notion/Agile": "Jira / Notion / metodologias ágeis",
    "Nenhuma/Iniciante": "Ainda estou começando / nenhuma ferramenta específica",
}

VALUE_OPTIONS = {
    "api_regras": "Entregar APIs, serviços e regras de negócio confiáveis",
    "experiencia_visual": "Entregar uma experiência visual simples e agradável ao usuário",
    "insights_modelos": "Gerar previsões, padrões e insights a partir de dados",
    "dados_confiaveis": "Disponibilizar dados organizados, integrados e confiáveis",
    "protecao": "Reduzir riscos e proteger sistemas e informações",
    "automacao_estabilidade": "Automatizar operações e manter sistemas estáveis",
    "infraestrutura_escala": "Sustentar aplicações escaláveis com infraestrutura robusta",
    "app_mobile": "Entregar um bom aplicativo para dispositivos móveis",
    "confiabilidade": "Garantir que o software funcione conforme o esperado",
    "estrategia_produto": "Definir prioridades e maximizar o valor do produto",
}

EXPERIENCE_OPTIONS = {
    "Iniciante": "Iniciante — estou aprendendo os fundamentos",
    "Intermediário": "Intermediário — já desenvolvi exercícios ou projetos",
    "Avançado": "Avançado — tenho experiência prática consistente",
}

GOAL_OPTIONS = {
    "resolver_problemas": "Resolver desafios técnicos e construir soluções",
    "criatividade": "Usar criatividade e trabalhar com experiência visual",
    "investigacao": "Investigar perguntas e descobrir padrões",
    "automacao": "Eliminar tarefas manuais e automatizar processos",
    "escalabilidade": "Projetar soluções que cresçam com a demanda",
    "protecao": "Investigar riscos e melhorar a segurança",
    "confiabilidade": "Aumentar estabilidade, qualidade e confiança",
    "impacto_usuario": "Criar soluções úteis para usuários de dispositivos móveis",
    "lideranca_estrategia": "Conectar pessoas, negócio e decisões de produto",
    "aprendizado_amplo": "Explorar diferentes tecnologias e continuar aprendendo",
}

TRACKS = {
    "backend": {
        "name": "Desenvolvimento Back-end",
        "description": "Construção de APIs, regras de negócio, serviços e integração com bancos de dados.",
        "daily": "logica_servidor",
        "value": "api_regras",
        "stacks": ["Python", "Java", "SQL/BI"],
        "primary_stack": "Java",
        "math": "medium_high",
        "goal": "resolver_problemas",
        "tie_order": 1,
    },
    "frontend": {
        "name": "Desenvolvimento Front-end & UI/UX",
        "description": "Interfaces responsivas, interação, acessibilidade e experiência do usuário.",
        "daily": "interfaces_visuais",
        "value": "experiencia_visual",
        "stacks": ["JavaScript/TypeScript", "Design/Figma"],
        "primary_stack": "JavaScript/TypeScript",
        "math": "low",
        "goal": "criatividade",
        "tie_order": 2,
    },
    "data_science": {
        "name": "Ciência de Dados e Machine Learning",
        "description": "Estatística, experimentação, análise exploratória e modelos preditivos.",
        "daily": "analisar_dados",
        "value": "insights_modelos",
        "stacks": ["Python", "SQL/BI"],
        "primary_stack": "Python",
        "math": "high",
        "goal": "investigacao",
        "tie_order": 3,
    },
    "data_engineering": {
        "name": "Engenharia de Dados",
        "description": "Pipelines ETL/ELT, integração, qualidade e disponibilização de dados em escala.",
        "daily": "pipelines_dados",
        "value": "dados_confiaveis",
        "stacks": ["SQL/BI", "Python", "Linux/Redes"],
        "primary_stack": "SQL/BI",
        "math": "medium_high",
        "goal": "automacao",
        "tie_order": 4,
    },
    "security": {
        "name": "Cibersegurança (Security / Pentesting)",
        "description": "Proteção de ativos, investigação de vulnerabilidades, redes seguras e redução de riscos.",
        "daily": "seguranca",
        "value": "protecao",
        "stacks": ["Linux/Redes", "Python"],
        "primary_stack": "Linux/Redes",
        "math": "medium_high",
        "goal": "protecao",
        "tie_order": 5,
    },
    "devops": {
        "name": "DevOps & SRE",
        "description": "Automação de entrega, integração contínua, observabilidade, operações e confiabilidade.",
        "daily": "automatizar_deploy",
        "value": "automacao_estabilidade",
        "stacks": ["Docker/Git/CI-CD", "Linux/Redes"],
        "primary_stack": "Docker/Git/CI-CD",
        "math": "medium_high",
        "goal": "confiabilidade",
        "tie_order": 6,
    },
    "cloud": {
        "name": "Computação em Nuvem (Cloud Architecture)",
        "description": "Desenho e gestão de infraestrutura escalável, serviços em nuvem, custos e disponibilidade.",
        "daily": "infraestrutura_cloud",
        "value": "infraestrutura_escala",
        "stacks": ["AWS/Azure/GCP", "Docker/Git/CI-CD"],
        "primary_stack": "AWS/Azure/GCP",
        "math": "medium_high",
        "goal": "escalabilidade",
        "tie_order": 7,
    },
    "mobile": {
        "name": "Desenvolvimento Mobile",
        "description": "Aplicativos para celulares e tablets, usando desenvolvimento nativo ou multiplataforma.",
        "daily": "apps_mobile",
        "value": "app_mobile",
        "stacks": ["Flutter/Kotlin/Swift", "JavaScript/TypeScript"],
        "primary_stack": "Flutter/Kotlin/Swift",
        "math": "low",
        "goal": "impacto_usuario",
        "tie_order": 8,
    },
    "qa": {
        "name": "Engenharia de Qualidade e Testes (QA)",
        "description": "Testes manuais e automatizados, prevenção de defeitos e confiabilidade do software.",
        "daily": "testar_qualidade",
        "value": "confiabilidade",
        "stacks": ["Ferramentas de testes automatizados", "Python", "JavaScript/TypeScript"],
        "primary_stack": "Ferramentas de testes automatizados",
        "math": "medium_high",
        "goal": "confiabilidade",
        "tie_order": 9,
    },
    "product": {
        "name": "Gestão de Produtos (Product Management)",
        "description": "Ponte entre negócio, design e engenharia, com foco em necessidades, prioridades e valor.",
        "daily": "produto_negocio",
        "value": "estrategia_produto",
        "stacks": ["Jira/Notion/Agile", "Design/Figma"],
        "primary_stack": "Jira/Notion/Agile",
        "math": "low_medium",
        "goal": "lideranca_estrategia",
        "tie_order": 10,
    },
}

# Mapeia opções de resposta diretamente para sua trilha principal, usado somente
# como desempate transparente (não substitui as regras do motor Experta).
DAILY_TO_TRACK = {track["daily"]: key for key, track in TRACKS.items()}
VALUE_TO_TRACK = {track["value"]: key for key, track in TRACKS.items()}
STACK_TO_TRACK = {track["primary_stack"]: key for key, track in TRACKS.items()}

PROFILE_FIELDS = {
    "math": set(MATH_OPTIONS),
    "daily": set(DAILY_OPTIONS),
    "stack": set(STACK_OPTIONS),
    "value": set(VALUE_OPTIONS),
    "experience": set(EXPERIENCE_OPTIONS),
    "goal": set(GOAL_OPTIONS),
}
