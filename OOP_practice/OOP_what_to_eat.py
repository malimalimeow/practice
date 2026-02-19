class User:
    def __init__(self,username):
        self.username=username
        self.has_voted=False
    
class Poll:
    def __init__(self,topic):
        self.topic=topic
        self.options={}
        
    def add_option(self,option):
        if option not in self.options:
            self.options[option]=0
    
    def vote(self,user,option):
        if option not in self.options:
            print("The option is not available.")
        
        if user.has_voted:
            print(f"{user.username} has already voted!")
            
        self.options[option]+=1
        user.has_voted=True
        print(f"{user.username} has voted {option}.")
                
    
    def show_result(self):
        return self.options
    
    def winning_option(self):
        win=max(self.options.values())
        
        for option, val in self.options.items():
            if val==win:
                return option
        
            

poll = Poll("what to eat？")
poll.add_option("Pizza")
poll.add_option("Sushi")
poll.add_option("Hotpot")


user1 = User("Alice")
user2 = User("Bob")
user3 = User("Charlie")


poll.vote(user1, "Sushi")
poll.vote(user2, "Pizza")
poll.vote(user3, "Sushi")


poll.vote(user1, "Pizza")

poll.show_result()

winners = poll.winning_option()
print(winners)
    
        
        
        
        
        

            
            
        
            
    