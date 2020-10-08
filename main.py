# imports
from instapy import InstaPy
from instapy import smart_run
import time
import  random

# login credentials
insta_username = ''  # <- enter username here
insta_password = ''  # <- enter password here

#hashtag targeting
hashtags = ['']]

# target list
target_list = ['']
# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=4590,
                                    min_followers=45,
                                    min_following=77)

    

    # activity
    i = 0
    while i < 3:
        session.follow_user_followers(target_list, amount=35, randomize=False, interact=False, sleep_delay=random.randint(60, 75))
        session.like_by_tags(random.sample(hashtags, 4), amount=random.randint(1,20))
        i += 1
    