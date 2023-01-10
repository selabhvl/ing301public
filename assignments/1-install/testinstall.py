from pathlib import Path
import os
import sys


def main():
    print("Congratulations you are running Python in version " + sys.version)
    file = str(Path(__file__).parent.parent.absolute()) + "/2-programming/voluspaa.txt"
    if file and os.path.getsize(file) == 10627:
        print("and also your repository layout looks alright!")
    else:
        print("but your repository layout does not seem right! but it is")


if __name__ == '__main__':
    main()
