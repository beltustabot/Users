class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0


# Methods:
# display_info(self) - Have this method print all of the users' details on separate lines.

    def display_info(self):
            print(self.first_name)
            print(self.last_name)
            print(self.email)
            print(self.age)
            print(self.is_rewards_member)
            print(self.gold_card_points)
    
    def enroll(self):
        self.is_rewards_member= True
        self.gold_card_points= 200
    
    def spend_points(self,amount):
        self.gold_card_points= self.gold_card_points - amount


user1=User('Baki','Hanma','bakihanma@fight.com',18)
user1.enroll()
user1.display_info()
user1.spend_points(60)
user1.display_info()
# enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.
# spend_points(self, amount) - have this method decrease the user's points by the amount specified.





        