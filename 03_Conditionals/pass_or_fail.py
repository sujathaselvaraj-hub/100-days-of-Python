english= int(input( "Enter your English marks: "))
maths= int(input("Enter your Maths marks: "))
physics= int(input("Enter your Physics marks: "))
Total= english + maths + physics
if Total>=250 and Total<=300:
    print("Your marks is", Total, "And you have A grade.")
elif Total>=200 and Total<250:
    print("Your marks is", Total, "And you have a B grade.")
elif Total>=150 and Total<200:
    print("Your marks is", Total, "And you have a C grade.")
elif Total>=100 and Total<150:
    print("Your marks is", Total, "And you have a D grade.")
elif Total>=0 and Total<100:
    print("Your marks is", Total, "And you have failed.")
