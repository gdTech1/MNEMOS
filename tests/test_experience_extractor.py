from datetime import datetime, timezone

from src.agent.conversation import Conversation, MessageRole
from src.agent.experience_extractor import ExperienceExtractor


def test_extract_experience():
    conversation = Conversation()
    conversation.add_message(
        MessageRole.USER,
        "Eu comecei a estudar Java."
    )

    extractor = ExperienceExtractor()
    candidates = extractor.extract(conversation)

    assert len(candidates) == 1
    assert candidates[0].content == "Eu comecei a estudar Java."
    assert candidates[0].context == "experience"
    assert candidates[0].importance == 6
    assert candidates[0].confidence > 0


def test_extract_decision():
    conversation = Conversation()
    conversation.add_message(
        MessageRole.USER,
        "Decidi estudar inteligência artificial."
    )

    extractor = ExperienceExtractor()
    candidates = extractor.extract(conversation)

    assert len(candidates) == 1
    assert candidates[0].context == "decision"
    assert candidates[0].importance == 8


def test_extract_preference():
    conversation = Conversation()
    conversation.add_message(
        MessageRole.USER,
        "Eu prefiro Python para projetos de IA."
    )

    extractor = ExperienceExtractor()
    candidates = extractor.extract(conversation)

    assert len(candidates) == 1
    assert candidates[0].context == "preference"
    assert candidates[0].importance == 7


def test_ignore_irrelevant_message():
    conversation = Conversation()
    conversation.add_message(
        MessageRole.USER,
        "Qual é a diferença entre Java e Python?"
    )

    extractor = ExperienceExtractor()
    candidates = extractor.extract(conversation)

    assert candidates == []


def test_ignore_assistant_messages():
    conversation = Conversation()
    conversation.add_message(
        MessageRole.ASSISTANT,
        "Eu comecei a estudar Java."
    )

    extractor = ExperienceExtractor()
    candidates = extractor.extract(conversation)

    assert candidates == []


def test_extract_multiple_candidates():
    conversation = Conversation()
    conversation.add_message(
        MessageRole.USER,
        "Eu comecei a estudar Java."
    )
    conversation.add_message(
        MessageRole.USER,
        "Decidi aprender machine learning."
    )
    conversation.add_message(
        MessageRole.USER,
        "Eu prefiro Python."
    )

    extractor = ExperienceExtractor()
    candidates = extractor.extract(conversation)

    assert len(candidates) == 3
    assert candidates[0].context == "experience"
    assert candidates[1].context == "decision"
    assert candidates[2].context == "preference"


def test_candidate_preserves_message_timestamp():
    created_at = datetime(
        2026,
        9,
        10,
        15,
        0,
        tzinfo=timezone.utc,
    )

    conversation = Conversation()
    message = conversation.add_message(
        MessageRole.USER,
        "Hoje eu comecei um novo projeto.",
    )
    message.created_at = created_at

    extractor = ExperienceExtractor()
    candidates = extractor.extract(conversation)

    assert candidates[0].created_at == created_at


def test_candidate_contains_interpretation():
    conversation = Conversation()
    conversation.add_message(
        MessageRole.USER,
        "Eu terminei meu projeto."
    )

    extractor = ExperienceExtractor()
    candidates = extractor.extract(conversation)

    assert candidates[0].interpretation == (
        "User reported a personal experience."
    )


def test_candidate_confidence_is_valid():
    conversation = Conversation()
    conversation.add_message(
        MessageRole.USER,
        "Eu comecei a estudar Java e hoje eu estou aprendendo muito."
    )

    extractor = ExperienceExtractor()
    candidates = extractor.extract(conversation)

    assert 0.0 <= candidates[0].confidence <= 1.0
    
def test_candidate_has_unknown_sentiment_when_not_detected():
    conversation = Conversation()
    conversation.add_message(
        MessageRole.USER,
        "Eu comecei a estudar Java."
    )

    extractor = ExperienceExtractor()
    candidates = extractor.extract(conversation)

    assert candidates[0].sentiment is None