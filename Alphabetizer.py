from EventBus import EventBus
from LineStorage import LineStorage


class Alphabetizer:
    def __init__(self, bus: EventBus, repo: LineStorage):
        self._bus, self._repo = bus, repo
        bus.subscribe("shifts_ready", self._on_shifts_ready)

    def _on_shifts_ready(self) -> None:
        while self._repo.has_pending_shifts():
            self._repo.insert_sorted(self._repo.pop_pending_shift())
        self._bus.publish("index_updated")
