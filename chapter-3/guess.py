#set color_guess to blue
#set guess to 0
# while user_guess is not equal to color_guess
    #increment guess by 1    
    #prompt user input and store in user_guess
    #if user_guess is not equal to color_guess
        #display try again
    #else
        #break the loop
#if user_guess > 1
    #display "you guessed the color in guess guesses"
#else
    #display "you guessed the color in guess guess"

color_guess = 'blue'
guess = 0
user_guess = ''
while user_guess != color_guess:
    guess = guess + 1
    user_guess = input('Guess the color?')
    if user_guess != color_guess:
        print("try gain")
    else: 
        break
if guess > 1 :    
    print('it took you', guess, "guesses")
else:    
    print('it took you', guess, "guess")
