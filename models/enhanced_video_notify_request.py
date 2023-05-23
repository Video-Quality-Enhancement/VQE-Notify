import json

class EnhancedVideoNotifyRequest:

    def __init__(self, userId: str, requestId: str, enhancedVideoUrl: str, status: str):
        self.userId = userId
        self.requestId = requestId
        self.enhancedVideoUrl = enhancedVideoUrl
        self.status = status

    def __str__(self):
        return f"EnhancedVideoNotifyRequest({self.__dict__})"

    def loads(cls, bytes):
        d = json.loads(bytes)
        return cls(**d)