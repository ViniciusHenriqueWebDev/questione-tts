from abc import ABC, abstractmethod

class TextToSpeechService(ABC):
    @abstractmethod
    def convert_text_to_speech(self, text: str) -> bytes:
        pass
