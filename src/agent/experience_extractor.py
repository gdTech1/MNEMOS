from __future__ import annotations
import re
from ..memory.candidate import MemoryCandidate
from .conversation import Conversation, Message, MessageRole

class ExperienceExtractor:

    EXPERIENCE_PATTERNS = (
        r"\beu\s+(fiz|comecei|terminei|consegui|aprendi|estudei|descobri)\b",
        r"\bhoje\s+eu\b",
        r"\bontem\s+eu\b",
        r"\bestou\s+(estudando|aprendendo|tentando|trabalhando)\b",
    )

    DECISION_PATTERNS = (
        r"\bdecidi\b",
        r"\bvou\s+(começar|estudar|fazer|aprender|trabalhar)\b",
        r"\bpretendo\b",
        r"\bquero\s+(aprender|estudar|começar|trabalhar)\b",
    )

    PREFERENCE_PATTERNS = (
        r"\b(eu\s+)?(gosto|prefiro|adoro|odeio|detesto)\b",
    )

    CATEGORY_PATTERNS = {
        "experience": EXPERIENCE_PATTERNS,
        "decision": DECISION_PATTERNS,
        "preference": PREFERENCE_PATTERNS,
    }

    CATEGORY_IMPORTANCE = {
        "experience": 6,
        "decision": 8,
        "preference": 7,
    }

    CATEGORY_INTERPRETATION = {
        "experience": "User reported a personal experience.",
        "decision": "User reported a personal decision or intention.",
        "preference": "User expressed a personal preference.",
    }

    def extract(self, conversation: Conversation):
        candidates = []

        for message in conversation.get_messages():
            if message.role != MessageRole.USER:
                continue

            candidate = self._extract_from_message(message)

            if candidate is not None:
                candidates.append(candidate)

        return candidates

    def _extract_from_message(
        self,
        message: Message,
    ):
        category = self._classify(message.content)

        if category is None:
            return None

        return MemoryCandidate(
            content=message.content,
            importance=self.CATEGORY_IMPORTANCE[category],
            context=category,
            sentiment=None,
            interpretation=self.CATEGORY_INTERPRETATION[category],
            confidence=self._estimate_confidence(
                message.content,
                category,
            ),
            created_at=message.created_at,
        )

    def _classify(self, content: str):
        normalized = self._normalize(content)

        for category, patterns in self.CATEGORY_PATTERNS.items():
            if any(
                re.search(pattern, normalized)
                for pattern in patterns
            ):
                return category

        return None

    def _estimate_confidence(
        self,
        content: str,
        category: str,
    ):
        normalized = self._normalize(content)
        patterns = self.CATEGORY_PATTERNS[category]

        matches = sum(
            bool(re.search(pattern, normalized))
            for pattern in patterns
        )

        return min(0.5 + matches * 0.15, 1.0)

    @staticmethod
    def _normalize(content: str):
        return " ".join(content.lower().split())