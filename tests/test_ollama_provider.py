from unittest.mock import Mock, patch

import pytest

from src.intelligence.ollama_provider import OllamaProvider


def test_generate_returns_model_response():
    provider = OllamaProvider()

    mock_response = Mock()
    mock_response.json.return_value = {
        "response": "Memory stores information for later retrieval."
    }

    with patch("src.intelligence.ollama_provider.requests.post") as mock_post:
        mock_post.return_value = mock_response

        response = provider.generate("What is memory?")

    assert response == "Memory stores information for later retrieval."


def test_generate_sends_correct_request():
    provider = OllamaProvider(
        model="llama3",
        base_url="http://localhost:11434",
    )

    mock_response = Mock()
    mock_response.json.return_value = {
        "response": "response"
    }

    with patch("src.intelligence.ollama_provider.requests.post") as mock_post:
        mock_post.return_value = mock_response

        provider.generate("Test prompt")

    mock_post.assert_called_once_with(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": "Test prompt",
            "stream": False,
        },
    )


def test_generate_raises_for_http_error():
    provider = OllamaProvider()

    mock_response = Mock()
    mock_response.raise_for_status.side_effect = Exception("HTTP error")

    with patch("src.intelligence.ollama_provider.requests.post") as mock_post:
        mock_post.return_value = mock_response

        with pytest.raises(Exception, match="HTTP error"):
            provider.generate("Test prompt")