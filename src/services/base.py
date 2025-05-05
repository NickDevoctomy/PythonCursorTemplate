from abc import ABC, abstractmethod
from typing import Dict, Any

class ChatService(ABC):
    """Base class for all chat services."""
    
    @property
    @abstractmethod
    def name(self) -> str:
        """Return the name of the service."""
        pass
    
    @property
    @abstractmethod
    def description(self) -> str:
        """Return a description of the service."""
        pass
    
    @abstractmethod
    async def send_message(self, message: str) -> str:
        """Send a message to the service and return the response."""
        pass 