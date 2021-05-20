#decorators
text = str(input())


def uppercase_decorator(func):
    def wrapper(text):
        print(text.upper())

    return wrapper


@uppercase_decorator
def display_text(text):
    return (text)


display_text(text)
