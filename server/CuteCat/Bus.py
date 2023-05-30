from typing import Callable, List, Any
from collections import defaultdict
from .Utils import run_funcs

class EventBus:

    def __init__(self):
        self._subscribers = defaultdict(set)

    def subscribe(self, event: str, func: Callable) -> None:
        self._subscribers[event].add(func)

    def emit(self, event: str, *args, **kwargs) -> List[Any]:
        results = []
        results = run_funcs(self._subscribers[event], *args,**kwargs)
        return results