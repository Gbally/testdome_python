"""
Python skill test from:
https://www.testdome.com/questions/python/path/12282?visibility=1&skillId=9

Author:
Anonymous

Score:
100% (4 pass / 0 fail)

Question:
Write a function that provides change directory (cd) function for an abstract 
file system.

Notes:

- Root path is '/'.
- Path separator is '/'.
- Parent directory is addressable as '..'.
- Directory names consist only of English alphabet letters (A-Z and a-z).
- The function should support both relative and absolute paths.
- The function will not be passed any invalid paths.
- Do not use built-in path-related functions.

For example:

path = Path('/a/b/c/d')
path.cd('../x')
print(path.current_path)
should display '/a/b/c/x'.
"""

######## Start Original script ########

# class Path:
#     def __init__(self, path):
#         self.current_path = path

#     def cd(self, new_path):
#         pass

# path = Path('/a/b/c/d')
# path.cd('../x')
# print(path.current_path)

######## End Original script ########

class Path:
    def __init__(self, path):
        self.current_path = path

    def cd(self, new_path):
        n = new_path.split('/')
        for element in n:
            self.define_path(element)

    def define_path(self, element):
        if element == "..":
            path = self.current_path.split('/')
            path.pop()
            self.current_path = "/".join(e for e in path)
        
        elif element.isalpha:
            self.current_path += "/" + element

path = Path('/a/b/c/d')
path.cd('../x')
print(path.current_path)
