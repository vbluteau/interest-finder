import random
import sys
from paid_activities import *
from free_activities import * 

command = sys.argv[1]

free_activities = [play_games, go_walking, search_for_festivals, bonfire, go_drive, ride_bike,]

paid_activities = [eat_out, purchase_furniture, go_to_mall, go_to_movie, go_to_museum, farmers_market, concert,]

if command == "free_activity":
    random.choice(free_activities)()
elif command == "paid_activity":
    random.choice(paid_activities)()
else:
    print("I need the correct argument.")


