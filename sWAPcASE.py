#funtion is provided by hackerrank
def swap_case(s):
    
    #where we will store the new results
    newstring = ''
    
    #how we will increment each character to the new string
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    
    for i in s:
        
        #converting upper to lower
        if i.isupper():
            c1 += 1
            newstring += i.lower()
          
        #converting lower to upper
        elif i.islower():
            c2 += 1
            newstring += i.upper()
        
        #making sure I add the spaces to the new string
        elif i.isspace(): 
            c3 += 1
            newstring += i
        
        #Adds any other character in the string to the new list
        else:
            c4 += 1
            newstring += i
            
    return newstring

#main function is provided by hackerrank
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
