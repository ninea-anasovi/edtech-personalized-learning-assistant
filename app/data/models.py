from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class Student:
    """
    A data class representing a student.
    """
    student_id: str
    performance_history: List[Dict[str, any]] = field(default_factory=list)

    def to_dict(self):
        """Converts the Student object to a dictionary."""
        return {
            "student_id": self.student_id,
            "performance_history": self.performance_history,
        }

    @staticmethod
    def from_dict(data: dict):
        """Creates a Student object from a dictionary."""
        return Student(
            student_id=data.get("student_id"),
            performance_history=data.get("performance_history", []),
        )