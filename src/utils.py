from github.user import User


def print_user_info(user: User) -> None:
    print("===============================================================================================")
    print(user.login)
    print(user.bio)
