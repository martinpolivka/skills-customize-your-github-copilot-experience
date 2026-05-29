# Starter Code for Python Testing and Debugging Lab


def calculate_average(scores):
    """Return the average of a list of numbers."""
    # BUG: Empty list should return 0.0 instead of raising ZeroDivisionError.
    total = sum(scores)
    return total / len(scores)


def is_strong_password(password):
    """Return True if password has length >= 8 and includes a digit."""
    has_digit = False
    for ch in password:
        if ch.isdigit():
            has_digit = True

    # BUG: Uses OR instead of AND, allowing weak passwords.
    return len(password) >= 8 or has_digit


def format_username(first_name, last_name):
    """Return a username in the format: first initial + last name, lowercase."""
    # BUG: Does not trim spaces and can return uppercase characters.
    return first_name[0] + last_name


if __name__ == "__main__":
    print("Quick manual checks:")
    print(calculate_average([90, 80, 100]))
    print(is_strong_password("abc123"))
    print(format_username("Ada", "Lovelace"))
