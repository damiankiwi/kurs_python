import sys

def get_python_version():
    return sys.version

if __name__ == "__main__":
    python_version = get_python_version()
    print("You are using Python version:", python_version)