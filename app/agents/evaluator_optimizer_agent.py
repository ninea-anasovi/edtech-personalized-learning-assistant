from app.agents.base_agent import BaseAgent
from app.core.gemini_client import GeminiClient

class EvaluatorOptimizerAgent(BaseAgent):
    """
    An agent that uses the Evaluator-Optimizer pattern to generate and refine content.
    - The generator creates the initial content.
    - The evaluator critiques the content against predefined criteria.
    - The optimizer refines the content based on the feedback.
    This iterative process continues until the content meets the desired quality.
    """

    def __init__(self):
        self.generator = GeminiClient()
        self.evaluator = GeminiClient()
        self.optimizer = GeminiClient()

    def execute(self, topic: str, max_iterations: int = 3):
        """
        Generates and refines content for a given topic.

        Args:
            topic (str): The topic to generate content for.
            max_iterations (int): The maximum number of refinement iterations.

        Returns:
            str: The refined content.
        """
        # 1. Generate initial content
        generation_prompt = f"Generate a short quiz on the topic: {topic}"
        content = self.generator.generate_text(generation_prompt)

        for i in range(max_iterations):
            # 2. Evaluate the content
            evaluation_prompt = f"Evaluate the following quiz for clarity, accuracy, and engagement for a high school student. Provide specific feedback for improvement.\n\nQuiz:\n{content}"
            feedback = self.evaluator.generate_text(evaluation_prompt)

            # 3. Decide if refinement is needed
            decision_prompt = f"Based on the following feedback, does the quiz need improvement? Answer with 'yes' or 'no'.\n\nFeedback:\n{feedback}"
            decision = self.optimizer.generate_text(decision_prompt).strip().lower()

            if 'no' in decision:
                break

            # 4. Optimize the content based on feedback
            optimization_prompt = f"Based on the following feedback, revise the quiz to improve it.\n\nFeedback:\n{feedback}\n\nOriginal Quiz:\n{content}"
            content = self.optimizer.generate_text(optimization_prompt)

        return content