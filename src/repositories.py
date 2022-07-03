from typing import Protocol

from src.domain.entities import Unity


class UnityRepository(Protocol):
    def register_unity():
        ...

    def count_occupied_unities(unity: Unity):
        ...
