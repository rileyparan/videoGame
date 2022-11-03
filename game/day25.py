# if first IF statement is not true the code goes towards the next line of possibility
def monkey_trouble (a_smile, b_smile): 
    if(a_smile == b_smile):
        print(True)
    else: 
        print(False)

monkey_trouble(True, False)
# explains that if they don't equal towards each other the conclusion is false 
def monkey_trouble_butgreater(a_smile, b_smile): 
        if a_smile ==b_smile: 
            return(True)
        else: 
            return(False)
