from input import*
from random import randint
import itertools
import unittest
def is_num(a) :
    tamp = "1234567890"
    if ( tamp.find(a) != -1 ):
        return a;
    else :
        return -1; 
def sortList(L1,L2):
    for j in range(len(L1)):
        for i in range((len(L1) - 1), j, -1):
            if (L1[i] < L1[i-1]):
                L1[i], L1[i-1] = L1[i-1], L1[i]
                L2[i],L2[i-1] = L2[i-1], L2[i]
def checkCondition(leftList, rightList):
        for i in range(len(leftList)):
            for j in range(1, len(leftList[i])):
                if(rightList[i][j-1] > leftList[i][j]):
                    return 0
        return 1
                
def randomList(L1,L2):
    listRundom = L1
    for i in range(len(L1)):
      
        for j in range(len(L1[i])):
            listRundom[i][j]= randint(L1[i][j], L2[i][j])
    return listRundom
first_list = main.__doc__
mylist = first_list.split('\n')
variable_list = []
for i in range(len(mylist)):
    if mylist[i].find(':') != -1:
        tamp = ""
        value_list = []
        for j in mylist[i] :
            if ( is_num(j) != -1 ) :
                tamp += j
            else :
                if ( j == ';' or j == ']') :
                    value_list.append(tamp)
                    tamp = '' 
        variable_list.append(value_list)
left_list = []
right_list = []
for i in range(0,len(variable_list)):
    l1 = []
    l2 = []
    for j in range(len(variable_list[i])):
        if (j%2==0):
            l1.append(int(variable_list[i][j]))
        else:
            l2.append(int(variable_list[i][j]))
    sortList(l1,l2)
    left_list.append(l1)
    right_list.append(l2)
print left_list
'''sinh rundom tu 2 list'''
a = randomList(left_list, right_list)
'''tich decac: sinh ra cac tong so ca kiem thu'''
AllTestcase = []
for i in itertools.product(*a):
    AllTestcase.append( i)
print len(AllTestcase)
'''generate dynamic testcase'''
class TestSequense(unittest.TestCase):
    pass
def test_generator(a,b):
    def test(self):
        self.assertEqual(a,b)
    return test
if __name__ == '__main__':
    if (checkCondition(left_list, right_list) == 0):
        raise Exception("Error")    
    else:
        i = 1
        for t in AllTestcase:
            test_name = 'test_%s'  %i
            test = test_generator(main(*t),"")
            setattr(TestSequense, test_name, test)
            i = i+1
        unittest.main()