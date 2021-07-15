
# to remove the trailing zeros from the values of the string
def removes(n1):
    new=".".join([str(int(i)) for i in n1.split(".")])
    return new;
#print(removes(""))

