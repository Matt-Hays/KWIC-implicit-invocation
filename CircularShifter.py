from EventBus import EventBus
from LineStorage import LineStorage

class CircularShifter:
    def __init__(self, bus: EventBus, repo: LineStorage) -> None:
        self._bus, self._repo = bus, repo
        bus.subscribe("line_added", self._on_line_added)
        
    def _on_line_added(self, line_id: int, text: str) -> None:
        words = text.split()
        for i in range(len(words)):
            shifted = " ".join(words[i:] + words[:i])
            self._repo.add_shift(shifted)
        self._bus.publish("shifts_ready")