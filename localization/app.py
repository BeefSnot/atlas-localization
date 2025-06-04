#!/usr/bin/env python3
"""
Simple app showing string localization from Babel
"""
from babel import _, ngettext


def main():
    """Main function showing translation functions"""
    greeting = _("Hello, World!")
    print(greeting)

    num_messages = 5
    message = ngettext(
        "You have one message",
        "You have %(num)d messages",
        num_messages
    ) % {'num': num_messages}
    print(message)

    welcome = _("Welcome to our application")
    print(welcome)

    num_files = 1
    file_message = ngettext(
        "%(num)d file processed",
        "%(num)d files processed",
        num_files
    ) % {'num': num_files}
    print(file_message)


if __name__ == "__main__":
    main()
