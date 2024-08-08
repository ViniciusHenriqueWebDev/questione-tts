from services.chatgpt_service import ChatGPTService
from services.azure_tts_service import AzureTTSService

def main():
    chat_service = ChatGPTService()
    tts_service = AzureTTSService()

    user_input = "Olá, como você está?"
    chat_response = chat_service.get_response(user_input)
    audio_content = tts_service.convert_text_to_speech(chat_response)

    with open("response_audio.wav", "wb") as audio_file:
        audio_file.write(audio_content)

    print("Resposta em áudio gerada com sucesso!")

if __name__ == "__main__":
    main()
