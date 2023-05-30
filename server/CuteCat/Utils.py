from typing import Any, Callable, Awaitable, Iterable, List

def run_funcs(funcs: Iterable[Callable[..., Awaitable[Any]]], *args,
                          **kwargs) -> List[Any]:
    """
    同时运行多个异步函数，并等待所有函数运行完成，返回运行结果列表。
    """
    results = []
    for f in funcs:
        results.append(f(*args, **kwargs))
    return results