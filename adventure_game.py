print("Welcome to the adventure game!")

first = input(
    "Once upon a time, on a very green land, lived an 18-year-old boy named Jarede. "
    "Jarede really liked adventures and outdoor activities, so one day he decided to go out and have a time with himself, "
    "but he had a dilema, and he didn't know what to do, he could go FISHING, to go HIKING, or to ride a BOAT. "
    "And now, it's up to you to decide what to do, type FISHING or HIKING to decide the next step."
).lower()

if first == "fishing":
    place = input("You chose to go fishing, now you have to choose a place to go fishing, RIVER or LAKE ").lower()
    if place == "lake":
        fish = input("You chose to go to a lake, now you have to choose a fish to catch, BASS or CATFISH ").lower()
        if fish == "bass":
            bass = input("You chose to catch a bass, now you have to choose a bait to catch the bass, WORM or NET ").lower()
            if bass == "worm":
                worm = input("OK worms, you don't have them on hands now, you can go to the fishing store and BUY them, or you can DIG a little hole and look for them ").lower()
                if worm == "buy":
                    print("That's good, go to the fishing store, buy your worms and have a good fishing time ")
                elif worm == "dig":
                    print("That's good, get a hoe dig a little hole and look for your worms ")
            elif bass == "net":
                net = input("OK nets, you don't have them on hands now, you can go to the fishing store and BUY them, or you can fish with WORMS ").lower()
                if net == "buy":
                    print("That's good, go to the fishing store, buy your net and have a good fishing time")
                elif net == "worms":
                    print("That's good, go to the fishing store, buy your worms and have a good fishing time")
        if fish == "catfish":
            catfish = input("You chose to catch a catfish, now you have to choose a bait to catch the catfish, STINKBAIT or BLUEGILLS").lower()
            if catfish == "stinkbait":
                print("That's good, go to the fishing store, buy your stinkbait and have a good fishing time")
            elif catfish == "bluegills":
                print("That's good, go to the fishing store, buy your bluegills and have a good fishing time")
    elif place == "river":
        color = input("You chose to go to a river, now you have to choose a boat to go, do you want a BROWN OR BLACK boat").lower() 
        if color == "brown":
            brown = input("You pick the brown boat, but it's a mile from you, will you go get it WALKING or by a CAR").lower()
            if brown == "walking":
                print("Good pick, walking is the best way to go")
            elif brown == "car":
                print("That's good, get in the car and go get the boat")
        elif color == "black":
            black = input("The black boat is broken, but you can FIX it or get the BROWN one").lower()
            if black == "FIX":
                print("That's good, go to the car and get the tools for fixing it")
            elif black == "brown":
                 brown = input("You pick the brown boat, but it's a mile from you, will you go get it WALKING or by a CAR").lower()
            if brown == "walking":
                print("Good pick, walking is the best way to go")
            elif brown == "car":
                print("That's good, get in the car and go get the boat")
                
elif first == "hiking":
    hike = input ("You chose to go hiking, now you have to choose a place to go hiking, CANION or MOUNTAIN").lower()  
    if hike == "canion":
        canion = input("Thats awesome canions have a great view, how are you going to register the adventure? with a CAMERA or with a CELLPHONE?").lower()
        if canion == "camera":
            camera = input("Ok, and what are you going to eat? are you taking a SNACK or a LUNCH?").lower()
            if camera == "snack":
                print("That's good, have a good time")
            elif camera == "lunch":
                print("That's good, have a good time")
        elif canion == "cellphone":
            cellphone = input("You have to take something to charge the cellphone in case the batery runs out, do you prefer a MOBILE batery or a mobile CHARGER? ").lower()
            if cellphone == "mobile":
                print("That's good, have a good time")
            elif cellphone == "charger":
                print("That's good, have a good time")
    elif hike == "mountain":
        mountain = input("Ok mountain, but how are you going to guide yourself? with a GPS or with a MAP? ").lower()
        if mountain == "gps":
                gps = input("Good, and what are you to take agains the mosquitos? a CREAM repellent or a SPRAY repellent? ").lower()
                if gps == "cream":
                    print("That's good, have a good time ")
                elif gps == "spray":
                    print("That's good, have a good time" )
        elif mountain == "map":
            map = input("Good, and what are you going to take in case you get lost? a FLARE gun or a SMOKE signal? ").lower()
            if map == "flare":
                print("That's good, have a good time ")
            elif map == "smoke":
                print("That's good, have a good time ")
else:
    print("Hey, you need to choose one of the 3 options")
