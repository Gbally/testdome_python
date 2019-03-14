"""
Python skill test from:
https://www.testdome.com/questions/python/pipeline/24245?visibility=1&skillId=9

Author:
Davor Čulig

Score:
100% (3 pass / 0 fail)

Question:
As part of a data processing pipeline, complete the implementation of the 
pipeline method:

- The method should accept a variable number of functions, and it should 
	return a new function that accepts one parameter arg.
- The returned function should call the first function in the pipeline with 
	the parameter arg, and call the second function with the result of the 
	first function.
- The returned function should continue calling each function in the pipeline 
	in order, following the same pattern, and return the value from the last 
	function.

For example, pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2) then 
calling the returned function with 3 should return 5.0.
"""

######## Start Original script ########

# def pipeline(*funcs):
#     def helper(arg):
#         pass
#     return helper
            
# fun = pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2)
# print(fun(3)) #should print 5.0

######## End Original script ########

def pipeline(*funcs):
    def helper(arg):
        for func in funcs:
            arg = func(arg)
        return arg
        
    return helper
            
fun = pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2)
print(fun(3)) #should print 5.0