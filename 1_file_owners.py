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