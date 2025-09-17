# Personad AdTech Learning Assistent


### Agentic Patterns

-   **Evaluator-Optimizer Pattern**: This pattern involves two distinct agent roles. An `Evaluator` agent assesses the quality of generated content (e.g., a quiz) against a set of predefined criteria (e.g., clarity, accuracy, difficulty). An `Optimizer` agent then takes the evaluator's feedback to refine and improve the content. This iterative loop ensures the final output is of high quality.
-   **Memory-Augmented Agent**: This agent is designed with both short-term and long-term memory capabilities. It maintains a persistent memory of each student's interactions and performance history by interfacing with Firestore. This long-term memory is crucial for personalizing future recommendations and adapting the learning path over time.

## Getting Started

Follow these steps to set up the project locally.

### Prerequisites

-   Python 3.9+
-   A Google Cloud Platform (GCP) project with Firestore enabled.
-   `gcloud` CLI installed and authenticated.
-   An API key for the Gemini API.

### Installation

1.  **Clone the Repository**
    ```sh
    git clone https://github.com/ninea-anasovi/edtech-personalized-learning-assistant.git
    cd edtech-personalized-learning-assistant
    ```

2.  **Create and Activate a Virtual Environment**
    ```sh
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install Dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Set Up Environment Variables**
    Create a `.env` file in the root directory and add your credentials:
    ```env
    GEMINI_API_KEY="your_gemini_api_key"
    FIREBASE_PROJECT_ID="your_firebase_project_id"
    ```

5.  **Set Up Firebase Authentication**
    Authenticate the Google Cloud CLI to allow the application to access Firestore.
    ```sh
    gcloud auth application-default login
    ```

6.  **Run the Application**
    ```sh
    python -m app.main
    ```
    The application will be available at `http://127.0.0.1:5000`.

## Usage

The web interface provides two main functionalities:

1.  **Generate a Quiz**: Enter a topic (e.g., "World War II"), and the Evaluator-Optimizer agent will generate a refined quiz on that subject.
2.  **Get Learning Recommendation**: Enter a student ID, and the Memory-Augmented agent will analyze the student's history to provide a personalized recommendation for their next learning step.

## Ethical Data Handling

This project is committed to the highest standards of ethical data handling and responsible AI.

-   **Data Privacy**: All student data is securely stored in Firestore, which provides robust security rules to prevent unauthorized access.
-   **Purpose Limitation**: Data is used exclusively for the purpose of personalizing the learning experience and is never shared with third parties.
-   **Transparency**: The system's logic for generating recommendations is designed to be as transparent as possible, ensuring that the educational goals remain the primary focus.

## Roadmap

-   [ ] Implement user authentication and profiles.
-   [ ] Expand content generation to include lesson plans and summaries.
-   [ ] Add support for different languages.
-   [ ] Develop a more sophisticated front-end with interactive elements.
-   [ ] Integrate with other educational platforms and APIs.

See the [open issues](https://github.com/ninea-anasovi/edtech-personalized-learning-assistant/issues) for a full list of proposed features (and known issues).

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## Contact

Ninea Anasovi - ninea.anasovi@gmail.com

Project Link: [https://github.com/ninea-anasovi/edtech-personalized-learning-assistant](https://github.com/ninea-anasovi/edtech-personalized-learning-assistant)