import sys

def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = ("Test at line {0} ok.".format(linenum))
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def sum_odd(list):
    s = 0
    flag = True
    for i in list:
        if flag:
            if i % 2 == 0:
                flag = False
            else:
                s = s + i
    return s

def test_suite():
    test(sum_odd([1,3,5,7]) == 16)
    test(sum_odd([1,2,3,5,7]) == 1)
    test(sum_odd([1,3,5,7,2]) == 16)
    test(sum_odd([1,2,4,3,5,7]) == 1)
    test(sum_odd([2,1,3,5,7]) == 0)

test_suite()