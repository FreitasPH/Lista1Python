import sys

def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = ("Test at line {0} ok.".format(linenum))
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def is_prime(num):
    if num > 1:
        for i in range (2,num):
            if (num % i) == 0:
                return False
        return True
    return False

def test_suite():
    test(is_prime(11))
    test(not is_prime(35))
    test(is_prime(19990228))

test_suite()