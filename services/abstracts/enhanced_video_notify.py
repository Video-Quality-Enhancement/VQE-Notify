from abc import ABC, abstractmethod
from models import EnhancedVideoNotifyRequest

class EnhancedVideoNotify(ABC):

    @abstractmethod
    def notify(self, notify_request: EnhancedVideoNotifyRequest):
        pass

