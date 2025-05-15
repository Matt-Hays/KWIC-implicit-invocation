from EventBus import EventBus
from LineStorage import LineStorage


class IndexPrinter:
    def __init__(self, bus: EventBus, repo: LineStorage) -> None:
        self._repo = repo
        bus.subscribe("index_updated", self._print)

    def _print(self) -> None:
        print("\nKWIC INDEX")
        for s in self._repo.iter_index():
            print(s)
