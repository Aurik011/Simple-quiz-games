print("Welcome to the quiz game")

willPlay = input("Will you play? ")

if willPlay.lower() != "yes": # so that Yes or YES results in play mode
    quit()

print("Entering test play mode:")
score = 0

answer = input("Who is the founder of Microsoft? ")
if answer.lower() == "bill gates": # Don't write Bill Gates
    print("Correct Answer!")
    score += 1
else:
    print("Not correct!")

answer = input("What does PC stand for? ")
if answer.lower() == "personal computer":
    print("Correct Answer!")
    score += 1
else:
    print("Not correct!")

answer = input("What does CPU mean? ")
if answer.lower() == "central processing unit":
    print("Correct Answer!")
    score += 1
else:
    print("Not correct!")

answer = input("Who is Shakib Al Hasan? ")
if answer.lower() == "cricketer":
    print("Correct Answer!")
    score += 1
else:
    print("Not correct!")

print("You got " + str(score) + " questions correct")
print("you got " + str((score/4)*100) + "% questions correct") # percentage of correct answers

