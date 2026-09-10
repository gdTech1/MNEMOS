from src.agent.conversation import Conversation, MessageRole

def test_create_conversation():
    conversation = Conversation()

    assert conversation.id is not None
    assert conversation.messages == []
    assert len(conversation) == 0

def test_add_message():
    conversation = Conversation()

    message = conversation.add_message(
        MessageRole.USER,
        "I started studying Java.",
    )

    assert message.role == MessageRole.USER
    assert message.content == "I started studying Java."
    assert message.id is not None
    assert len(conversation) == 1

def test_add_multiple_messages():
    conversation = Conversation()

    conversation.add_message(
        MessageRole.USER,
        "I started studying Java.",
    )

    conversation.add_message(
        MessageRole.ASSISTANT,
        "That's great.",
    )

    assert len(conversation) == 2
    assert conversation.messages[0].role == MessageRole.USER
    assert conversation.messages[1].role == MessageRole.ASSISTANT

def test_get_messages_returns_copy():
    conversation = Conversation()

    conversation.add_message(
        MessageRole.USER,
        "Hello.",
    )

    messages = conversation.get_messages()
    messages.clear()

    assert len(conversation) == 1

def test_get_last_message():
    conversation = Conversation()

    conversation.add_message(
        MessageRole.USER,
        "First message.",
    )

    last_message = conversation.add_message(
        MessageRole.USER,
        "Last message.",
    )

    assert conversation.get_last_message() == last_message

def test_get_last_message_returns_none_when_empty():
    conversation = Conversation()

    assert conversation.get_last_message() is None

def test_message_rejects_empty_content():
    try:
        conversation = Conversation()
        conversation.add_message(MessageRole.USER, "")
        assert False
    except ValueError:
        assert True