import unittest
from unittest.mock import patch
from app.agents.evaluator_optimizer_agent import EvaluatorOptimizerAgent
from app.agents.memory_augmented_agent import MemoryAugmentedAgent

class TestAgents(unittest.TestCase):

    @patch('app.core.gemini_client.GeminiClient.generate_text')
    def test_evaluator_optimizer_agent(self, mock_generate_text):
        # Mock the responses from the Gemini client
        mock_generate_text.side_effect = [
            "Initial quiz content",  # Generator
            "This quiz is good.",   # Evaluator
            "no"                     # Decision
        ]
        agent = EvaluatorOptimizerAgent()
        result = agent.execute("History")
        self.assertEqual(result, "Initial quiz content")

    @patch('app.data.firestore_client.FirestoreDB.get_document')
    @patch('app.data.firestore_client.FirestoreDB.set_document')
    @patch('app.core.gemini_client.GeminiClient.generate_text')
    def test_memory_augmented_agent(self, mock_generate_text, mock_set_document, mock_get_document):
        # Mock the data returned from Firestore
        mock_get_document.return_value = {
            "student_id": "test_student",
            "performance_history": [{"topic": "Math", "score": 0.8}]
        }
        mock_generate_text.return_value = "Recommendation: Focus on Algebra."

        agent = MemoryAugmentedAgent("test_student")
        recommendation = agent.execute()

        self.assertEqual(recommendation, "Recommendation: Focus on Algebra.")
        mock_set_document.assert_not_called()

if __name__ == '__main__':
    unittest.main()