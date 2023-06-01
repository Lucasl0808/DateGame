﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define raven = Character("Raven")
define you = Character("[name]")

image ravendefault = "images/ravendefault.png"
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

    "You arrive at the carnival with Raven."
    scene carnival at center:
        zoom 7
        "carnival.png"
    play sound "carnival.mp3"

    show ravendefault at center:
        zoom 0.5

    # These display lines of dialogue.

    raven "Hey [you], glad you could make it, how was your sleep?"

    menu:
        "Hey Raven, it was alright! How about yours?":
            jump carnival_route

        "Hi... uh, it was good.":
            jump suspicious_route
    
    label suspicious_route:
        $sus_points += 1
        hide ravendefault
        show ravensurprised at center:
            zoom 0.5
        "An interesting first question to be asked. It seems normal at first but its just a bit of an odd choice..."
        raven "Good. I'm glad."
        raven "Let's go to the Ferris wheel and enjoy the view."

        menu:
            "I'm good, ferris wheels are kinda boring":
                hide ravensurprised
                show ravenannoyed at center:
                    zoom 0.5
                $sus_points += 1
                raven "What?! I love ferris wheels, they give us such a nice view! I'm going regardless."
                you "Ok fine I'll go with you"
                hide ravenannoyed
                show ravenblush at center:
                    zoom 0.5
                raven "Great! lets go!"
                jump ferris_wheel
            "Sure! lets go check it out!":
                hide ravensurprised
                show ravenblush at center:
                    zoom 0.5
                raven "Great! I love that we're on the same page"
                jump ferris_wheel

        
    label carnival_route:
        hide ravenblush
        show ravenhappy at center:
            zoom 0.5
        raven "Mine was great!"
        raven "Hey let's go to the Ferris wheel! I want to see the view from the top."
        hide ravenhappy
        show ravendefault at center:
            zoom 0.5
        menu:
            "I'm good, ferris wheels are kinda boring":
                hide ravendefault
                show ravenannoyed at center:
                    zoom 0.5
                $sus_points += 1
                raven "What?! I love ferris wheels, they give us such a nice view! I'm going regardless."
                you "Ok fine I'll go with you"
                hide ravenannoyed
                show ravenblush at center:
                    zoom 0.5
                raven "Great! lets go!"
                jump ferris_wheel
            "Sure! lets go check it out!":
                hide ravendefault
                show ravenblush at center:
                    zoom 0.5
                raven "Great! I love that we're on the same page"
                jump ferris_wheel

    label ferris_wheel:

        "Raven and I get on the Ferris wheel."
        "The city lights grew smaller and smaller as we rose up into the darkened sky."
        hide ravenblush
        show ravendefault at center:
            zoom 0.5

        raven "I love this view! It's so peaceful and this breeze is to die for."

        you "I agree, it really is something else."

        "Like anyone does, I of course stalked Raven on social media to find out what I was getting into."
        "...But one thing I noticed was that she has barely any presence online. I found almost nothing on her."
        menu:

            "So, do you have social media or anything?":
                $sus_points += 1
                jump suspicious_route2

            "What do you like to do on your free time?":
                jump carnival_route2

    
    label suspicious_route2:
        hide ravendefault
        show ravensad at center:
            zoom 0.5
        raven "Oh, I don't really like social media. I don't want everyone to be all up in my business you know."
        "that felt like a sore topic, and things got more awkward..."
        you "Yeah I can see that, it can get pretty invasive and toxic."
        hide ravensad
        show ravendefault at center:
            zoom 0.5
        jump movie
        
    label carnival_route2:
        hide ravendefault
        show ravenhappy at center:
            zoom 0.5
        raven "Hmm... lately I've been really into cooking!"
        raven "There's just something so satisfying about putting in the work to feed yourself when hungry."
        you "Wow, I wish I could cook, lately it's just been takeout for me"
        you "I buy groceries, but I don't even know what I could make. I've failed too much..."
        raven "I could come over and see what I can make for you! I'm pretty good at improvising."
        hide ravenhappy
        show ravenblush at center:
            zoom 0.5
        you "You'd do that? That would be great! A homecooked meal is a dream come true."
        jump movie

    label movie:
        raven "So what geres of shows do you like to watch?"
        menu:
            "Crime shows":
                $sus_points += 1
                jump suspicious_route3
            "Anime":
                jump normal_route3
            "I don't watch TV":
                jump endingChoice
            "Comedies":
                jump endingChoice2

    label suspicious_route3:
        hide ravendefault
        show ravensurprised at center:
            zoom 0.5
        raven "I see."
        you "... Yeah, I think it's pretty interesting, getting into the minds of all those people and seeing why they did it."
        raven "Why don't we head to my place and watch some later tonight?"
        raven "I've never seen anything like that show."
        you "Sure. I'd be happy to share my interests!"
        "insert path to bad ending"
        return

    label normal_route3:
        hide ravendefault
        show ravensurprised at center:
            zoom 0.5
        raven "Woah you're into anime? That's sick! I've also been trying to catch up on Demon Slayer."
        raven "My roommate actually broke our TV though, so I haven't been able to watch anything on a bigger screen."
        you "Damn that sucks. If you want to, we can watch the new episode at my place after this."
        hide ravensurprised
        show ravenblush at center:
            zoom 0.5
        raven "Sounds great!"
        "insert path to good ending"
        return

    label endingChoice:
        hide ravendefault
        show ravensurprised at center:
            zoom 0.5
        raven "Wait you don't watch any TV!?"
        raven "I should show you some good shows or movies"
        hide ravensurprised
        show ravenhappy at center:
            zoom 0.5
        you "Sounds great! We can watch some at:"
        menu:
            "my place":
                you "my place later!"
                hide ravenhappy
                show ravenblush at center:
                    zoom 0.5
                raven "Sure! I'd be glad to go to your place!"
                "insert path to good ending"
                return
            "her place":
                you "your place, if you can"
                hide ravenhappy
                show ravensurprised at center:
                    zoom 0.5
                raven "MY place!? I..."
                raven "uh..."
                hide ravensurprised
                show ravenblush at center:
                    zoom 0.5
                raven "Sure...! Lets do my place"
                "insert to bad ending"
                return

    label endingChoice2:
        hide ravendefault
        show ravensurprised at center:
            zoom 0.5
        raven "Woah you don't seem like the kind of guy to watch comedies"
        you "Yeah I have a funny bone in me..."
        hide ravensurprised
        show ravenhappy at center:
            zoom 0.5
        raven "Yeah I guess people like what they like, I haven't seen many comedies"
        you "I can show you a couple of my favorites if you have time"
        raven "I have time right now, where do you want to go?"
        menu:
            "my place":
                you "We can go to my place"
                hide ravenhappy
                show ravenblush at center:
                    zoom 0.5
                raven "Sure! I'd be glad to go to your place!"
                "insert path to good ending"
                return
            "her place":
                you "your place, if you can"
                hide ravenhappy
                show ravensurprised at center:
                    zoom 0.5
                raven "MY place!? I..."
                raven "uh..."
                hide ravensurprised
                show ravenblush at center:
                    zoom 0.5
                raven "Sure...! Lets do my place"
                "insert to bad ending"
                return
    # This ends the game.

    return
