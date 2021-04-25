# cost of semester / average ball
name = input(" enter you name : ")
sem1_score = int(input(" 1 sem score : "))
sem2_score = int(input(" 2 sem score : "))
if 90 <= ((sem1_score + sem2_score) / 2) <= 100:
    print(50)
elif 80 <= ((sem1_score + sem2_score) / 2) <= 89:
    print(30)
elif 70 <= ((sem1_score + sem2_score) / 2) <= 79:
    print(10)
elif 0 <= ((sem1_score + sem2_score) / 2) <= 69:
    print(0)
