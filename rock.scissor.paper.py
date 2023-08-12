import random
while True:
  print("rock","scissor","paper")
  list=["rock","scissor","paper"]
  user_gamer=str(input())
  com_gamer=random.choice(list)
  
  if user_gamer=="exit":
   break
 
  else:
   print("computer:",com_gamer)
   if user_gamer==com_gamer:
    print("no one is winner")
 
   elif user_gamer=="rock" and com_gamer=="paper":
    print("com_gamer is won")
   elif user_gamer=="rock" and com_gamer=="scissor":
    print("user_gamer is won") 

   elif user_gamer=="paper" and com_gamer=="rock":
    print("user_gamer is won")
   elif user_gamer=="paper" and com_gamer=="scissor":
    print("com_gamer is won")    
 
   elif user_gamer=="scissor" and com_gamer=="rock":
    print("com_gamer is won")
   elif user_gamer=="scissor" and com_gamer=="paper":
    print("user_gamer is won")  

 
  
  
  
  
  
 


