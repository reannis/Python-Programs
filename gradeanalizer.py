A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60

score = int(input("What did you score on the test? "))

if score >= A_SCORE:
    print("You got an A")

elif score >= B_SCORE:
    print("You got a B")

elif score >= C_SCORE:
    print("You got a C")

elif score >= D_SCORE:
    print("You got a D")

else:
    print("You got an F")
