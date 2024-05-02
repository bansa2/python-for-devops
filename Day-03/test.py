def confeg(c):
   a = "good"
   b = "bad"

   if c == 1:
     print("Your system health is ",a)
   else:
     print("Your system Health is ",b)

c = int(input("Please check config status please enter 1,2   "))

confeg(c)