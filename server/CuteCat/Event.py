from typing import Dict, Any, Optional


class Event(dict):
    @staticmethod
    def from_payload(payload: Dict[str, Any]) -> 'Optional[Event]':
        e = Event(payload)
        return e

    @property
    def type(self) -> str:
        """
        事件类型
        """
        return self['event']


    success         : bool
    message         : str
    robot_wxid      : str
    robot_name      : Optional[str]
    type            : int
    from_wxid       : Optional[str]
    from_name       : Optional[str]
    to_wxid         : Optional[str]
    member_wxid     : Optional[str]
    member_name     : Optional[str]
    final_from_wxid : Optional[str]
    group_wxid      : Optional[str]
    to_wxid         : Optional[str]
    money           : Optional[float]

    def __getattr__(self, key) -> Optional[Any]:
        return self.get(key)

    def __setattr__(self, key, value) -> None:
        self[key] = value

    def __repr__(self) -> str:
        return super().__repr__()