from typing import Dict, List, Callable, Any
from pydantic import BaseModel, Field
import uuid
import time

class WebhookEvent(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    topic: str
    payload: Dict[str, Any]
    timestamp: float = Field(default_factory=time.time)

class MicroserviceEventBus:
    def __init__(self):
        self._subscribers: Dict[str, List[Callable[[WebhookEvent], None]]] = {}
        self._history: List[WebhookEvent] = []

    def subscribe(self, topic: str, handler: Callable[[WebhookEvent], None]) -> None:
        if not topic:
            raise ValueError("Topic cannot be empty")
        if topic not in self._subscribers:
            self._subscribers[topic] = []
        self._subscribers[topic].append(handler)

    def publish(self, event: WebhookEvent) -> int:
        handlers = self._subscribers.get(event.topic, [])
        for handler in handlers:
            handler(event)
        self._history.append(event)
        return len(handlers)

    def get_history(self, topic: str = None) -> List[WebhookEvent]:
        if topic:
            return [e for e in self._history if e.topic == topic]
        return list(self._history)
