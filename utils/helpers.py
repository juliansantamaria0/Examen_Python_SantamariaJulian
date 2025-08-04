def validate_input(prompt, error_message):
    value = input(prompt).strip()
    while not value:
        print(error_message)
        value = input(prompt).strip()
    return value

    