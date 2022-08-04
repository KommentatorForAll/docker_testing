import inspect
from typing import List, TypeVar, Tuple, Type, Callable

C = TypeVar("C", type, Tuple[type])

_notice_me_obj_cache = []
_notice_me_call_cache = {}
_notice_me_add_on_obj_init = []
_notice_me_missing_classes = {}


def notice_me(cls: C) -> C:
    try:
        _notice_me_obj_cache.append(cls())
    except TypeError:
        _notice_me_add_on_obj_init.append(cls)

    class NoticeMe(cls):
        def __init__(self, *args, **kwargs):
            super(NoticeMe, self).__init__(*args, **kwargs)
            if cls in _notice_me_add_on_obj_init:
                _notice_me_add_on_obj_init.remove(cls)
                _notice_me_obj_cache.append(self)

    return NoticeMe


def get_instances(cls: Type[C]) -> List[C]:
    if not inspect.isclass(cls):
        raise TypeError("cls must be of type Class")
    if cls not in _notice_me_call_cache.keys():
        result = []
        for obj in _notice_me_obj_cache:
            if isinstance(obj, cls):
                result.append(obj)
        _notice_me_call_cache[cls] = result
    return _notice_me_call_cache.get(cls)
