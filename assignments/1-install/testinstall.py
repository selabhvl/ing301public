from pathlib import Path
import os
import sys


def main():
    print("Congratulations you are running Python in version " + sys.version)
    file = str(Path(__file__).parent.parent.absolute()) + "/2-programming/voluspaa.txt"
    if file:
        print("and also your repository layout looks alright!")
    else:
        print("but your repository layout does not seem right!")


if __name__ == '__main__':
    main()
