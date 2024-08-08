from interfaces.chat_service import ChatService

class ChatGPTService(ChatService):
    def get_response(self, user_input: str) -> str:
        # Simulação de resposta do ChatGPT
        return "Estou bem, obrigado por perguntar!"
