#!/usr/bin/env python

import sys


if __name__ == '__main__':
    counter = 0

    for d in (5,):
        for o in range(0, 10):
            for n in range(0, 10):
                for a in range(0, 10):
                    for l in range(0, 10):
                        for g in range(0, 10):
                            for e in range(0, 10):
                                for r in range(0, 10):
                                    for b in range(0, 10):
                                        for t in (0,):
                                            donald = d * 100000 + o * 10000 + n * 1000 + a * 100 + l * 10 + d
                                            gerald = g * 100000 + e * 10000 + r * 1000 + a * 100 + l * 10 + d
                                            robert = r * 100000 + o * 10000 + b * 1000 + e * 100 + r * 10 + t

                                            letters = [d, o, n, a, l, g, e, r, b, t]

                                            cond = []
                                            cond.append(len(letters) == len(set(letters)))  # check that all letters are unique
                                            cond.append(donald + gerald == robert)
                                            cond.append(donald < 1000000)
                                            cond.append(gerald < 1000000)
                                            cond.append(robert < 1000000)

                                            if sum(cond) == len(cond):
                                                print(donald, gerald, robert)

                                            counter += 1
    sys.exit(0)
