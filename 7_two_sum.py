"""
Python skill test from:
https://www.testdome.com/questions/python/two-sum/24970?visibility=1&skillId=9

Author:
Anonymous

Score:
75% (3 pass / 1 fail)
Fail on:
Performance test with a large list of numbers: Time limit exceeded

Question:
Write a function that, when passed a list and a target sum, returns, efficiently 
with respect to time used, two distinct zero-based indices of any two of the numbers, 
whose sum is equal to the target sum. If there are no two numbers, the function should 
return None.

For example, find_two_sum([3, 1, 5, 7, 5, 9], 10) should return a single tuple containing 
any of the following pairs of indices:

- 0 and 3 (or 3 and 0) as 3 + 7 = 10
- 1 and 5 (or 5 and 1) as 1 + 9 = 10
0- 2 and 4 (or 4 and 2) as 5 + 5 = 10
"""

######## Start Original script ########

# def find_two_sum(numbers, target_sum):
#     """
#     :param numbers: (list of ints) The list of numbers.
#     :param target_sum: (int) The required target sum.
#     :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
#     """
#     return None

# print(find_two_sum([3, 1, 5, 7, 5, 9], 10))

######## End Original script ########

def find_two_sum(numbers, target_sum):
    """
    :param numbers: (list of ints) The list of numbers.
    :param target_sum: (int) The required target sum.
    :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
    """
    cpt = 0
    for n in numbers:
        cpt2 = 0
        for n2 in numbers[numbers.index(n) + 1:]:
            if n + n2 == target_sum:
                return tuple([cpt, numbers.index(n) + 1 + cpt2])
            cpt2 += 1
        cpt += 1

    return None

print(find_two_sum([5, 5], 10))
