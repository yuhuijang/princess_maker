def median(lst):
    lst = sorted(lst)
    if len(lst) % 2 == 0:
        first = len(lst)/2 # index = 2, value = 5
        sencond = first -1 # index = 1, val = 4

        a = float(lst[first]+lst[sencond])/2.0
        print a


    else:
        center = (lst[0] + len(lst))/2
        print center

median([6, 8, 12, 2, 23])
