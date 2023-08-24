import os
import requests

from github.user import User
from github.query import Query
from github.exceptions import SearchUserException, GetUserInfoException


class APIClient:
    GITHUB_BASE_URL = "https://api.github.com"

    def __init__(self) -> None:
        self._timeout = 15
        self._token = os.environ.get("API_TOKEN")
        self._headers = {"Authorization": "Bearer " + self._token}

    def search_users(self, query: Query) -> list[User]:
        response = requests.get(f"{self.GITHUB_BASE_URL}/search/users?per_page=100&q={query}", headers=self._headers, timeout=self._timeout)
        if not response.ok:
            raise SearchUserException(str(response.json()))
        data = response.json()["items"]
        return [User(**user) for user in data]

    def get_user_info(self, username: str) -> list[User]:
        response = requests.get(f"{self.GITHUB_BASE_URL}/users/{username}", headers=self._headers, timeout=self._timeout)
        if not response.ok:
            raise GetUserInfoException(str(response.json()))
        return User(**response.json())
