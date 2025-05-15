from EventBus import EventBus
from LineStorage import LineStorage
from CircularShifter import CircularShifter
from Alphabetizer import Alphabetizer
from IndexPrinter import IndexPrinter
# from QueryService import QueryService
# from typing import List


class KWICApp:
    def __init__(self):
        self._bus = EventBus() # Event processor
        self._repo = LineStorage() # Shared data storage
        self._shifter = CircularShifter(self._bus, self._repo)
        Alphabetizer(self._bus, self._repo)
        IndexPrinter(self._bus, self._repo)
        # self._query = QueryService(self._repo, self._shifter.shift_map)
        
    def add_line(self, text: str) -> None:
        line_id = self._repo.add_line(text)
        self._bus.publish("line_added", line_id=line_id, text=text)
        
    # def find(self, keyword: str) -> List[str]:
    #     return self._query.search(keyword)
