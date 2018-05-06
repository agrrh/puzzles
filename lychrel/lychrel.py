import sys

def reverse(i):
    return int(str(i)[::-1])

def is_palyndrome(i):
    i = str(i)
    if len(i) < 2:
        return False
    if i == i[::-1]:
        return True
    return False

def is_lychrel(a, iters):
    answer = True
    for i in range(0, iters):
        a = a + reverse(a)
        if is_palyndrome(a):
            answer = False
            break
    return a if answer else answer

if __name__ == '__main__':
    try:
        start, end, iters = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    except IndexError:
        print("Usage:\n\t{} [start end iters]\n".format(sys.argv[0]))
        start = 1
        end = 200
        iters = 50

    print("# Seeking Lychrel numbers in {}..{} with {} iterations:\n".format(start, end, iters))

    r = 0
    for i in range(start, end + 1):
        tmp = is_lychrel(i, iters)
        if tmp:
            print("{} -> {}".format(i, tmp))
            r += 1
    print("\nNothing. :(" if not r else "\nFound {} Lychrel number(s).".format(r))
