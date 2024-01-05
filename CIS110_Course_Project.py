print(f"Hi, there!  I have an exciting story about a runaway dog.  I can't wait to tell it. ")
print(f"Before the story begins, I have a few questions I need you to answer.")
print(f"After typing your answer, be sure to press the enter key.")
input(f"\nPress the enter key to continue...")

keepPlaying = "yes"
while keepPlaying.lower() == "yes":

    #5 Questions Before the story begins
    _breed = input(f"\nWhat breed is the runaway dog:  ")
    while len(breed) == 0:
        breed = input(f"Please enter a breed:  ")
    #Second Question
    dogName = input(f"What is the runaway dog's name:  ")
    while len(dogName) == 0:
        dogName = input(f"Please enter a dog's name:  ")
    #Third Question
    city = input(f"What major city do you live nearby:  ")
    while len(city) == 0:
        city = input(f"Please enter a city:  ")
    #Fourth Question
    restaurant = input(f"What is your favorite restaurant:  ")
    while len(restaurant) == 0:
        restaurant = input(f"Please enter a restaurant:  ")
    #Fifth Question
    number = input(f"What is your favorite number:  ")
    while not number.isdigit():
        number = input(f"Value not recognized. Please enter a numeric value:  ")

    #Story Start
    print(f"\nLET'S GO!!!")
    print(f"\nOnce upon a time there was a beautiful {breed} named {dogName}. ")
    print(f"{dogName} always wanted to go outside and explore {city}. ")
    print(f"Today was {dogName}'s chance.  The gate was accidently left open! ")
    print(f"{dogName} ran out the gate heading straight towards the city. ")
    print(f"While walking down the street, {dogName} arrived at {restaurant}.  He always wanted to eat there. ")
    
    #Decision 1
    sneakIntoRestaurant = input(f"\nShould {dogName} sneak into the restaurant?  Type yes or no:  ")
    while sneakIntoRestaurant.lower() != "yes" and sneakIntoRestaurant.lower() != "no":
        sneakIntoRestaurant = input("Please type yes or no:  ")

    if sneakIntoRestaurant == "yes":
        print(f"\n{dogName} sneaks into {restaurant}'s kitchen through the backdoor. ")
        print(f"When the chef notices and tries to remove the dog, the dog jumps into the lobby. ")
        print(f"and starts jumping on customer tables knocking everything over in it's path. ")
        print(f"Customers start screaming and call the police. ")
        print(f"{dogName} managed to eat {number} plates of food. ")
        print(f"Luckily, he managed to escape before the police arrived. ")
    else:
        print(f"\n{dogName} decides it's too risky to sneak into {restaurant}'s kitchen. ")
        print(f"Being too afraid of getting caught, the dog instead digs through")
        print(f"the dumpster in the back for {number} minutes. ")
        print(f"Unfortunately, there was nothing good in the dumpster to eat. ")
        print(f"Therefore,{dogName} descides to leave and keep exploring the city. ")

    print(f"After a hot long day exploring {city}, {dogName} sees a car wash. ")
    print(f"The car wash looks very fun and refreshing! ")
    
    #Decision 2
    walkThroughCarWash = input(f"\nShould {dogName} walk through the car wash? Type yes or no:  ")
    while walkThroughCarWash.lower() != "yes" and walkThroughCarWash.lower() != "no":
        walkThroughCarWash = input("Please type yes or no:  ")

    if walkThroughCarWash == "yes":
        print(f"\n{dogName} walks up to the car wash. ")
        print(f"When he walks in, he trips the motion activated laser starting the car wash. ")
        print(f"First he was scared, but he ends up having the time of his life playing in the water. ")
        print(f"He goes through the car wash {number} of times. ")
        print(f"Amazingly, no one notices the dog at the car wash. ")
    else:
        print(f"\nHe decides not to go near the car wash. {breed} get scared easily. ")
        print(f"Being too afraid of all the moving parts and thinking someone might call the police,")
        print(f"{dogName} decides to just keep walking trying not to make a scene. ")

    #Alternate Endings
    if sneakIntoRestaurant == "yes" and walkThroughCarWash == "yes":
        print(f"\nAfter spending a day in {city}, sneaking into {restaurant} and walking through the car wash, ")
        print(f"{dogName} was caught by the police. ")
        print(f"Luckily, the police noticed your name written on the tag hanging from the dog's collar. ")
        print(f"{dogName} was successfully returned home with a full belly and that new car smell! ")
    elif sneakIntoRestaurant == "no" and walkThroughCarWash == "no":
        print(f"\nAfter spending a day in {city}, {dogName} was found by the police. ")
        print(f"Luckily, the police noticed your name on the collar tag. ") 
        print(f"{dogName} was successfully returned home to his owner. ")
        print(f"The police couldn't believe how well behaved {dogName} was all day long. ")    
    else:
        print(f"\nAfter spending a day in {city}, {dogName} was caught by the police. ")
        print(f"Luckily, the police noticed your name on the collar tag. ")
        print(f"{dogName} was successfully returned home to his owner. ")
        print(f"The police know idea {dogName} visited the restaurant or the carwash. ")
    print(f"\nThe End")
    
    keepPlaying = input(f"\nDo you want to play again? Enter yes or no:  ")
    while keepPlaying.lower() != "yes" and keepPlaying.lower() != "no":
        keepPlaying = input(f"Please type yes or no:  ")


