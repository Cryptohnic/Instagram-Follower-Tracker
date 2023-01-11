# THIS IS MADE FOR MACOS ONLY
# This program is used to see names of accounts who have followed and who have unfollowed Instagram accounts recently.
# This will also work for private accounts under 2 conditions.
# 1. You log in with the private account you want to check
# 2. The account you use to log in is following the private account you want to check.
# If the account is public that you want to check, you can login with any account and
# still check said accounts followers.
# The code works by storing a set of all the followers that an account has in the Documents folder
# of a MacOS computer
# The next time the code is run, it will compare current followers to the followers we saved originally.
# If the new followers is missing someone from the old followers, that means they unfollowed and that is 
# output to the user. Vice versa is true for followers.

import instaloader # Cool module very useful for instagram automation
import os

# Login to instagram
L = instaloader.Instaloader()
USER=input('\nThis program needs an Instagram account to login to.\nIt can get followers of private accounts that the inputted account follows and followers of all public accounts.\n\nEnter your username: ')
L.interactive_login(USER)
print(f'\nLogged in as {USER}\n')

# Create directory for save data
COMPUTER=os.path.expanduser('~')[7:]
if not os.path.exists(f'/Users/{COMPUTER}/Documents/FollowerChecker'):
    os.makedirs(f'/Users/{COMPUTER}/Documents/FollowerChecker')

# Obtain profile metadata
CHECKING=input(f'Whose followers do you want to check? (If checking own followers, just hit ENTER): ')
USERNAME=CHECKING
if CHECKING.strip()=='':
    CHECKING=USER
    USERNAME='you'
print(f'\nLoading...\n')
profile=instaloader.Profile.from_username(L.context,CHECKING)

# Print list of followers
follower_set=set()
for follower in profile.get_followers():
    follower_set.add(follower.username)
if not os.path.exists(f'/Users/{COMPUTER}/Documents/FollowerChecker/{CHECKING}\'sfollowers.txt'):
    file=open(f'/Users/{COMPUTER}/Documents/FollowerChecker/{CHECKING}\'sfollowers.txt','w')
    for follower in follower_set:
        file.write(f'{follower}\n')
    file.close()
    print(f'{len(follower_set)} people are following {CHECKING}')
    print(f'Followers list saved to {CHECKING}\'sfollowers.txt in Documents')
    print(f'\nStarted tracking {CHECKING}\'s followers.')
else:
    file=open(f'/Users/{COMPUTER}/Documents/FollowerChecker/{CHECKING}\'sfollowers.txt','r+')
    old_followers=set(file.read().splitlines())
    new_followers=follower_set-old_followers
    for follower in follower_set:
        file.write(f'{follower}\n')
    file.close()
    for people in new_followers:
        print(f'{people} has followed {USERNAME}')
    if len(new_followers)==1:
        print(f'{1} person has followed {USERNAME}\n')
    else:
        print(f'{len(new_followers)} people have followed {USERNAME}\n')
    only_old_followers=old_followers-follower_set
    for people in only_old_followers:
        print(f'{people} has unfollowed {USERNAME}')
    if len(only_old_followers)==1:
        print(f'{1} person has unfollowed {USERNAME}')
    else:
        print(f'{len(only_old_followers)} people have unfollowed {USERNAME}')
    print(f'\n{len(follower_set)} people are following {USERNAME}')
    print(f'Followers list saved to {CHECKING}\'s_followers.txt in Documents\n')