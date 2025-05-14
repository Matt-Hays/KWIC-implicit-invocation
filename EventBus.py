from typing import List, Callable, Dict
from collections import defaultdict

class EventBus:
    def __init__(self):
        self._subscribers: Dict[str, List[Callable]] = defaultdict(list)
        
    def subscribe(self, event: str, handler: Callable):
        self._subscribers[event].append(handler)
        
    def publish(self, event:str, **kwargs):
        for handler in list(self._subscribers.get(event, [])):
            handler(**kwargs)