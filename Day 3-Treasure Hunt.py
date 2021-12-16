print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#Write your code below this line 👇

n1 = (input("right or left?\n"))
if n1== 'left':
  n2 = (input('swim or wait?\n'))
  #print (n2)
  if n2 == 'wait':
    n3 = (input('which door? red, blue, or yellow?\n'))
    #print (n3)
    if n3 == 'red':
      print ('burned by fire, Game Over!')
    elif n3 == 'blue':
      print ('drowned in water, Game Over!')
    elif n3 == 'yellow':
      print ('YOU WON!')
    else: 
      print ('Game Over!')
  else: 
    print ("attacked by shark, Game Over!")
else:
  print ("Fall into a hole, Game Over!")