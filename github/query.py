from enum import Enum


class QueryItemType(Enum):
    LANGUAGE = "language"
    LOCATION = "location"
    REPOS = "repos"
    KIND = "type"


class QueryItem:
    def __init__(self, item_type: QueryItemType, value: str) -> None:
        self._type = item_type
        self._value = value.lower()

    def __str__(self) -> str:
        return f"{self._type.value}:{self._value}"

    @staticmethod
    def bulk_create(item_type: QueryItemType, values: list[str]) -> list["QueryItem"]:
        return [QueryItem(item_type, value) for value in values]


class Query:
    def __init__(self, *args) -> None:
        self._items: list[QueryItem] = args

    def __str__(self) -> str:
        return "+".join(str(item) for item in self._items)
