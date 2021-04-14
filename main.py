from simpledemotivators import demcreate
from random import randint
import config
# debug: print(config.text)

if config.PICS_NUMBER >= len(config.text):
    print("Error text is lower, than your pics")
    exit(1)


first = True

for i in range(1, config.PICS_NUMBER+1):
    print("Making image #{}...".format(i))
    if first:
        dem = demcreate(config.START_TEXT)
        first = False
    else:
        dem = demcreate(config.text[i]*randint(4, 8))
    dem.makeImage('{path}/pic_{i}.jpg'.format(
                      path=config.PATH_PICS,
                      i=i-1
                  ),
                  RESULT_FILENAME='{path}/pic_{i}.jpg'.format(
                      path=config.PATH_PICS,
                      i=i)
                  )
    print("Image #{} saved".format(i))

print("Images done!")