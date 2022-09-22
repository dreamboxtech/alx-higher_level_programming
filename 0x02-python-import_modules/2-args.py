#!/usr/bin/python3

def run(*args):
    length = len(args)

    def list_args(args):
        for index, value in enumerate(args):
            print("{}: {}".format(index + 1, value))

    if length == 1:
        print("{} argument:".format(length))
        list_args(args)
    elif length == 0:
        print("{} arguments.".format(length))
        list_args(args)
    elif length > 1:
        print("{} arguments:".format(length))
        list_args(args)


if __name__ == "__main__":
    run()
