anime = []
while True:
    title = input("Enter the title of an anime (or type 'exit' to finish): ")
    if title.lower() == 'exit': 
        print('You have exited the anime entry.')
        break
    elif title:
        anime.append(title)
        print(f"'{title}' has been added to your anime list")
print(f'Your anime list includes:\n- ' + '\n- '.join(anime))
