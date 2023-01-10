from pathlib import Path
import os
import sys


def main():
    print("Congratulations you are running Python in version " + sys.version)
    file = str(Path(__file__).parent.parent.absolute()) + "/2-programming/voluspaa.txt"
    if file:
        print("and also your repository layout looks alright!")
    else:
        print("your files do not look correct at all!")
        print("test123")


if __name__ == '__main__':
    main()
