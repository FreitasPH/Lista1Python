import sys

def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = ("Test at line {0} ok.".format(linenum))
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def sum_complex(num1, num2):
    R = num1[0] + num2[0]
    I = num1[1] + num2[1]
    sum = (R,I)
    return sum

def test_suite():
    test(sum_complex((1,2),(3,4)) == (4,6))
    test(sum_complex((1,2),(0,0)) == (1,2))
    test(sum_complex((1,2),(-1,-2)) == (0,0))

test_suite()