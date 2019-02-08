'''
QUIZ MASTER PROJEC
-------------------
The criteria for the project are on the website. Make sure you test this quiz with
two of your student colleagues before you run it by your instructor
'''

score = 0


print("this is a test")

#1. how many letters are in the word'letters'
numoneanswer = input("1. how many letters are in the word'letters'\n\r   A. 1\n\r   B. 7\n\r   C. 6\n\r   Your Answer:")
if numoneanswer.lower() == "a" or numoneanswer == "1":
    print("correct")
    score+=1
elif numoneanswer.lower() == "b" or numoneanswer == "2":
    print("wrong, trick question")
elif numoneanswer.lower() == "c" or numoneanswer == "3":
    print("wrong, trick question")
else:
    print("wrong")

#2. when will the wall be built
numtwoanswer = input("\n\r2. when will the wall be built?\n\r   A. 2019\n\r   B. 2020\n\r   C. 2021\n\r   Your Answer:")
if numtwoanswer.lower() == "a" or numtwoanswer.lower() == "when will the wall be built":
    print("nope, the goverment shut down will continue through trumps presidensy")
elif numtwoanswer.lower() == "b" or numtwoanswer == "2020":
    print("nope, we wont even have flying cars")
elif numtwoanswer.lower() == "c" or numtwoanswer == "2021":
    print("who knows?")
    score += 1
else:
    print("wrong")

#3. how to comment
numthreeanswer = input("\n\r3. how do you enter a single line comment?\n\r   A. idk\n\r   B. #this is how\n\r   C. //this is how\n\r   Your Answer:")
if numthreeanswer.lower() == "a" or numthreeanswer.lower() == "idk":
    print("wrong")
elif numthreeanswer.lower() == "b" or numthreeanswer.lower() == "#this is how":
    print("correct")
    score += 1
elif numthreeanswer.lower() == "c" or numthreeanswer.lower() == "//this is how":
    print("wrong, this is NOT C sharp")
else:
    print("wrong")

#4. how was python named
numfouranswer = input("\n\r4. how was python named?\n\r   A. snake was the first game made in the language\n\r   B. the movie: mighty python and the holly grail\n\r   C. snakes are cool\n\r   Your Answer:")
if numfouranswer.lower() == "a" or numfouranswer.lower() == "snake was the first game made in the language":
    print("nope")
elif numfouranswer.lower() == "b" or numfouranswer.lower() == "the movie: mighty python and the holly grail":
    print("correct")
    score += 1
elif numfouranswer.lower() == "c" or numfouranswer.lower() == "snakes are cool":
    print("no, snakes are not cool")
else:
    print("wrong")

#5. what do you prefer
numfiveanswer = input("\n\r5. what do you prefer\n\r   A. this quiz to be over\n\r   B. to own a zoo\n\r   C. a slice of pie\n\r   D. to get a high score\n\r   Your Answer:")
if numfiveanswer.lower() == "a" or numfiveanswer.lower == "this quiz to be over":
    print("same, but wrong")
elif numfiveanswer.lower() == "b" or numfiveanswer.lower == "to own a zoo":
    print("what, why?")
elif numfiveanswer.lower() == "c" or numfiveanswer.lower == "a slice of pie":
    print("sounds yummy, but im a computer not a cook")
elif numfiveanswer.lower() == "d" or numfiveanswer.lower == "to get a high score":
    print("correct")
    score += 1
else:
    print("wrong")

#score and percentage
percentage= score/5*100
print("\n\ryour score is:", score, "out of 5")
print("your pecentage is:", percentage,"%")