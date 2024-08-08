import os
import requests
from interfaces.tts_service import TextToSpeechService

class AzureTTSService(TextToSpeechService):
    def __init__(self):
        self.subscription_key = os.getenv("AZURE_TTS_KEY")
        self.endpoint = os.getenv("AZURE_TTS_ENDPOINT")

    def convert_text_to_speech(self, text: str) -> bytes:
        headers = {
            "Ocp-Apim-Subscription-Key": self.subscription_key,
            "Content-Type": "application/ssml+xml",
            "X-Microsoft-OutputFormat": "riff-24khz-16bit-mono-pcm",
        }

        body = f"""
        <speak version='1.0' xml:lang='en-US'>
            <voice xml:lang='en-US' xml:gender='Female' name='en-US-JessaRUS'>
                {text}
            </voice>
        </speak>
        """

        response = requests.post(f"{self.endpoint}/cognitiveservices/v1", headers=headers, data=body)
        
        if response.status_code == 200:
            return response.content
        else:
            raise Exception(f"Erro ao obter resposta TTS: {response.status_code}, {response.text}")
