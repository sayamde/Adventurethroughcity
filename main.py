#introduction

x = input("Greetings, what is your name? :")
print(" Hello",x,"Welcome to the adventure through the city.")
place=input( "Where would you like to go? The cafe, The Shopping Mall, The Resturant, or to the movie theaters, enter: cafe/mall/Resturant/Movies: ")

#cafe
if place == "cafe":
  option= input("Great choice you have entered the cafe, What would you like to order? Coffee/Frappucino/Sandwich/Salad: ")
  if option=="Coffee":
    print("Amazing, your coffee will be served in 5 minutes. . .",x,"Your coffee is served, enjoy :) \n\nThank you for joining us in adventure through the city ")
  elif option=="Frappucino":
    print("Amazing, your Frappucino will be served in 5 minutes. . .",x,"Your Frappucino is served, enjoy :) \n\nThank you for joining us in adventure through the city ")
  elif option=="Sandwich":
    print("Amazing, your Sandwich will be served in 5 minutes. . .",x,"Your Sandwich is served, enjoy :) \n\nThank you for joining us in adventure through the city ")
  elif option=="Salad":
    print("Healthy Choice :), your Salad will be served in 5 minutes. . .",x,"Your Salad is served, enjoy :) \n\nThank you for joining us in adventure through the city ")

#mall
if place == "mall":
  option= input("Great choice you have entered the mall, where would you like to go? clothing store/cafeteria/Video Games store: ")
  if option=="clothing store":
    print("Amazing, You have so many options but it looks like you are looking at the polk-a-dotted t-shirt. Yup I was right looks like you are going to buy the t-shirt. . . Your total will be $10.46 \n\nThank you for joining us in adventure through the city ")
  elif option=="cafeteria":
    print("Amazing You have a couple resturants,McDonalds,Panda Express,KFC, oh it looks like you are getting the orange chicken bowl from panda express. . .Your total will be $11.67 \n\nThank you for joining us in adventure through the city ")
  elif option=="Video Games store":
    print("Amazing, you are at the checkout counter holding NBA 2k20 in your hand with the gamestop giftcard you got on christmas. . .Your total will be $20.54 taken from your gift card \n\nThank you for joining us in adventure through the city ")

#Resturant
if place == "Resturant":
  option= input("Great choice you have entered the Resturant, what would you like to eat? pizza/hamburgers/french fries: ")
  if option=="pizza":
    print("mmmmh, sounds tasty your food will come out in 15 minutes. . .Enjoy:) \n\nThank you for joining us in adventure through the city ")
  elif option=="hamburgers":
    print("yummy, looks like your getting hamburgers your food will be out in 15 minutes. . .Enjoy:) \n\nThank you for joining us in adventure through the city ")
  elif option=="french fries":
    print("Sounds delecious, coming right out in 10 minutes. . .Here you go enjoy, oh wait I'll get you some ketchup. There your all set enjoy your food:) \n\nThank you for joining us in adventure through the city ")

#Movies
if place == "Movies":
  option= input("Great choice you have entered the Movie theater, what would you like to eat? home alone/coco/finding nemo: ")
  if option=="home alone":
    print("really great movie, have fun watching it and don't forget the butter popcorn \n\nThank you for joining us in adventure through the city ")
  elif option=="coco":
    print("coco, very good movie with a good moral have a great time watching it dont forget your popcorn:) \n\nThank you for joining us in adventure through the city ")
  elif option=="finding nemo":
    print("Finding Nemo, ahhh kind of a sad movie but its pretty good have fun, dont forget the popcorn;) \n\nThank you for joining us in adventure through the city ")


