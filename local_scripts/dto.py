#!/usr/bin/env python
from typing import NamedTuple


class CommandDTO(NamedTuple):
    """DTO cmd - команда, exit_code - код выполнения команды"""

    cmd: str
    exit_code: str