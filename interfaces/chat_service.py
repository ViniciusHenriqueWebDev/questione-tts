from abc import ABC, abstractmethod

class ChatService(ABC):
    @abstractmethod
    def get_response(self, user_input: str) -> str:
        pass
