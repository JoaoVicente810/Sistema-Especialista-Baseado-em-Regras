"""Motor de inferência do Consultor Inteligente de Carreiras em TI.

Experta é um motor de regras de encadeamento para frente. Cada regra atribui
pontos e registra uma justificativa que pode ser mostrada ao usuário.
"""

import collections
import collections.abc

for _name in ("Awaitable", "Coroutine", "AsyncIterable", "AsyncIterator", "AsyncGenerator", "Hashable", "Iterable", "Iterator", "Generator", "Callable", "Collection", "Container", "Sequence", "MutableSequence", "Mapping", "MutableMapping", "Set", "MutableSet", "Sized"):
    if not hasattr(collections, _name) and hasattr(collections.abc, _name):
        setattr(collections, _name, getattr(collections.abc, _name))

from experta import Fact, KnowledgeEngine, OR, Rule

from decision_data import (
    DAILY_TO_TRACK,
    STACK_TO_TRACK,
    TRACKS,
    VALUE_TO_TRACK,
)


class UserProfile(Fact):
    """Respostas fornecidas pela pessoa na entrevista."""
    pass


class CareerAdvisor(KnowledgeEngine):
    """Base de conhecimento com regras de pontuação e justificativas."""

    def __init__(self):
        super().__init__()
        self.scores = {track_id: 0 for track_id in TRACKS}
        self.evidence = {track_id: [] for track_id in TRACKS}

    def award(self, track_id, points, reason):
        """Registra o efeito de uma regra disparada."""
        self.scores[track_id] += points
        self.evidence[track_id].append({"points": points, "reason": reason})

    # --- Regras para Desenvolvimento Back-end ---
    @Rule(UserProfile(daily="logica_servidor"))
    def backend_daily_preference(self):
        self.award("backend", 6, "Preferência diária compatível: Desenvolvimento Back-end (+6).")

    @Rule(UserProfile(value="api_regras"))
    def backend_delivery_value(self):
        self.award("backend", 5, "Tipo de entrega de valor compatível: Desenvolvimento Back-end (+5).")

    @Rule(OR(UserProfile(stack="Python"), UserProfile(stack="Java"), UserProfile(stack="SQL/BI")))
    def backend_tool_affinity(self):
        self.award("backend", 3, "Afinidade com ferramenta/tecnologia relevante para Desenvolvimento Back-end (+3).")

    @Rule(UserProfile(daily="logica_servidor", value="api_regras"))
    def backend_crossed_profile(self):
        self.award("backend", 4, "Regra cruzada: preferência diária e entrega de valor apontam para Desenvolvimento Back-end (+4).")

    @Rule(OR(UserProfile(math="Média"), UserProfile(math="Alta")))
    def backend_math_affinity(self):
        self.award("backend", 2, "Afinidade matemática média ou alta compatível com Desenvolvimento Back-end (+2).")

    # --- Regras para Desenvolvimento Front-end & UI/UX ---
    @Rule(UserProfile(daily="interfaces_visuais"))
    def frontend_daily_preference(self):
        self.award("frontend", 6, "Preferência diária compatível: Desenvolvimento Front-end & UI/UX (+6).")

    @Rule(UserProfile(value="experiencia_visual"))
    def frontend_delivery_value(self):
        self.award("frontend", 5, "Tipo de entrega de valor compatível: Desenvolvimento Front-end & UI/UX (+5).")

    @Rule(OR(UserProfile(stack="JavaScript/TypeScript"), UserProfile(stack="Design/Figma")))
    def frontend_tool_affinity(self):
        self.award("frontend", 3, "Afinidade com ferramenta/tecnologia relevante para Desenvolvimento Front-end & UI/UX (+3).")

    @Rule(UserProfile(daily="interfaces_visuais", value="experiencia_visual"))
    def frontend_crossed_profile(self):
        self.award("frontend", 4, "Regra cruzada: preferência diária e entrega de valor apontam para Desenvolvimento Front-end & UI/UX (+4).")

    @Rule(UserProfile(math="Baixa"))
    def frontend_math_affinity(self):
        self.award("frontend", 2, "Afinidade matemática baixa compatível com Desenvolvimento Front-end & UI/UX (+2).")

    # --- Regras para Ciência de Dados e Machine Learning ---
    @Rule(UserProfile(daily="analisar_dados"))
    def data_science_daily_preference(self):
        self.award("data_science", 6, "Preferência diária compatível: Ciência de Dados e Machine Learning (+6).")

    @Rule(UserProfile(value="insights_modelos"))
    def data_science_delivery_value(self):
        self.award("data_science", 5, "Tipo de entrega de valor compatível: Ciência de Dados e Machine Learning (+5).")

    @Rule(OR(UserProfile(stack="Python"), UserProfile(stack="SQL/BI")))
    def data_science_tool_affinity(self):
        self.award("data_science", 3, "Afinidade com ferramenta/tecnologia relevante para Ciência de Dados e Machine Learning (+3).")

    @Rule(UserProfile(daily="analisar_dados", value="insights_modelos"))
    def data_science_crossed_profile(self):
        self.award("data_science", 4, "Regra cruzada: preferência diária e entrega de valor apontam para Ciência de Dados e Machine Learning (+4).")

    @Rule(UserProfile(daily="analisar_dados", math="Alta"))
    def data_science_daily_math_cross(self):
        self.award("data_science", 2, "Regra cruzada: análise de dados combinada com afinidade matemática alta reforça Ciência de Dados (+2).")

    @Rule(UserProfile(math="Alta"))
    def data_science_math_affinity(self):
        self.award("data_science", 2, "Afinidade matemática alta compatível com Ciência de Dados e Machine Learning (+2).")

    # --- Regras para Engenharia de Dados ---
    @Rule(UserProfile(daily="pipelines_dados"))
    def data_engineering_daily_preference(self):
        self.award("data_engineering", 6, "Preferência diária compatível: Engenharia de Dados (+6).")

    @Rule(UserProfile(value="dados_confiaveis"))
    def data_engineering_delivery_value(self):
        self.award("data_engineering", 5, "Tipo de entrega de valor compatível: Engenharia de Dados (+5).")

    @Rule(OR(UserProfile(stack="SQL/BI"), UserProfile(stack="Python"), UserProfile(stack="Linux/Redes")))
    def data_engineering_tool_affinity(self):
        self.award("data_engineering", 3, "Afinidade com ferramenta/tecnologia relevante para Engenharia de Dados (+3).")

    @Rule(UserProfile(daily="pipelines_dados", value="dados_confiaveis"))
    def data_engineering_crossed_profile(self):
        self.award("data_engineering", 4, "Regra cruzada: preferência diária e entrega de valor apontam para Engenharia de Dados (+4).")

    @Rule(UserProfile(daily="pipelines_dados", stack="SQL/BI"))
    def data_engineering_pipeline_sql_cross(self):
        self.award("data_engineering", 2, "Regra cruzada: preferência por pipelines com afinidade por SQL/BI reforça Engenharia de Dados (+2).")

    @Rule(OR(UserProfile(math="Média"), UserProfile(math="Alta")))
    def data_engineering_math_affinity(self):
        self.award("data_engineering", 2, "Afinidade matemática média ou alta compatível com Engenharia de Dados (+2).")

    # --- Regras para Cibersegurança ---
    @Rule(UserProfile(daily="seguranca"))
    def security_daily_preference(self):
        self.award("security", 6, "Preferência diária compatível: Cibersegurança (+6).")

    @Rule(UserProfile(value="protecao"))
    def security_delivery_value(self):
        self.award("security", 5, "Tipo de entrega de valor compatível: Cibersegurança (+5).")

    @Rule(OR(UserProfile(stack="Linux/Redes"), UserProfile(stack="Python")))
    def security_tool_affinity(self):
        self.award("security", 3, "Afinidade com ferramenta/tecnologia relevante para Cibersegurança (+3).")

    @Rule(UserProfile(daily="seguranca", value="protecao"))
    def security_crossed_profile(self):
        self.award("security", 4, "Regra cruzada: preferência diária e entrega de valor apontam para Cibersegurança (+4).")

    @Rule(UserProfile(daily="seguranca", stack="Linux/Redes"))
    def security_networks_cross(self):
        self.award("security", 2, "Regra cruzada: interesse em segurança combinado com Linux/redes reforça Cibersegurança (+2).")

    @Rule(OR(UserProfile(math="Média"), UserProfile(math="Alta")))
    def security_math_affinity(self):
        self.award("security", 2, "Afinidade matemática média ou alta compatível com Cibersegurança (+2).")

    # --- Regras para DevOps & SRE ---
    @Rule(UserProfile(daily="automatizar_deploy"))
    def devops_daily_preference(self):
        self.award("devops", 6, "Preferência diária compatível: DevOps & SRE (+6).")

    @Rule(UserProfile(value="automacao_estabilidade"))
    def devops_delivery_value(self):
        self.award("devops", 5, "Tipo de entrega de valor compatível: DevOps & SRE (+5).")

    @Rule(OR(UserProfile(stack="Docker/Git/CI-CD"), UserProfile(stack="Linux/Redes")))
    def devops_tool_affinity(self):
        self.award("devops", 3, "Afinidade com ferramenta/tecnologia relevante para DevOps & SRE (+3).")

    @Rule(UserProfile(daily="automatizar_deploy", value="automacao_estabilidade"))
    def devops_crossed_profile(self):
        self.award("devops", 4, "Regra cruzada: preferência diária e entrega de valor apontam para DevOps & SRE (+4).")

    @Rule(UserProfile(daily="automatizar_deploy", stack="Docker/Git/CI-CD"))
    def devops_automation_stack_cross(self):
        self.award("devops", 2, "Regra cruzada: automação de entregas combinada com Docker/Git/CI-CD reforça DevOps & SRE (+2).")

    @Rule(OR(UserProfile(math="Média"), UserProfile(math="Alta")))
    def devops_math_affinity(self):
        self.award("devops", 2, "Afinidade matemática média ou alta compatível com DevOps & SRE (+2).")

    # --- Regras para Computação em Nuvem ---
    @Rule(UserProfile(daily="infraestrutura_cloud"))
    def cloud_daily_preference(self):
        self.award("cloud", 6, "Preferência diária compatível: Computação em Nuvem (+6).")

    @Rule(UserProfile(value="infraestrutura_escala"))
    def cloud_delivery_value(self):
        self.award("cloud", 5, "Tipo de entrega de valor compatível: Computação em Nuvem (+5).")

    @Rule(OR(UserProfile(stack="AWS/Azure/GCP"), UserProfile(stack="Docker/Git/CI-CD")))
    def cloud_tool_affinity(self):
        self.award("cloud", 3, "Afinidade com ferramenta/tecnologia relevante para Computação em Nuvem (+3).")

    @Rule(UserProfile(daily="infraestrutura_cloud", value="infraestrutura_escala"))
    def cloud_crossed_profile(self):
        self.award("cloud", 4, "Regra cruzada: preferência diária e entrega de valor apontam para Computação em Nuvem (+4).")

    @Rule(UserProfile(daily="infraestrutura_cloud", stack="AWS/Azure/GCP"))
    def cloud_infrastructure_stack_cross(self):
        self.award("cloud", 2, "Regra cruzada: interesse em infraestrutura combinado com afinidade por nuvem reforça Cloud Architecture (+2).")

    @Rule(OR(UserProfile(math="Média"), UserProfile(math="Alta")))
    def cloud_math_affinity(self):
        self.award("cloud", 2, "Afinidade matemática média ou alta compatível com Computação em Nuvem (+2).")

    # --- Regras para Desenvolvimento Mobile ---
    @Rule(UserProfile(daily="apps_mobile"))
    def mobile_daily_preference(self):
        self.award("mobile", 6, "Preferência diária compatível: Desenvolvimento Mobile (+6).")

    @Rule(UserProfile(value="app_mobile"))
    def mobile_delivery_value(self):
        self.award("mobile", 5, "Tipo de entrega de valor compatível: Desenvolvimento Mobile (+5).")

    @Rule(OR(UserProfile(stack="Flutter/Kotlin/Swift"), UserProfile(stack="JavaScript/TypeScript")))
    def mobile_tool_affinity(self):
        self.award("mobile", 3, "Afinidade com ferramenta/tecnologia relevante para Desenvolvimento Mobile (+3).")

    @Rule(UserProfile(daily="apps_mobile", value="app_mobile"))
    def mobile_crossed_profile(self):
        self.award("mobile", 4, "Regra cruzada: preferência diária e entrega de valor apontam para Desenvolvimento Mobile (+4).")

    @Rule(UserProfile(math="Baixa"))
    def mobile_math_affinity(self):
        self.award("mobile", 2, "Afinidade matemática baixa compatível com Desenvolvimento Mobile (+2).")

    # --- Regras para Engenharia de Qualidade e Testes (QA) ---
    @Rule(UserProfile(daily="testar_qualidade"))
    def qa_daily_preference(self):
        self.award("qa", 6, "Preferência diária compatível: Engenharia de Qualidade e Testes (QA) (+6).")

    @Rule(UserProfile(value="confiabilidade"))
    def qa_delivery_value(self):
        self.award("qa", 5, "Tipo de entrega de valor compatível: Engenharia de Qualidade e Testes (QA) (+5).")

    @Rule(OR(UserProfile(stack="Ferramentas de testes automatizados"), UserProfile(stack="Python"), UserProfile(stack="JavaScript/TypeScript")))
    def qa_tool_affinity(self):
        self.award("qa", 3, "Afinidade com ferramenta/tecnologia relevante para Engenharia de Qualidade e Testes (QA) (+3).")

    @Rule(UserProfile(daily="testar_qualidade", value="confiabilidade"))
    def qa_crossed_profile(self):
        self.award("qa", 4, "Regra cruzada: preferência diária e entrega de valor apontam para Engenharia de Qualidade e Testes (QA) (+4).")

    @Rule(OR(UserProfile(math="Média"), UserProfile(math="Alta")))
    def qa_math_affinity(self):
        self.award("qa", 2, "Afinidade matemática média ou alta compatível com Engenharia de Qualidade e Testes (QA) (+2).")

    # --- Regras para Gestão de Produtos ---
    @Rule(UserProfile(daily="produto_negocio"))
    def product_daily_preference(self):
        self.award("product", 6, "Preferência diária compatível: Gestão de Produtos (+6).")

    @Rule(UserProfile(value="estrategia_produto"))
    def product_delivery_value(self):
        self.award("product", 5, "Tipo de entrega de valor compatível: Gestão de Produtos (+5).")

    @Rule(OR(UserProfile(stack="Jira/Notion/Agile"), UserProfile(stack="Design/Figma")))
    def product_tool_affinity(self):
        self.award("product", 3, "Afinidade com ferramenta/tecnologia relevante para Gestão de Produtos (+3).")

    @Rule(UserProfile(daily="produto_negocio", value="estrategia_produto"))
    def product_crossed_profile(self):
        self.award("product", 4, "Regra cruzada: preferência diária e entrega de valor apontam para Gestão de Produtos (+4).")

    @Rule(OR(UserProfile(math="Baixa"), UserProfile(math="Média")))
    def product_math_affinity(self):
        self.award("product", 2, "Afinidade matemática baixa ou média compatível com Gestão de Produtos (+2).")


