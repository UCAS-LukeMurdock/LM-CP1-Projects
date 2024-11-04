#Luke Murdock, Simple Quiz Game
score = 0

print("Math Quiz")
ans = input("What is 1 + 1?\n a. 3\n b. 2\n c. -1\n d. 1\n")
if ans == "b":
    score += 1
    print("You got it right")
    ans = input("What is 257 - 62?\n a. 193\n b. 170\n c. 195\n d. 174\n")
    if ans == "c":
        score += 1
        print("You got it right")
        ans = input("What is 57 * 62?\n a. 3534\n b. 3484\n c. 3639\n d. 3395\n")
        if ans == "a":
            score += 1
            print("You got it right")
            ans = input("What is 3654 / 63?\n a. 56\n b. 58\n c. 59\n d. 60\n")
            if ans == "b":
                score += 1
                print("You got it right")
                ans = input("What is 7 ^ 4?\n a. 2325\n b. 2321\n c. 2431\n d. 2401\n")
                if ans == "d":
                    score += 1
                    print("You got it right")
                    
                else:
                    print("You got it wrong")

            #If you get question 4 wrong
            else:
                print("You got it wrong")
                ans = input("What is 2 ^ 2?\n a. 2\n b. 16\n c. 8\n d. 4\n")
                if ans == "d":
                    score += 1
                    print("You got it right")
                    
                else:
                    print("You got it wrong")

        #If you get question 3 wrong
        else:
            print("You got it wrong")
            ans = input("What is 10 / 5?\n a. 3\n b. 2\n c. 1\n d. 2.5\n")
            if ans == "b":
                score += 1
                print("You got it right")
                ans = input("What is 7 ^ 4?\n a. 2325\n b. 2321\n c. 2431\n d. 2401\n")
                if ans == "d":
                    score += 1
                    print("You got it right")
                    
                else:
                    print("You got it wrong")
                    
            else:
                print("You got it wrong")
                ans = input("What is 2 ^ 2?\n a. 2\n b. 16\n c. 8\n d. 4\n")
                if ans == "d":
                    score += 1
                    print("You got it right")
                    
                else:
                    print("You got it wrong")

    #If you get question 2 wrong
    else:
        print("You got it wrong")
        ans = input("What is 3 * 3?\n a. 9\n b. 8\n c. 10\n d. 7\n")
        if ans == "a":
            score += 1
            print("You got it right")
            ans = input("What is 3654 / 63?\n a. 56\n b. 58\n c. 59\n d. 60\n")
            if ans == "b":
                score += 1
                print("You got it right")
                ans = input("What is 7 ^ 4?\n a. 2325\n b. 2321\n c. 2431\n d. 2401\n")
                if ans == "d":
                    score += 1
                    print("You got it right")
                    
                else:
                    print("You got it wrong")
                    
            else:
                print("You got it wrong")
                ans = input("What is 7 ^ 4?\n a. 2325\n b. 2321\n c. 2431\n d. 2401\n")
                if ans == "d":
                    score += 1
                    print("You got it right")
                    
                else:
                    print("You got it wrong")
                    
        else:
            print("You got it wrong")
            ans = input("What is 10 / 5?\n a. 3\n b. 2\n c. 1\n d. 2.5\n")
            if ans == "b":
                score += 1
                print("You got it right")
                ans = input("What is 7 ^ 4?\n a. 2325\n b. 2321\n c. 2431\n d. 2401\n")
                if ans == "d":
                    score += 1
                    print("You got it right")
                    
                else:
                    print("You got it wrong")

#If you get question 1 wrong
else: 
    print("You got it wrong")
    ans = input("What is 5 - 3?\n a. 2\n b. 3\n c. -1\n d. 1\n")
    if ans == "a":
        score += 1
        print("You got it right")
        ans = input("What is 57 * 62?\n a. 3534\n b. 3484\n c. 3639\n d. 3395\n")
        if ans == "a":
            score += 1
            print("You got it right")
            ans = input("What is 3654 / 63?\n a. 56\n b. 58\n c. 59\n d. 60\n")
            if ans == "b":
                score += 1
                print("You got it right")
                ans = input("What is 7 ^ 4?\n a. 2325\n b. 2321\n c. 2431\n d. 2401\n")
                if ans == "d":
                    score += 1
                    print("You got it right")
                    
                else:
                    print("You got it wrong")
                    
            else:
                print("You got it wrong")
                ans = input("What is 2 ^ 2?\n a. 2\n b. 16\n c. 8\n d. 4\n")
                if ans == "d":
                    score += 1
                    print("You got it right")
                    
                else:
                    print("You got it wrong")
                    
    else:
        print("You got it wrong")
        ans = input("What is 3 * 3?\n a. 9\n b. 8\n c. 10\n d. 7\n")
        if ans == "a":
            score += 1
            print("You got it right")
            ans = input("What is 3654 / 63?\n a. 56\n b. 58\n c. 59\n d. 60\n")
            if ans == "b":
                score += 1
                print("You got it right")
                ans = input("What is 7 ^ 4?\n a. 2325\n b. 2321\n c. 2431\n d. 2401\n")
                if ans == "d":
                    score += 1
                    print("You got it right")
                    
                else:
                    print("You got it wrong")
                    
            else:
                print("You got it wrong")
                ans = input("What is 7 ^ 4?\n a. 2325\n b. 2321\n c. 2431\n d. 2401\n")
                if ans == "d":
                    score += 1
                    print("You got it right")
                    
                else:
                    print("You got it wrong")
                    
        else:
            print("You got it wrong")
            ans = input("What is 10 / 5?\n a. 3\n b. 2\n c. 1\n d. 2.5\n")
            if ans == "b":
                score += 1
                print("You got it right")
                ans = input("What is 7 ^ 4?\n a. 2325\n b. 2321\n c. 2431\n d. 2401\n")
                if ans == "d":
                    score += 1
                    print("You got it right")
                    
                else:
                    print("You got it wrong")
                    
            else:
                print("You got it wrong")
                ans = input("What is 7 ^ 4?\n a. 2325\n b. 2321\n c. 2431\n d. 2401\n")
                if ans == "d":
                    score += 1
                    print("You got it right")

                else:
                    print("You got it wrong")

print("Score: " + str(score) + "/5")