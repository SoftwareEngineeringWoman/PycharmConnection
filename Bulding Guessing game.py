#we have a secret word and user needs to figure that out

#vaiable to store our secret word
secret_word= "puppy"
#variabe to store users guess and prompt new guess(while loop use)
guess=""
#limit the tries
guess_count=0
#limiting
guess_limit=3
#if true, no more guesses left
out_of_guesses= False

while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess=input("Enter guess: ")
        guess_count+=1   #after each loop, increment count
    else:
        out_of_guesses= True
if out_of_guesses:
    print("Out of guesses, You Lose")
else:
    print("You win!")

