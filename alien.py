alien_0 = {'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
alien_1 = {}
alien_1['color'] = 'red'
alien_1['points'] = '20'
print(alien_1)
print('--------------------------------')
favourite_languages = {
'jen': 'python',
'sarah': 'c++',
'mike': 'ruby',
'phil': 'python',
}
for name in favourite_languages.keys():
    print(name.title())
print('--------------------------------')
for name in favourite_languages:
    print(name.title())
print('--------------------------------')
friends = ['phil', 'sarah']
for name in favourite_languages.keys():
    print(name.title())

    if name in friends:
        print("  Hi " + name.title() + 
            ", I see your favoutite language is " +
            favourite_languages[name].title() + "!")
print('--------------------------------')
for name in sorted(favourite_languages.keys()):
    print(name.title() + ", thank you for taking the poll")