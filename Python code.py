
############################################################### PYTHON CODE ########################################################



ws = 'Print only the words that start with s in this sentence'


for letter in ws.split():
    if letter[0] == 's':
        print(letter)



# Used range() to print all the even numbers from 0 to 10

wrds = [x for x in range(0,11) if x%2==0]

print(wrds)



# This puts the output in a list format

list(range(0,11,2))



# This prints the output for the variable x

for x in range(0,11,2):
    print(x)



list1 = [y for y in range(0,51) if y%3==0]

print(list1)



n_x =  'Print every word in this sentence that has an even number of letters'

for y in n_x.split():
    if len(y) %2==0:
        print(y + ': is Even')
    else:
      print(y + ': is Odd')
      


# Here I write a program that prints the integers from 1 to 100. But for multiples of three print "Python" instead of the number, and for multiples of five print "Coding". For numbers which are multiples of both three and five print "PythonCoding".

for z in range(1,101):
    if z%3==0 and  z%5==0:
        print('PythonCoding')
    elif z%3==0:
        print('Python')
    elif z%5==0:
        print('Coding')
    else:
        print(z)
 


# Used List Comprehension to create a list of the first letters of every word in the string below:

bunch = 'Create a list of the first letters of every word in this string'

newst = [n[0] for n in bunch.split()]

print(newst)



# Wrote a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd


def min_or_max(a,b):

    if a%2==0 and b%2==0:
        if a < b: 
            result = a 
        else:
            result = b
    else:
        if a > b:
            result = a 
        else:
            result = b
        
    return result



# Another way to write the code is:

def minOrMax(a,b):
    if a%2==0 and b%2==0:
        result = min(a,b)
    else:
        result = max(a,b)
    
    return result


print(minOrMax(32,71))



# Another way to write the code:

def Min_or_Max(a,b):
    if a%2==0 and b%2==0:
        return min(a,b)
    else:
        return max(a,b)
        

print(min_or_max(7,14))

print(Min_or_Max(12,20))



# Here I write a function that takes a string and returns 'True' if both words begin with same letter:

def gc(name1,name2):

    if name1[0] == name2[0]:
        return True
    else:
        return False 

print(gc('Brick', 'House'))



# Here is another way to solve it using a two-word string:

def GC(text):
    wordlist = text.lower().split()
       
    first = wordlist[0]
    second = wordlist[1]
    
    return first[0] == second[0]

print(GC('Computer desk'))    



# Here is a third way to write it:

def a_cr(text):
    wordlist = text.lower().split()
           
    return wordlist[0][0] == wordlist[1][0]

print(a_cr('Space shuttle'))

print(a_cr('Yay you'))



# Here is a fourth way to write it:

def A_Cr(text):
    wordlist = text.lower().split()
       
    first = wordlist[0]
    second = wordlist[1]
    
    return first[0] == second[0]


print(A_Cr('Car seat'))



#  Given two integers, the code returns 'True' if the sum of the integers is 20 or if one of the integers is 20. If not, return 'False'.

def sum_int(a,b):
    if a + b == 20:
        return True
    elif a==20 or b==20:
        return True
    else:
        return False


print(sum_int(20,30))

print(sum_int(12,17))

print(sum_int(18,34))



# Another way to write it:

def sumOfInt(a,b):

    if a + b == 20:
        result = 'True'
    elif a == 20 or b==20:
        result = 'True'
    else:
        result = 'False'
    return result


print(sumOfInt(22,3))

print(sumOfInt(14,6))

print(sumOfInt(12,24))



#  Here I write a function that capitalizes the first and fourth letters of a word: 

def Cap_Name(name):
    Aname = name[0].upper() + name[3].upper()
    return Aname

print(Cap_Name('Learning'))



# Here is another way to write the code but writing the whole word:

def cap_name(name):
    
    first_letter = name[0]
    inbetween = name[1:3]
    fourth_letter = name[3]
    rest = name[4:]
    
    return first_letter.upper() + inbetween + fourth_letter.upper() + rest

print(cap_name('Specialize'))

print(cap_name('Coding'))



# Another way to write the code using 'capitalize()':

def CapName(name):
    
    first_half = name[:3]
    second_half = name[3:]
    
    return first_half.capitalize() + second_half.capitalize()

print(CapName('Driving'))

print(CapName('Parking'))



# Here I write a code that takes a sentence and returns the sentence with the words reversed:

def sn_reve(text):
    words = text.split()
    reversed_words = words[::-1]
    
    return ' '.join(reversed_words)

print(sn_reve('Coding is fun.'))

print(sn_reve('The movie was good.'))



# Here is another way to write the code:

def SnReve(text):
    words = text[::-1]    
    return words

print(SnReve('Drawing and painting.'))



# Here I write a code that takes an integer n and returns 'True' if n is within 10 of either 100 or 200 and returns 'False' otherwise:

def a_t(num):
    if 111 > num > 89:
        return True
    if 211 > num > 189:
        return True
    else:
        return False

print(a_t(82))

print(a_t(203))

print(a_t(90))



# Here given a list of integers, return 'True' if the array contains a 3 next to another 3 somewhere else in the list otherwise return 'False':
   
def has_33(nums):
    if nums[1:1+2] == [3,3]:   
        return True
    else:
        return False

print(has_33([2,3,3,4,62]))

print(has_33([2,3,4,5,6,7,8]))

print(has_33([2,4,7,8,9,3,3,1,0]))
        


# Here, given a string, the code returns a string where for every character in the original string the code will output three copies of each character:

def hb(wrds):
    
    newstr = []

    for i in wrds:
        newstr += i * 3     
    
    return newstr

aVar = hb('It will be sunny today.')
print(aVar, end='')



def cu(text):

    result = ''
    
    for char in text:
        result += char*3
    return result

print(cu('It is sunny today.'))

print(cu('House'))

    





