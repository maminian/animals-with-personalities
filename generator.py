import csv

with open('english-adjectives.txt','r') as f:
    csvr = csv.reader(f)
    adjectives = [a[0].lower() for a in csvr]
with open('animals.txt','r') as f:
    csvr = csv.reader(f)
    animals = [a[0].lower() for a in csvr]

nd = len(adjectives)
nn = len(animals)

prime1,prime2 = 24169,42061

def generate(integer,sep='_'):
    '''
    Generates a random codename from the files
    english-adjectives.txt and animals.txt.
    Uses a poor man's linear congruential generator to
    uniquely index the outputs.

    Optional input "sep" determines what to replace spaces with.
    Default: '_'
    '''
    # What is this monstrosity?
    # I can't fill the space of animals with this.
    # oh well.
    animal = animals[(prime1*integer + prime2)%nn]
    adjective = adjectives[(prime2*integer + prime1)%nd]
    #return adjective+' '+animal
    return (adjective+' '+animal).replace(' ', sep)
#

if __name__=="__main__":
    for i in range(10):
        print( generate_codename(i) )

# Output:
#
# warped sea snail
# dazzling beetle
# hot macaw
# pertinent wombat
# testy echidna
# bite-sized rainbow trout
# fluid anteater
# measly kingfisher
# short-term turkey
# winged crawdad
