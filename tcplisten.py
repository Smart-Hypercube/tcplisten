#!/usr/bin/python3

while True:
    line = input()
    if line[15:19] == ' IP ' and ' tcp ' in line:
        size = int(line.rpartition(' ')[2])
        if size == 0:
            continue
        f = 200 + size * 4
        print('play --no-show-progress --null --channels 1 synth 0.1 sine %d' % f, flush=True)
