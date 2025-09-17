from app.agents.base_agent import BaseAgent
from app.data.firestore_client import FirestoreDB
from app.core.gemini_client import GeminiClient
from app.data.models import Student

class MemoryAugmentedAgent(BaseAgent):
    """
    An agent that retains and utilizes student performance history to personalize recommendations.
    This agent demonstrates memory management by interacting with a Firestore database.
    """

    def __init__(self, student_id: str):
        self.student_id = student_id
        self.db = FirestoreDB.get_instance()
        self.llm = GeminiClient()
        self.student = self._load_student_data()

    def _load_student_data(self):
        """Loads student data from Firestore."""
        student_data = self.db.get_document('students', self.student_id)
        if student_data:
            return Student.from_dict(student_data)
        return Student(student_id=self.student_id)

    def update_performance(self, topic: str, score: float):
        """
        Updates the student's performance history.

        Args:
            topic (str): The topic of the quiz or activity.
            score (float): The score the student achieved.
        """
        self.student.performance_history.append({"topic": topic, "score": score})
        self.db.set_document('students', self.student_id, self.student.to_dict())

    def execute(self):
        """
        Generates personalized learning recommendations based on performance history.

        Returns:
            str: A personalized learning recommendation.
        """
        performance_summary = "\n".join([f"- Topic: {entry['topic']}, Score: {entry['score']}" for entry in self.student.performance_history])

        prompt = f"""
        Based on the following student performance history, generate a personalized learning recommendation.
        The recommendation should suggest the next topic to focus on and provide a brief rationale.

        Performance History:
        {performance_summary}
        """

        recommendation = self.llm.generate_text(prompt)
        return recommendation