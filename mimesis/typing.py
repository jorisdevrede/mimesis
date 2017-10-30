"""
This module is included built in and custom types for type hinting.
This is internal module and you shouldn't use it if you don't know
why you should.
"""
import datetime
from typing import (Any, Dict, List,
                    Union, MutableSequence)

__all__ = [
    'Array',
    'Gender',
    'JSON',
    'Size',
    'Bytes',
    'DateTime',
    'Timestamp',
]

JSON = Union[
    Dict[str, Any],
    Any,
]

_StrOrInt = Union[str, int]

# Gender can be int and str.
Gender = _StrOrInt

Size = _StrOrInt

Number = _StrOrInt

# Array (instance of array.array)
Array = Union[
    # can contain float and int.
    MutableSequence[float],
    MutableSequence[int],
    List[Union[int, float]],
]

# Bytes type
Bytes = bytes

DateTime = Union[datetime.datetime, Any]

Timestamp = _StrOrInt