def recommend(profile):
    """Executa o motor e devolve recomendação, pontuação e justificativas.

    ``profile`` deve conter apenas math, daily, stack e value.
    """
    required = {"math", "daily", "stack", "value"}
    missing = required - set(profile)
    if missing:
        raise ValueError("Campos ausentes no perfil: " + ", ".join(sorted(missing)))

    engine = CareerAdvisor()
    engine.reset()
    engine.declare(UserProfile(**{key: profile[key] for key in required}))
    engine.run()

    best_score = max(engine.scores.values())
    finalists = [key for key, score in engine.scores.items() if score == best_score]
    tie_break = None

    # Desempate explícito
    for field, lookup, explanation in (
        ("daily", DAILY_TO_TRACK, "preferência diária"),
        ("value", VALUE_TO_TRACK, "tipo de entrega de valor"),
        ("stack", STACK_TO_TRACK, "ferramenta principal"),
    ):
        preferred = lookup.get(profile[field])
        if preferred in finalists:
            chosen = preferred
            tie_break = explanation if len(finalists) > 1 else None
            break
    else:
        chosen = sorted(finalists, key=lambda key: TRACKS[key]["tie_order"])[0]
        if len(finalists) > 1:
            tie_break = "ordem estável da matriz de decisão"

    score_table = sorted(
        ({"track_id": key, "name": TRACKS[key]["name"], "score": score}
         for key, score in engine.scores.items()),
        key=lambda item: (-item["score"], TRACKS[item["track_id"]]["tie_order"]),
    )

    return {
        "track_id": chosen,
        "track": TRACKS[chosen],
        "score": engine.scores[chosen],
        "evidence": sorted(engine.evidence[chosen], key=lambda item: -item["points"]),
        "all_scores": score_table,
        "tie_break": tie_break,
        "rules_fired": sum(len(items) for items in engine.evidence.values()),
    }