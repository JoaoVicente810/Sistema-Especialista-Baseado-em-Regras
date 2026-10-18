"""Validação da base de conhecimento com personas representativas."""
import ast
import unittest
from pathlib import Path

from expert_system import recommend


PERSONAS = {
    "cientista_de_dados": {
        "profile": {
            "math": "Alta",
            "daily": "analisar_dados",
            "stack": "Python",
            "value": "insights_modelos",
            "experience": "Intermediário",
            "goal": "investigacao",
        },
        "expected": "data_science",
    },
    "engenheiro_de_dados": {
        "profile": {
            "math": "Média",
            "daily": "pipelines_dados",
            "stack": "SQL/BI",
            "value": "dados_confiaveis",
            "experience": "Intermediário",
            "goal": "automacao",
        },
        "expected": "data_engineering",
    },
    "ciberseguranca": {
        "profile": {
            "math": "Média",
            "daily": "seguranca",
            "stack": "Linux/Redes",
            "value": "protecao",
            "experience": "Intermediário",
            "goal": "protecao",
        },
        "expected": "security",
    },
    "front_end_visual": {
        "profile": {
            "math": "Baixa",
            "daily": "interfaces_visuais",
            "stack": "JavaScript/TypeScript",
            "value": "experiencia_visual",
            "experience": "Iniciante",
            "goal": "criatividade",
        },
        "expected": "frontend",
    },
    "gestao_de_produtos": {
        "profile": {
            "math": "Média",
            "daily": "produto_negocio",
            "stack": "Jira/Notion/Agile",
            "value": "estrategia_produto",
            "experience": "Intermediário",
            "goal": "lideranca_estrategia",
        },
        "expected": "product",
    },
}


class TestCareerAdvisorPersonas(unittest.TestCase):
    def test_personas_receive_expected_recommendation(self):
        for name, case in PERSONAS.items():
            with self.subTest(persona=name):
                result = recommend(case["profile"])
                self.assertEqual(result["track_id"], case["expected"])
                self.assertGreater(result["score"], 0)
                self.assertTrue(result["evidence"])
                self.assertEqual(len(result["all_scores"]), 10)

    def test_data_science_and_data_engineering_are_distinguished(self):
        ds = recommend(PERSONAS["cientista_de_dados"]["profile"])
        de = recommend(PERSONAS["engenheiro_de_dados"]["profile"])
        self.assertEqual(ds["track_id"], "data_science")
        self.assertEqual(de["track_id"], "data_engineering")

    def test_knowledge_base_declares_at_least_25_rule_decorators(self):
        source_path = Path(__file__).resolve().parents[1] / "expert_system.py"
        syntax_tree = ast.parse(source_path.read_text(encoding="utf-8"))
        rule_count = sum(
            1
            for node in ast.walk(syntax_tree)
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
            for decorator in node.decorator_list
            if isinstance(decorator, ast.Call)
            and isinstance(decorator.func, ast.Name)
            and decorator.func.id == "Rule"
        )
        self.assertGreaterEqual(rule_count, 25)
        cross_rule_count = sum(
            1
            for node in ast.walk(syntax_tree)
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
            and "cross" in node.name
        )
        self.assertGreaterEqual(cross_rule_count, 25)

    def test_missing_field_is_rejected(self):
        with self.assertRaises(ValueError):
            recommend({"math": "Alta"})


if __name__ == "__main__":
    unittest.main(verbosity=2)
