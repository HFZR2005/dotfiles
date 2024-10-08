from typing import Any, NamedTuple

class _Event(NamedTuple):
    when: Any
    callback: Any
    args: Any
    kwargs: Any

class EventLoop:
    current: Any
    idlers: Any
    inactive: int
    queue: Any
    rpcs: Any
    rpc_results: Any
    def __init__(self) -> None: ...
    def clear(self) -> None: ...
    def insort_event_right(self, event) -> None: ...
    def call_soon(self, callback, *args, **kwargs) -> None: ...
    def queue_call(self, delay, callback, *args, **kwargs) -> None: ...
    def queue_rpc(self, rpc, callback) -> None: ...
    def add_idle(self, callback, *args, **kwargs) -> None: ...
    def run_idle(self): ...
    def run0(self): ...
    def run1(self): ...
    def run(self) -> None: ...
