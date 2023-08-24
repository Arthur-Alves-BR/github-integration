from dotenv import load_dotenv

from src.utils import print_user_info

from github.api_client import APIClient
from github.query import QueryItem, QueryItemType, Query


def main() -> None:
    load_dotenv()

    api = APIClient()

    languages = QueryItem.bulk_create(QueryItemType.LANGUAGE, ["cobol", "fortran"])
    location = QueryItem(QueryItemType.LOCATION, "Brazil")
    repos = QueryItem(QueryItemType.REPOS, ">2")
    kind = QueryItem(QueryItemType.KIND, "user")

    query = Query(kind, location, *languages, repos)

    for el in api.search_users(query):
        user = api.get_user_info(el.login)
        if user.bio:
            print_user_info(user)


if __name__ == "__main__":
    main()
