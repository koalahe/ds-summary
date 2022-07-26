import functools

'''Customized sort list for python 3'''
def customizedSort(x,y):
    return(x ** 3 - y ** 3)

if __name__ == "__main__":
    list_1 = [6, 10, 5, 20, 46]
    sorted_l = sorted(list_1, key=functools.cmp_to_key(customizedSort))
    print(sorted_l)

