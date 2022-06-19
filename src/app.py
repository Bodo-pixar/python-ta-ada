import sys
import os


def prime(s):
    # your code goes here
    for i in range(2, int(s/2)):
        if (s % i) == 0:
            return False
    return True

def solution(s):
    return prime(s)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argument required"))

    print(solution(sys.argv[1]))
