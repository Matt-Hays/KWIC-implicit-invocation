from EventBus import EventBus
from LineStorage import LineStorage
from CircularShifter import CircularShifter
from Alphabetizer import Alphabetizer
from IndexPrinter import IndexPrinter

class KWICApp:
    def __init__(self):
        self._bus = EventBus()
        self._repo = LineStorage()
        
        CircularShifter(self._bus, self._repo)
        Alphabetizer(self._bus, self._repo)
        IndexPrinter(self._bus, self._repo)
        
    def add_line(self, text: str) -> None:
        line_id = self._repo.add_line(text)
        self._bus.publish("line_added", line_id=line_id, text=text)
        