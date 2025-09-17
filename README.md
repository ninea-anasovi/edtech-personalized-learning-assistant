# EdTech Personalized Learning Assistant

This project is an AI-powered tutor that adapts to student progress, generates quizzes, and recommends learning materials.

## Features

- **Adaptive Learning Paths**: Utilizes Gemini's reasoning capabilities to create personalized learning journeys.
- **Dynamic Quiz Generation**: The Evaluator-Optimizer agent generates and refines quizzes.
- **Personalized Recommendations**: The Memory-Augmented agent uses student performance history to suggest relevant learning materials.
- **Secure Data Storage**: Student data is stored in Firestore with strict access controls.

## Agentic Patterns

- **Evaluator-Optimizer Pattern**: An evaluator agent critiques generated content (like quizzes) and an optimizer agent iteratively improves it.
- **Memory-Augmented Agent**: Retains student performance history in Firestore to personalize future recommendations.

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ninea-anasovi/edtech-personalized-learning-assistant.git
   cd edtech-personalized-learning-assistant
   ```
2. **Install the dependencies:**

```
pip install -r requirements.txt
```

3. **Set up your environment variables:**

Create a .env file in the root directory and add the following:

```
GEMINI_API_KEY="your_gemini_api_key"
```

4. **Set up Firebase Authentication:**

Follow the Firebase documentation to set up Application Default Credentials.
Run the application:
```aiignore
python -m app.main
```

