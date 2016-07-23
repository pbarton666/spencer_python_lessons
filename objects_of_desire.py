"""What to do:
Make a list of all the ranks to Eagle.
Each list element is a dict of the requirements e.g., 
   - merit badges
   - leadership requirements
   - time in rank
   
   Note that each dict has its own "index cards" (key, value) pairs.
   ... and the dict values can themselves be lists, strings, or anything else
"""

#some example code

#mom
m=dict()
m['kids']=2
m['dogs']=2
m['fish']=4
m['snake']=1
m['fav_color']='yellow'
m['fav_color']

#dad
d=dict()
d['kids']=38

#a list of parents
parents=[m, d]

#printing some info out
for individual in parents:
    print (individual['kids'])
    
#you can build a list of dicts which contain lists, and so on
#  (nested structures)

test_dict=dict()
test_dict['a_list']=[1,2,3]
test_dict['a_string']='some string'
