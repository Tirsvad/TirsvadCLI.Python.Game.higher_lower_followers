from game_data import data
from random import choice
from art import vs, logo
from os import name, system


def title() -> None:
    # define clear function
    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
    clear()
    print(logo)


def get_person(game_data: list) -> dict:
    """
    Get random person from game data.

        @param list game_data:
            game data

        @return dict:
            Return a new person from instagram
    """
    return choice(game_data)


def formatted_question(account: dict, s: str) -> str:
    """
    Returns a question formatted string for output

        @param dict account:
            x account
        @param str s:
            A or B for the question

        @return str:
            Formatted string for output
    """
    return f"Compare {s}: {account['name']} a {account['description']} from {account['country']}"


def check_answer(followers_a: int, followers_b: int, answer: str) -> bool:
    """
    Compare followers for person / organization

    @param int followers_a:
        followers that the account have
    @param int followers_b:
        followers that the account have
    @param str answer:
        Formatted string for console output

    @return bool:
        is answer correct
    """
    if followers_a > followers_b and answer == "a":
        return True
    elif followers_a < followers_b and answer == "b":
        return True
    return False


def game():
    """
    The game
    """
    score = 0
    answer = ""
    continue_game = True
    x_account_a = get_person(data)
    while continue_game:
        title()
        if answer != "":
            print(f"You got it right. Score {score}")
        x_account_b = get_person(data)
        while x_account_a == x_account_b:
            x_account_b = get_person(data)
        print(formatted_question(x_account_a, "A"))
        print(vs)
        print(formatted_question(x_account_b, "B"))
        answer = input("\nWho have more followers? Type 'A' or 'B' ").lower()
        if check_answer(followers_a=x_account_a["follower_count"],
                        followers_b=x_account_b["follower_count"], answer=answer):
            score += 1
            if answer == "b":
                x_account_a = x_account_b
        else:
            title()
            print(f"Sorry, that's wrong. Final score: {score}")
            continue_game = False


game()
