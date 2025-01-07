import sys


def main():
    if sys.version.startswith("3"):
        print("Congratulations you are running Python in version " + sys.version)
    else:
        print("It looks like you are not running Python 3")


if __name__ == '__main__':
    main()
