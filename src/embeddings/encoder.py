from __future__ import annotations
from sentence_transformers import SentenceTransformer

DEFAULT_MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

class EmbeddingEncoder:
    def __init__(self, model_name: str = DEFAULT_MODEL_NAME):
        self.model_name = model_name
        self._model: SentenceTransformer | None = None

    @property
    def model(self):
        if self._model is None:
            self._model = SentenceTransformer(self.model_name)
        return self._model

    def encode(self, text: str):
        return self.model.encode(text, convert_to_numpy=True).tolist()

    def encode_many(self, texts: list[str]):
        embeddings = self.model.encode(texts, convert_to_numpy=True)
        return embeddings.tolist()