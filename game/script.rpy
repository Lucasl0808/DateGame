# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define raven = Character("Raven")
define you = Character("[name]")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    $sus_points = 0

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    python:
        name = renpy.input("Enter Your Name:")

        name = name.strip() or "You"

    "You arrive at the carnival with Raven"

    play sound "carnival.mp3"

    show sk

    # These display lines of dialogue.

    raven "Hey [you], glad you could make it, how was your sleep?"

    menu:
        "Hey Raven, it was alright! How about yours?":
            jump carnival_route

        "Hi... uh, it was good":
            jump suspicious_route
    
    label suspicious_route:
        $sus_points += 1
        "An interesting first question to be asked. It seems normal at first but its just a bit of an odd choice"
        raven "Good. I'm glad"
        raven "Let's go to the Ferris wheel and enjoy the view"
        jump ferris_wheel
        
    label carnival_route:

        raven "Mine was great!"
        raven "Hey lets go to the Ferris wheel! I want to see the view from the top"
        jump ferris_wheel

    label ferris_wheel:

        "Raven and I go ahead and get on the Ferris wheel"
        "The city lights grew smaller and smaller as we rose up into the darkened sky"

        raven "I love this view from the top! It's so peaceful and this breeze is to die for"

        you "I agree, it really is something else"

        "Like anyone does, I of course stalked Raven on social media to find out anything else about her"
        "One thing I noticed was that she has barely any presence online. I found almost nothing on her"
        menu:

            "So, do you have social media or anything?":
                $sus_points += 1
                jump suspicious_route2

            "What do you like to do on your free time?":
                jump carnival_route2

    
    label suspicious_route2:
        raven "Oh, I don't really like social media. I don't want everyone to be all up in my business you know"
        "that felt like a sore topic, and things got more awkward"
        you "Yeah I can see that, it can get pretty invasive and toxic"
        raven "Yeah... So have you been watching anything new lately?"
        menu:
            "True Crime":
                $sus_points += 1
                jump suspicious_route3
            "Demon Slayer":
                jump normal_route3
    
    label carnival_route2:
        raven "Hmm... lately I've been really into cooking!"
        raven "There's just something so satisfying about putting in the work to feed yourself when hungry"
        you "Wow, I wish I could cook, lately it's just been takeout for me"
        you "I buy groceries for what, I don't even know what I could make"
        raven "I could come over and see what I can make for you! I'm pretty good at improvising"
        you "You'd do that? That would be great! Money has been pretty tight for me lately"
        "go to good ending"

    label suspicious_route3:
        raven "I see"
        you "... Yeah, I think it's pretty interesting, getting into the minds of all those people and seeing why they did it"
        raven "Why don't we head to my place and watch some later tonight?"
        raven "I've never seen anything like that show"
        you "Sure. I'd be happy to share my interests"
        "go to bad ending"
        return

    label normal_route3:
        raven "Woah you're into anime? That's sick! I've also been trying to catch up on Demon Slayer"
        raven "my roommate actually broke our TV though, so I haven't been able to watch anything on a bigger screen"
        you "Damn that sucks. If you want to, we can watch the new episode at my place after this"
        raven "Sounds great!"
        "go to good ending"
        return

    # This ends the game.

    return
