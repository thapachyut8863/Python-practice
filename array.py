#here we willa talk about the array in python>
#from importing *we can use all the function of array
from array import *
nums = array('i',[1,2,34,4,5,6])

newaar = array(nums.typecode,(a*a for a in nums))


for e in newaar:
    print(e)