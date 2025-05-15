from LineStorage import LineStorage
from typing import List, Dict, Tuple

class QueryService:
    def __init__(self, repo: LineStorage, shift_map: Dict[str, Tuple[int, int]]):
        self._repo = repo
        self._map = shift_map
        
        
    def search(self, keyword: str) -> List[Dict[str, any]]:
        leader = keyword.lower() + " "

        hits = [
            {
                "line_id": self._map[s][0],
                "shift": s,
                "position": self._map[s][1]
            }
            for s in self._repo.iter_index()
            if s.lower().startswith(leader)
        ]
        return hits