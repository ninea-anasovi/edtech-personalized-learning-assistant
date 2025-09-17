import unittest
from app.data.models import Student

class TestModels(unittest.TestCase):

    def test_student_model(self):
        student = Student(student_id="test_id", performance_history=[{"topic": "Science", "score": 0.9}])
        self.assertEqual(student.student_id, "test_id")
        self.assertEqual(len(student.performance_history), 1)
        self.assertEqual(student.to_dict(), {
            "student_id": "test_id",
            "performance_history": [{"topic": "Science", "score": 0.9}]
        })

if __name__ == '__main__':
    unittest.main()