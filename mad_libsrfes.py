# Python Mad Libs Warm-Up Activity

# Welcome message
print("Welcome to Python Mad Libs!")
print("Answer the following questions to create your very own silly story.\n")

# Gather user inputs
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adverb = input("Enter an adverb: ")

# Build the story using an f-string
story = (
    f"Today, I saw a {adjective} {noun} that decided to {verb} {adverb}.\n"
    "I couldn't believe my eyes!"
)

# Display the completed story
print("\nHere is your story:")
print(story)

print("Would you like to play again?")
play_again = input("Enter Yes or No: ")
if play_again == "Yes":
    while play_again == "Yes":
        # Welcome  back message
        print("Welcome back to Python Mad Libs!")
        print("Answer the following questions to create your very own silly story.\n")

        # Regather user inputs
        adjective = input("Enter an adjective: ")
        noun = input("Enter a noun: ")
        verb = input("Enter a verb: ")
        adverb = input("Enter an adverb: ")

        # Build the story using an f-string
        story = (
            f"Today, I saw a {adjective} {noun} that decided to {verb} {adverb}.\n"
            "I couldn't believe my eyes!"
        )
        print("\nHere is your story:")
        print(story)

        print("Would you like to play again?")
        play_again = input("Enter Yes or No: ")

        if play_again == "No":
            print("Nice playing with you!")
            exit
        elif play_again == "Yes":
            # Welcome  back message
            print("Welcome back to Python Mad Libs! Lets change it up this time!")
            print("Answer the following questions to create your new very own silly story.\n")

            # Regather user inputs
            adjective = input("Enter an adjective: ")
            noun = input("Enter a noun: ")
            verb = input("Enter a verb: ")
            adverb = input("Enter an adverb: ")
            number1 = int(input("Enter your favorite number: "))
            number2 = int(input("Now enter in ridiculous number: "))
            noun2 = input("Enter a random building name: ")

            # Build the story using an f-string
            story = (
                f"Today, I saw a {adjective} {noun} that decided to {verb} {adverb}.\n"
                f"I couldn't believe my eyes! It was amazing how they managed to travel"
                f" {number2} miles in a matter of {number1} seconds. By the time they finished {verb}" 
                f" they were at {noun2}, amazing right!"
            )

            print("\nHere is your story:")
            print(story)
            print("Would you like to play again?")
            play_again = input("Enter Yes or No: ")

else:
    print("Nice playing with you!")
    exit

