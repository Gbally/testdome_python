def unique_names(names1, names2):
    l = []
    l = check(names1, l)
    l = check(names2, l)
    return l

def check(name_list, l):
    for n in name_list:
        if n not in l:
            l.append(n)
    return l

names1 = ["Ava", "Emma", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]
print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia