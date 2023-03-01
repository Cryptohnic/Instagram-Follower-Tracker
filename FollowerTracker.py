import instaloader
import os

L=instaloader.Instaloader()

def login():
    global USER
    USER=input('\nThis program needs an Instagram account to login to.\nIt can get followers of private accounts that the inputted account follows and followers of all public accounts.\n\nEnter your username: ')
    L.interactive_login(USER)
    print(f'\nLogged in as {USER}\n')

def obtainUser():
    global USERNAME
    global CHECKING
    global PROFILE
    USERNAME=input(f'Whose followers do you want to check? (If checking own followers, just hit ENTER): ')
    if USERNAME.strip()=='':
        CHECKING='you'
        USERNAME=USER
    else:
        CHECKING=USERNAME
    print(f'\nLoading...\n')
    PROFILE=instaloader.Profile.from_username(L.context,USERNAME)

def checkDir():
    global COMPUTER
    COMPUTER=os.path.expanduser('~')[7:]
    if not os.path.exists(f'/Users/{COMPUTER}/Documents/FollowerChecker'):
        os.makedirs(f'/Users/{COMPUTER}/Documents/FollowerChecker')

def obtainFollowers():
    global follower_set
    follower_set=set()
    for follower in PROFILE.get_followers():
        follower_set.add(follower.username)

def readFile():
    global old_followers
    file=open(f'/Users/{COMPUTER}/Documents/FollowerChecker/{USERNAME}\'sfollowers.txt','r')
    old_followers=set(file.read().splitlines())
    file.close()
    file=open(f'/Users/{COMPUTER}/Documents/FollowerChecker/{USERNAME}\'sfollowers.txt','w')
    for follower in follower_set:
        file.write(f'{follower}\n')
    file.close()

def firstTime():
    file=open(f'/Users/{COMPUTER}/Documents/FollowerChecker/{USERNAME}\'sfollowers.txt','w')
    for follower in follower_set:
        file.write(f'{follower}\n')
    file.close()
    print(f'{len(follower_set)} people are following {CHECKING}')
    print(f'Followers list saved to {USERNAME}\'sfollowers.txt in Documents')
    print(f'\nStarted tracking {USERNAME}\'s followers.')

def printFollowers():
    new_followers=follower_set-old_followers
    for people in new_followers:
        print(f'{people} has followed {CHECKING}')
    if len(new_followers)==1:
        print(f'{1} person has followed {CHECKING}\n')
    else:
        print(f'{len(new_followers)} people have followed {CHECKING}\n')

def printUnfollowers():
    only_old_followers=old_followers-follower_set
    for people in only_old_followers:
        print(f'{people} has unfollowed {CHECKING}')
    if len(only_old_followers)==1:
        print(f'{1} person has unfollowed {CHECKING}')
    else:
        print(f'{len(only_old_followers)} people have unfollowed {CHECKING}')

def printNonReciprocators():
    print()
    following_set=set()
    for follower in PROFILE.get_followees():
        following_set.add(follower.username)
    not_following_back=following_set-follower_set
    for people in not_following_back:
        print(f'{people} is not following {CHECKING} back')
    print(f'\n{len(not_following_back)} people are not following {CHECKING} back')

def main():
    login()
    checkDir()
    obtainUser()
    obtainFollowers()
    if not os.path.exists(f'/Users/{COMPUTER}/Documents/FollowerChecker/{USERNAME}\'sfollowers.txt'):
        firstTime()
    else:
        readFile()
        printFollowers()
        printUnfollowers()
        print(f'\n{len(follower_set)} people are following {CHECKING}')
        print(f'Followers list saved to {USERNAME}\'s_followers.txt in Documents\n')
    if CHECKING=='you':
        reciprocators=input(f'Would you like to check who is not following you back? (y/n): ')
        if reciprocators.strip().lower()=='y':
            printNonReciprocators()

if __name__=='__main__':
    main()