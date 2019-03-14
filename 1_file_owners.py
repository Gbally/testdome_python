"""
Python skill test from:
https://www.testdome.com/questions/python/file-owners/24226?visibility=1&skillId=9

Author:
Vjekoslav Giacometti

Score:
100% (3 pass / 0 fail)

Question:
Implement a group_by_owners function that:

- Accepts a dictionary containing the file owner name for each file name.
- Returns a dictionary containing a list of file names for each owner name, in any order.
- For example, for dictionary {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}
		the group_by_owners function should return {'Randy': ['Input.txt', 'Output.txt'], 
		'Stan': ['Code.py']}.
"""

######## Start Original script ########

# def group_by_owners(files):
#     dic = {}
#     for key, value in files.items():
#         if value in dic:
#             l = dic[value]
#             l.append(key)
#             dic[value] = l
#         else:
#             dic[value] = [key]
    
#     return dic
    
# files = {
#     'Input.txt': 'Randy',
#     'Code.py': 'Stan',
#     'Output.txt': 'Randy'
# }   
# print(group_by_owners(files))

######## End Original script ########

def group_by_owners(files):
    dic = {}
    for key, value in files.items():
        if value in dic:
            l = dic[value]
            l.append(key)
            dic[value] = l
        else:
            dic[value] = [key]
    
    return dic
    
files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}   
print(group_by_owners(files))