from typing import List, Callable, Dict
from collections import defaultdict


class EventBus:
    def __init__(self):
        self._subscribers: Dict[str, List[Callable]] = defaultdict(list)

    def subscribe(self, event: str, handler: Callable):
        self._subscribers[event].append(handler)

    def unsubscribe(self, event: str, handler: Callable):
        if event in self._subscribers:
            self._subscribers[event].remove(handler)

    def publish(self, event: str, **payload):
        for handler in list(self._subscribers.get(event, [])):
            handler(**payload)
