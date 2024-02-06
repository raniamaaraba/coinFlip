# Activity Python 13: Task 2
# File: ACT_Python_HeaderTemplate_Team355_maarabrn.py 
# Date:    12 11 2023
# By:      Rania Maaraba
# Section: 21
# Team:    355
# 
# ELECTRONIC SIGNATURE
# Rania Maaraba
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# Based on user input flips a coin and determines the number of
# heads, tails, and percentage of heads to tails

import math, random

#user input random sequence
Tr = int(input('Enter number of coin flips: '))

#create the numebr of head and tails trials
V = 0
V2 = 0

for k in range(Tr):
    flip = random.randint(0,1)
    if flip == 0:
        V = V + 1 
    else:
        V2 = V2 + 1
V3 = (V2/V)*100
     
print("Number of tails is", V)
print("Number of heads is", V2)
print("The percentage of heads to tails is {0:.2f}".format(V3))
    


