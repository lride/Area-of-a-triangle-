import math 
import random 

#Generate two random values between 5 and 10 for both A and B:
a = random.randint(5, 10)
b = random.randint(5, 10)

# Get angle C from user in degrees
c = int(input("Enter an angle between 0 and 180 to find the area of triangle with sides A and B", ))

#Ensure angle is between 180;
#(decided to add for practice; not perfect because program terminates when if statemment fails and doesnt check the else. Please don't take marks for this I just wanted to try it and possibly get feedback :-):
if 0 <= c <= 180:
	#convert:
	angle = math.radians(c)
else:
	print("Sorry, the angle you entered is does not fit the properties of a triangle")

#Compute area using side-angle-side method:
area = 0.5*a*b*(math.sin(angle))

#Give final results:
print("The area of the triangle with sides:", "A =", str(a), "and", "B = ", str(b), "and angle:", str(c), "degrees is:", (round(area, 2)))
