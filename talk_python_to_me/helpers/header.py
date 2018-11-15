def print_header(title='HELLO APP', width=50):
    spaces = int((width - len(title)) / 2)

    print('-' * width)
    print(' ' * spaces + title)
    print('-' * width)
    print()
