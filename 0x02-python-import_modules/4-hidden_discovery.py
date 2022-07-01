#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    dir_t = dir(hidden_4)
    for i in range(0, len(dir_t)):
        if "__" != dir_t[i][:2]:
            print(dir_t[i])
