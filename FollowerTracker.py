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

import instaloader # Crazy cool module very useful for instagram automation
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
follow_list=[]
for follower in profile.get_followers():
    follow_list.append(follower.username)
if not os.path.exists(f'/Users/{COMPUTER}/Documents/FollowerChecker/{CHECKING}\'sfollowers.txt'):
    file=open(f'/Users/{COMPUTER}/Documents/FollowerChecker/{CHECKING}\'sfollowers.txt','w+')
    for follower in follow_list:
        file.write(f'{follower}\n')
    file.close()
    print(f'{len(follow_list)} people are following {CHECKING}')
    print(f'Followers list saved to {CHECKING}\'sfollowers.txt in Documents')
    print(f'\nStarted tracking {CHECKING}\'s followers.')
else:
    file=open(f'/Users/{COMPUTER}/Documents/FollowerChecker/{CHECKING}\'sfollowers.txt','r')
    old_followers=file.readlines()
    file.close()
    file=open(f'/Users/{COMPUTER}/Documents/FollowerChecker/{CHECKING}\'sfollowers.txt','w+')
    for follower in follow_list:
        file.write(f'{follower}\n')
    file.close()
    file=open(f'/Users/{COMPUTER}/Documents/FollowerChecker/{CHECKING}\'sfollowers.txt','r')
    new_followers=file.readlines()
    file.close()
    new_followers_set=set(new_followers)-set(old_followers)
    for people in new_followers_set:
        print(f'{people[0:-1]} has followed {USERNAME}')
    if len(new_followers_set)==1:
        print(f'{1} person has followed {USERNAME}\n')
    else:
        print(f'{len(new_followers_set)} people have followed {USERNAME}\n')
    old_followers_set=set(old_followers)-set(new_followers)
    for people in old_followers_set:
        print(f'{people[0:-1]} has unfollowed {USERNAME}')
    if len(old_followers_set)==1:
        print(f'{1} person has unfollowed {USERNAME}')
    else:
        print(f'{len(old_followers_set)} people have unfollowed {USERNAME}')
    print(f'\n{len(new_followers)} people are following {USERNAME}')
    print(f'Followers list saved to {CHECKING}\'s_followers.txt in Documents\n')