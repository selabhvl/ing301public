import sys
from datetime import date
import os
import platform
import pathlib

def main():
    if sys.version.startswith("3"):
        version_extract = sys.version.split()[0]
        today = date.today()
        year = today.year if today.month < 7 else today.year + 1
        year %= 2000
        print(f"Congratulations 🎉 It looks like you are running Python in version {version_extract} and ready for ING301 - Spring'{year} 🎓 !!!")
        print(f"\nBTW did you know that...")
        python_location = os.path.dirname(sys.executable).removesuffix(f"bin")
        print(f"• The Python interpreter you are running is installed at '{python_location}'?")
        os_name = platform.system()
        if os_name == "Darwin":
            os_name = "Mac OS X"
        print(f"• Your operating system is '{os_name}' (detailed name: '{platform.platform()}'), your processor architecure is: '{platform.machine()}', OS type is: '{os.name}'?")
        line_endings = os.linesep
        if line_endings == "\n":
            line_endings = "a LF ('line feed' character): '\\n'"
        elif line_endings == "\r":
            line_endings = "a CR ('carriage return' character): '\\r'"
        elif line_endings == "\r\n":
            line_endings = "a CR ('carriage return') folled by a LF ('line feed') characters: '\\r\\n'"
        else:
            bytes_seq = ' '.join([f"{int(c):x}" for c in line_endings])
            line_endings = f"the byte sequence: '{bytes_seq}'"

        print(f"• Paths on your operating file system are separated by '{os.sep}', files are per default read in '{sys.getfilesystemencoding()}' encoding {os.linesep} and file endings are detected via {line_endings}?")
        print(f"• You are currently executing this file from the directory '{pathlib.Path().cwd()}'?")
    else:
        print("It looks like you are not running Python 3 ...")
        sys.exit(1)


if __name__ == '__main__':
    main()
