#!/usr/bin/env python3
import sys, random
print("Добро пожаловать в 'Подбор имен для напарника.' как в сериале'Ясновидец'\n")

print("Имя, наподобие того, которое Шин подбирал для Гаса:\n\n")

first = ('Baby Oil1', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
"Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite' ",
'Butterbean', 'Buttermilk', 'Buttocks', 'Chad',
'Chesterfield', 'Chewy', 'Chigger", "Cinnabuns', 'Cleet',
'Cornbread', 'Crab Meat', 'Crapps', 'Dark Skies',
'Dennis Clawhammer', 'Dicman', 'Elphonso', 'Fancypants',
'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"',
'Mergatroid', '"Mr Peabody"', 'Oil-Сап', 'Oinks',
'Old Scratch', 'Ovaltine', 'Pennywhistle', 'Pitchfork Ben',
'Potato Bug', 'Pushmeet','Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut', "Sid 'The Squirts'",
'Skidmark', 'Slaps', 'Snakes', 'Snoobs', 'Snorki',
'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky', 'Storyboard',
'Sweet Tea', 'TeeTee', 'Wheezy Joe', "Winston ’Jazz Hands’",
'Worms ')

last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple',
'Goodensmith', 'Goodpasture', 'Guster', 'Henderson',
'Hooperbag', 'Hoosenater', 'Hootkins', 'Jefferson', 'Jenkins',
'Jingley-Schmidt', 'Johnson', 'Kingfish', 'Listenbee',
"M’Bernbo", 'McFadden', 'Moonshine', 'Nettles', 'Noseworthy',
'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf', 'Oxhandler',
'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow', 'Pinkerton',
'Porkins', 'Putney', 'Quakenbush', 'Rainwater', 'Rosenthal',
'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern', 'Stevens',
'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins',
'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger',
'Weewax', 'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch',
'Winterkorn', 'Woolysocks')
try_again = ""
while try_again.lower() != "n":
    first_name = random.choice(first)
    last_name = random.choice(last)
    print("{} {}".format(first_name, last_name), file=sys.stderr)
    print("\n\n")
    try_again = input("\n\nПопробуете еще? (Нажмите Enter либо n, чтобывыйти)\n")
