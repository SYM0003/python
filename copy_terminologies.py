# aliasing
    # creating duplicate reffrece variable for an object
l1=[10,20,50,60]
l2=l1
# cloning
    # creating duplicate object for an ..`object
l1=[10,20,50,60]
l2=l2.copy()


# shalow cloning
l1=[10,20,[30,40],50,60]
l2=l2.copy()

# deep cloning

import copy
# copy.copy()->shalow copy
# copy.deepcopy(x)->deep copy
l1=[10,20,[30,40],50,60]
l2=copy.deepcopy(l1)
