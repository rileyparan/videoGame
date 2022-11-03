# warm up
# write a lizard class and create an instance of iguana 

class Lizard: 
    def init__(self, locomotion): 
        self.locomotion = locomotion  
        pass 
    # whatever proerties 
    def themoreregulation(self): 
        pass  

class Iguana(Lizard): 
    def init__(self, locomotion, regeneration): 
        super().init__(locomotion)
        self.regeneration = regeneration   
        def swim(self): 
            print("paddle paddle ...") 
    
Iggy = Iguana("quad", True)

print (Iggy.regeneration)
print (Iggy.locomotion)