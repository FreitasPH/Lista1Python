import sys

def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = ("Test at line {0} ok.".format(linenum))
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def sum_name(list):
    cont = 0
    flag = True
    for i in list:
        if flag:
            if i == "sam":
                flag = False
                cont += 1
            else:
                cont += 1
    return cont

def test_suite():
    test(sum_name(["ana","beto","carlos","sam"]) == 4)
    test(sum_name(["ana","beto","carlos","sam","diana"]) == 4)
    test(sum_name(["sam","ana","beto","carlos"]) == 1)
    test(sum_name(["ana","beto","carlos"]) == 3)
    test(sum_name(["ana","sam","beto","carlos","sam"]) == 2)

test_suite()