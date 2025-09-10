print("wlcome to the Manga reader Recomender")
print("Answer a few questions to find your next read")
genre = input("What genre do you like?(Sci-fi,Adventure,Thriller):")

if genre == "Sci-fi":
    length = input("How long the mangga should be? (short, medium, long):")
    
    if length == "short":
        Style = input("Which style do you prefer(animation,In real life)?: ")

        if Style == "animation":
            print("We recomend:Hotel-by Boichi ")
        if Style == "In real life":
            print("We Recomend:Abara-by Tsutomu Nihei ")

    elif length == "medium":
        Style = input("Which style do you prefer(animation,In real life)?: ")

        if Style == "animation":
            print("We recomend:Battle Angel Alita-by Yukito kishiro ")
        if Style == "In real life":
            print("We Recomend:Pluto-by Naoki Urusawa ")

    elif length == "long":
        Style = input("Which style do you prefer(animation,In real life)?: ")

        if Style == "animation":
            print("We recomend:Akira-by Katsuhiro Otomo ")
        if Style == "In real life":
            print("We Recomend:20th Century Boys-by Naoki Urusawa ")
    else:
        print("Invalid")

elif genre == "Adventure":
    length = input("How long the mangga should be? (short, medium, long):")
    
    if length == "short":
        Style = input("Which style do you prefer(animation,In real life)?: ")

        if Style == "animation":
            print("We recomend:Dragon ball: Episode of Bardlock ")
        if Style == "In real life":
            print("We Recomend:The summer of the Gods-by Jiro Tanaguchi ")

    elif length == "medium":
        Style = input("Which style do you prefer(animation,In real life)?: ")

        if Style == "animation":
            print("We recomend:Made in abyss-by Akihito Tsukushi ")
        if Style == "In real life":
            print("We Recomend:Golden Kamuy-by Satoru Noda ")

    elif length == "long":
        Style = input("Which style do you prefer(animation,In real life)?: ")

        if Style == "animation":
            print("We recomend:One Piece-by Eichiro Oda ")
        if Style == "In real life":
            print("We Recomend:Vagabond-by Takehiko Inoue ")
    else:
        print("Invalid")

elif genre == "Thriller":
    length = input("How long the mangga should be? (short, medium, long):")
    
    if length == "short":
        Style = input("Which style do you prefer(animation,In real life)?: ")

        if Style == "animation":
            print("We recomend:Death note:Another note-by The Los angeles BB murder Cases  ")
        if Style == "In real life":
            print("We Recomend:I Am Hero In Osaka ")

    elif length == "medium":
        Style = input("Which style do you prefer(animation,In real life)?: ")

        if Style == "animation":
            print("We recomend:Demi-Human-by Gamon Sakurai ")
        if Style == "In real life":
            print("We Recomend:Monster-by Naoki Urusawa ")

    elif length == "long":
        Style = input("Which style do you prefer(animation,In real life)?: ")

        if Style == "animation":
            print("We recomend:Death note-by Tsugumi Ohba & Takeshi Obata ")
        if Style == "In real life":
            print("We Recomend:Santuary-by Sho Fumimura & Ryoichi Ikegami ")
    else:
        print("Invalid")