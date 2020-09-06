import time
total_score = 0
user =input("Username please?: ")
print(user)

def hole_one(score_hole_one):
    global total_score
    total_score = total_score + score_hole_one
    return score_hole_one

while True:
    # Take input from the user
    choice = input("Enter hole number (1, 2, 3, 4, 5): ")
    if choice in ('1', '2', '3', '4', '5'):
        hole_score = int(input("Score for the hole: "))
        if choice == '1':
            print(user, "has a score of", hole_one(hole_score), "for hole number", choice)
            time.sleep(1.5)
            print(user, "has a total score of:", total_score)
        elif choice == '2':
            print(user, "has a score of", hole_one(hole_score), "for hole number", choice)
            time.sleep(1.5)
            print(user, "has a total score of:", total_score)
        elif choice == '3':
            print(user, "has a score of", hole_one(hole_score), "for hole number", choice)
            time.sleep(1.5)
            print(user, "has a total score of:", total_score)
        elif choice == '4':
            print(user, "has a score of", hole_one(hole_score), "for hole number", choice)
            time.sleep(1.5)
            print(user, "has a total score of:", total_score)
        elif choice == '5':
            print(user, "has a score of", hole_one(hole_score), "for hole number", choice)
            time.sleep(1.5)
            print(user, "has a total score of:", total_score)
    else:
        print("Nope")
        time.sleep(1)
        print("Not allowed anything other than 1, 2, 3, 4, 5")
        time.sleep(1.5)
        print("Let's try again")
        time.sleep(1)

        # break
