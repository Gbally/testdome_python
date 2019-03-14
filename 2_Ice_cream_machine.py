"""
Python skill test from:
https://www.testdome.com/questions/python/ice-cream-machine/18331?visibility=1&skillId=9

Author:
Davor Čulig

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

# class IceCreamMachine:
    
#     def __init__(self, ingredients, toppings):
#         self.ingredients = ingredients
#         self.toppings = toppings
        
#     def scoops(self):
#         pass

# machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
# print(machine.scoops()) #should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]

######## End Original script ########

class IceCreamMachine:
    
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings
        
    def scoops(self):
        l = []
        for ingr in self.ingredients:
            for top in self.toppings:
                p = [ingr, top]
                l.append(p)
        return l

machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
print(machine.scoops()) #should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]