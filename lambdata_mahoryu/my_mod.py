# lambdata_mahoryu/my_mod.py

def enlarge(n):
    return n * 100


if __name__ == "__main__":
    # only if run from the command line, invoke the following,
    # otherwise don't

    print("JUNK")
    print("GLOBAL SCOPE")

    y = float(input("Please input a number to enlarge"))
    print(enlarge(y))