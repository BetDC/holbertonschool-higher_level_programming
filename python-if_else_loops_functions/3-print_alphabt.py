#!/usr/bin/python3
for i in range(97, 123):
    if i != 101 and i != 113:  # ASCII de 'e' es 101, y de 'q' es 113
        print(f"{chr(i)}", end="")

