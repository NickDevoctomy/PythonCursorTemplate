from .base import ChatService

class EchoService(ChatService):
    """A simple echo service that returns the same message it receives."""
    
    @property
    def name(self) -> str:
        return "Echo"
    
    @property
    def description(self) -> str:
        return "Echoes back whatever message you send"
    
    async def send_message(self, message: str) -> str:
        return message 