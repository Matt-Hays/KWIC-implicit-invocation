from typing import List
from bisect import insort

class LineStorage:
    def __init__(self):
        self._lines: List[str] = []
        self._pending_shifts: List[str] = []
        self._index: List[str] = []
        
    def add_line(self, text: str) -> int:
        self._lines.append(text)
        return len(self._lines) - 1
    
    def add_shift(self, shift: str) -> None:
        self._pending_shifts.append(shift)
        
    def pop_pending_shift(self) -> str:
        return self._pending_shifts.pop()
    
    def has_pending_shifts(self) -> bool:
        return bool(self._pending_shifts)
    
    def insert_sorted(self, shift: str) -> None:
        insort(self._index, shift)
        
    def iter_index(self) -> List[str]:
        return list(self._index)