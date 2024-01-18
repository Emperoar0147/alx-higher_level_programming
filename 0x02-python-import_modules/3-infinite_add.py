#!/usr/bin/python3
import sys

def main():
    argv = sys.argv
    num_args = len(argv) - 1

    if num_args == 0:
        print("No arguments provided.")
    else:
        total = sum(int(arg) for arg in argv[1:])
        print(f"Result of the addition of all arguments: {total}")

if __name__ == "__main__":
    main()
