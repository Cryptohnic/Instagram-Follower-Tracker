# Instagram-Follower-Tracker
Python program that will track Instagram followers telling you when someone follows or unfollows.

THIS IS MADE FOR MACOS ONLY
This program is used to see names of accounts who have followed and who have unfollowed Instagram accounts recently.
This will also work for private accounts under 2 conditions.
1. You log in with the private account you want to check
2. The account you use to log in is following the private account you want to check.
If the account is public that you want to check, you can login with any account and
still check said accounts followers.
The code works by storing a set of all the followers that an account has in the Documents folder
of a MacOS computer
The next time the code is run, it will compare current followers to the followers we saved originally. 
If the new followers is missing someone from the old followers, that means they unfollowed and that is 
output to the user. Vice versa is true for followers.
