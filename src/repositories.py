from typing import Protocol

from src.entities import Unity


class UnityRepository(Protocol):
    def register_unity():
        ...

    def count_occupied_unities(unity: Unity):
        ...
