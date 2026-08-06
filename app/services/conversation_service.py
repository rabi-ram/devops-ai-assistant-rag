from collections import defaultdict
from typing import Dict, List


class ConversationService:
    """
    Stores conversation history in memory.

    Note:
    This is suitable for development and testing.
    In production, conversation history should be stored
    in Redis, PostgreSQL, DynamoDB, etc.
    """

    def __init__(self):

        self._conversations: Dict[str, List[dict]] = defaultdict(list)

        # Maximum number of user/assistant exchanges to keep
        self._max_messages = 10

    def add_user_message(
        self,
        conversation_id: str,
        message: str,
    ):

        self._conversations[conversation_id].append(
            {
                "role": "user",
                "content": message,
            }
        )

        self._trim(conversation_id)

    def add_assistant_message(
        self,
        conversation_id: str,
        message: str,
    ):

        self._conversations[conversation_id].append(
            {
                "role": "assistant",
                "content": message,
            }
        )

        self._trim(conversation_id)

    def get_history(
        self,
        conversation_id: str,
    ) -> List[dict]:

        return self._conversations[conversation_id]

    def clear(
        self,
        conversation_id: str,
    ):

        self._conversations.pop(conversation_id, None)

    def _trim(
        self,
        conversation_id: str,
    ):

        if len(self._conversations[conversation_id]) > self._max_messages:

            self._conversations[conversation_id] = (
                self._conversations[conversation_id][-self._max_messages:]
            )


conversation_service = ConversationService()
