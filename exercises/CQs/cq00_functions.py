"""Challenge Question 00"""

__author__ = "730569908"


def mimic(message: str) -> str:
    """Repeat (print) the message"""
    return message


def main() -> None:
    """main function for mimic: Howdy"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
