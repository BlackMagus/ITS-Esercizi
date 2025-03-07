def add_one(n):
    n = n + 1
    return n

def add_to_list(mylist : list):
    new_list : list = []
    for a in mylist:
        new_list.append(add_one(a))
    print(new_list)