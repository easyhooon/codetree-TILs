import sys

si = sys.stdin.readline

n = int(si())

d = dict()

for i in range(n):
    cmd = si().strip()
    if cmd.split(" ")[0] == "add":
        key = cmd.split(" ")[1]
        value = cmd.split(" ")[2]
        d[key] = value

    if cmd.split(" ")[0] == "find":
        key = cmd.split(" ")[1]
        if key in d:
            print(d[key])
        else:
            print("None")

    if cmd.split(" ")[0] == "remove":
        key = cmd.split(" ")[1]
        d.pop(key)