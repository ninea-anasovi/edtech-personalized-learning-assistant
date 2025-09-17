import google.generativeai as genai
import os

class GeminiClient:
    """A client for interacting with the Gemini API."""

    def __init__(self):
        # Configure the Gemini API key
        genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel('gemini-pro')

    def generate_text(self, prompt: str) -> str:
        """
        Generates text using the Gemini model.

        Args:
            prompt (str): The prompt to send to the model.

        Returns:
            str: The generated text.
        """
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"An error occurred: {e}")
            return "Error generating content."