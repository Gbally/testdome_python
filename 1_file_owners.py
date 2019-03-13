def group_by_owners(files):
    dic = {}
    for key, value in files.items():
        if value in dic:
            dic[value] = [dic[value], key]
        else:
            dic[value] = key
    
    return dic
    
files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}   
print(group_by_owners(files))