"""
Python skill test from:
https://www.testdome.com/questions/python/merge-names/24231?visibility=1&skillId=9

Author:
Hazael Gomez

Score:
100% (4 pass / 0 fail)

Question:
Implement the IceCreamMachine's scoops method so that it returns all 
combinations of one ingredient and one topping. If there are no ingredients 
or toppings, the method should return an empty list.

For example, IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"]).scoops() 
should return [['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']].
"""

######## Start Original script ########

# def unique_names(names1, names2):
#     return None

# names1 = ["Ava", "Emma", "Olivia"]
# names2 = ["Olivia", "Sophia", "Emma"]
# print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia

######## End Original script ########

def unique_names(*args):
    l = []
    for arg in args:
        l = check(arg, l)
    return l

def check(name_list, l):
    # Browse the list add append if it is not already in the list l
    for n in name_list:
        if n not in l:
            l.append(n)
    return l

names1 = ["Ava", "Emma", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]
print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia