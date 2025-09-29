print('PAROT SIMULATOR - THE ECHO CHAMBER!')
word = input('What do you want your parrot to say?')
times = eval(input('Hown many times the parrot should squawk it?'))

for x in range(times, 0, -1):
    print('🦜Squawk!',word)
