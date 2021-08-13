#mad libs generator v2: has random!!
'''this is a python mad libs generator, more advanced than my previous version
hoping to add random story pieces with the rand methods and lists'''
import random
#ok setup time. here are the rando bits of story i got for ya


expo = ['Once upon a time there was a ', 'A long time ago in a galaxy far far away, a creature called a ','1 million years in the future, there will be a ']
joint1 = [' whose best friend was a ', ' whose archrival was a behemoth called ', ' who went to school with a ']
act1 = ['. One day they had a huge fight, which ended with both of them ', '. A mutual friend came out of the trees, rendering them both ', '. They went to the library together, despite their differences but the librarian made them ']
act2 = ['Despite their problems, they trekked on. They decided to ', 'Years later, it happened again. This time, they responded by ', 'This devastated both of them and so they went to go ']
ending = ['Although they had been through a lot together, they never spoke again.', 'They remained friends for the rest of their lives', 'Years later, they told this story to all their grandchildren, together.']


#let's call for some user input yo
noun1 = input('Please input a noun')
noun2 = input('input a creature')
noun3 = input('enter a weapon')
state = input('enter a state of being')
verb1 = input('enter an ING verb')




#story time friends
print(random.choice(expo)+ noun1 + random.choice(joint1) + noun2 + random.choice(act1) + state)
print(random.choice(act2) + verb1 + ' with '+ noun3 + random.choice(ending))
