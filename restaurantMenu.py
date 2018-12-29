class Dish():
    def __init__(self,name,cost,ingredients):
        self.cost=cost
        self.name=name
        self.ingredients=ingredients



    def __str__(self):
        return("Name:{}\nIngredients:{}\nCost:{}".format(self.name,self.ingredients,self.cost))

D1=Dish('Palak Paneer',120,'Paneer,Corn,Butter')
D2=Dish('Mushroom Cheese',140,'Mushroom,Lettuce,Cheese')
D3=Dish('Vegetable Platter',180,'Carrots,Brinjal,Lettuce,Peas,etc')
S1=Dish('Sizzlers',150,'Corn,Cheese,Chicken')
S2=Dish('Chicken Tandoori',200,'Chicken,Chillies,Maida')
S3=Dish('Prawns Kebab',190,'Prawns,Spring Onions,Chillies')
C1=Dish('Cindrella',100,'Cream,Berries,Chocolate')
C2=Dish('Mojito',120,'Vodka,Redbull,Lemon')
C3=Dish('Red Wine',100,'Fertilized Grapes,Added Enhancer')
M1=Dish('Rabdi',120,'Fertilized Milk,Almonds')
M2=Dish('Gulab Jamun',80,'Maida,Sweetners,Kesar')
M3=Dish('Kheer',90,'Brown Rice,Milk,Dry Fruits')


print("Welcome To The Restaurant!!")
amount=0
while True:


    print('---Menu---')
    print('1.Starters\n2.Main Course\n3.Drinks\n4.Desserts\n5.Place Order')
    ch=int(input("Please Select Your Choice:"))
    if(ch==1):
        print('STARTERS AVAILABLE ARE:\n')
        print('')
        print(S1)
        print('')
        print(S2)
        print('')
        print(S3)
        ch1=int(input("Please Select your Choice:"))
        if(ch1==12):
            amount=amount+S1.cost+S2.cost
        elif(ch1==23):
            amount=amount+S2.cost+S3.cost
        elif(ch1==13):
            amount=amount+S1.cost+S3.cost
        elif(ch1==123):
            amount=amount+S1.cost+S2.cost+S3.cost

        elif(ch1==1):
            amount=amount+S1.cost

        elif(ch1==2):
            amount=amount+S2.cost

        elif(ch1==3):
            amount=amount+S3.cost

        else:
            print('Invalid Choice!!')
        continue

    elif(ch==2):
        print('MAIN COURSE AVAILABLE ARE:\n')
        print('')
        print(D1)
        print('')
        print(D2)
        print('')
        print(D3)
        ch2=int(input("Please Select your Choice:"))
        if(ch2==12):
            amount=amount+D1.cost+S2.cost
        elif(ch2==23):
            amount=amount+D2.cost+D3.cost
        elif(ch2==13):
            amount=amount+D1.cost+D3.cost
        elif(ch2==123):
            amount=amount+D1.cost+D2.cost+D3.cost

        elif(ch2==1):
            amount=amount+D1.cost

        elif(ch2==2):
            amount=amount+D2.cost

        elif(ch2==3):
            amount=amount+D3.cost

        else:
            print('Invalid Choice!!')
        continue

    elif(ch==3):
        print('DRINKS AVAILABLE ARE:\n')
        print('')
        print(C1)
        print('')
        print(C2)
        print('')
        print(C3)
        ch3=int(input("Please Select your Choice:"))
        if(ch3==12):
            amount=amount+C1.cost+C2.cost
        elif(ch3==23):
            amount=amount+C2.cost+C3.cost
        elif(ch3==13):
            amount=amount+C1.cost+C3.cost
        elif(ch3==123):
            amount=amount+C1.cost+C2.cost+C3.cost

        elif(ch3==1):
            amount=amount+C1.cost

        elif(ch3==2):
            amount=amount+C2.cost

        elif(ch3==3):
            amount=amount+C3.cost

        else:
            print('Invalid Choice!!')

        continue

    elif(ch==4):
        print('DESSERTS AVAILABLE ARE:\n')
        print('')
        print(M1)
        print('')
        print(M2)
        print('')
        print(M3)
        ch4=int(input("Please Select your Choice:"))
        if(ch4==12):
            amount=amount+M1.cost+M2.cost
        elif(ch4==23):
            amount=amount+M2.cost+M3.cost
        elif(ch4==13):
            amount=amount+M1.cost+M3.cost
        elif(ch4==123):
            amount=amount+M1.cost+M2.cost+M3.cost

        elif(ch4==1):
            amount=amount+M1.cost

        elif(ch4==2):
            amount=amount+M2.cost

        elif(ch4==3):
            amount=amount+M3.cost

        else:
            print('Invalid Choice!!')
        continue

    elif(ch==5):
        print('Place Order')
        break

    else:
        print('Incorrect Choice, Choose Again!')
        continue

print('YOUR BILL IS: {}'.format(amount))
    
