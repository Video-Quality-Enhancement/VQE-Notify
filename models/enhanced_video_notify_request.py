import json

class EnhancedVideoNotifyRequest:

    def __init__(self, userId: str, requestId: str, enhancedVideoUrl: str, enhancedVideoQuality: str, status: str, fcmTokens: list = []):
        self.userId = userId
        self.requestId = requestId
        self.enhancedVideoUrl = enhancedVideoUrl
        self.enhancedVideoQuality = enhancedVideoQuality
        self.status = status
        self.fcmTokens = fcmTokens

    def __str__(self):
        return f"EnhancedVideoNotifyRequest({self.__dict__})"

    @classmethod
    def loads(cls, bytes):
        d = json.loads(bytes)
        return cls(**d)