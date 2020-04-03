def mult_table(num):
    print("       ", end="")
    for j in range(1, num + 1):
        print(" {:4d}".format(j), end="")
    print("")
    print("    :--", end="")
    for j in range(1, num + 1):
        print("-----", end="")
    print("")
    for i in range(1, num + 1):
        print("{:4d}:  ".format(i), end="")
        for j in range(1, num + 1):
            print(" {:4d}".format(i*j), end="")
        print("")

mult_table(12)