#Ighoise Odigie
#May, 5 2020
#(Assignment #4)

#<!--First Part: The Setup-->
#This is the title which is just for aesthetic purposes
intro = "---Welcome to Guess That Animal---\n" + "_" * 35
print(intro)

#These are variables that must be initialized
chances = 3
score = 0
question_number = 0

#This is an array containing all the questions and their associated answers
questions_array = [["This one's easy, what is the tallest animal in the world", "Giraffe"], 
                   ["what is the fastest animal on planet earth", "Cheetah"], 
                   ["What is the slowest animal ever recorded", "Sloth"],
                   ["What is the biggest animal in the sea", "Whale"],
                   ["What animal lives in the North Pole", "Polar Bear"],
                   ["Which animal has 8 legs", "Spider"],
                   ["Now this one is hard, what animal is the most closely related to humans", "Chimpanzee"],
                   ["end"]
                  ]

#This is the check function that is used in the main code below, it checks if the user response matches the given answer
#The .lower is there to make the check case insensitive and make it a better experience for the user
def check(response):
  if response.lower() == answer.lower():
    return "correct"
  elif response.lower() != answer.lower():
    return "incorrect"


#<!--Second Part: Looping through Questiions-->
i = 0
while i <= chances:
  #These varibales extract the current question and answer from the array
  question = questions_array[question_number][0]
  answer = questions_array[question_number][1]
  #The variables above are formatted and displayed to the user 
  response_text = f"\nQuestion {question_number + 1}: {question} =>" 
  response = str(input(response_text))
  #This variable takes the user response and calls the check function. 
  #The result from the check function (either correct or incorrect) is used to determine how to continue below
  result = check(response)
  
  #If the answer is correct the below occurs
  if result == "correct":
    #A correct message is displayed
    print("\nYou are correct ✔️")
    #The score is increased by 1 and displayed
    score += 1
    print(f"[Your current score: {score}]")
    #The chances are reset to 3, and we move on to the next question unless their are no more
    chances = 3
    if (questions_array[question_number + 1][0] == "end"):
      isCompleted = True
      break
    else:
      question_number += 1
    
  #Else If the answer is wrong the below occurs
  else:
    #A incorrect message is displayed
    print("\nSorry, but you are incorrect ❌")
    #The users chances are decreased by 1
    chances -= 1
    #If the user has no more chances, than display the game over message and the correct answer
    if chances == 0:
      print(f"\nGame Over! The correct answer was {answer}\n[You scored {score} points]")
      isCompleted = False
      break
    #Else If the user has a few more chances, than display how many chances are left
    else:
      print(f"[You have {chances} chance(s) left]")

if isCompleted == True:
  #If the iser has completed all questions than the for loop will break out to here where this message will be displayed
  print(f"\n\n[Great Job, you answered all questions correctly]\n[You scored {score} points]")

#<!--Program Complete-->