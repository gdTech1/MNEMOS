import requests
from .provider import LLMProvider

class OllamaProvider(LLMProvider):

    def __init__(
        self,
        model: str = "llama3",
        base_url: str = "http://localhost:11434",
    ):
        self.model = model
        self.base_url = base_url

    def generate(self, prompt: str):
        response = requests.post(
            f"{self.base_url}/api/generate",
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False,
            },
        )

        response.raise_for_status()

        return response.json()["response"]