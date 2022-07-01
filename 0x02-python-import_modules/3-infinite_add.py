#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    add = 0
    for i in range(1, len(sys.argv)):
        add += int(sys.argv[i])
    print(add)
