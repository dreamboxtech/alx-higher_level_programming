#!/usr/bin/python3
print(*["{} = {}".format(a, hex(a)) for a in range(99)], sep ="\n")