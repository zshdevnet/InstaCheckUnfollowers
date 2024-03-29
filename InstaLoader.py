import instaloader
import pandas as pd
from decouple import config

# Creating an instance of the Instaloader class
bot = instaloader.Instaloader()
 
# Loading the profile from an Instagram handle
profile = instaloader.Profile.from_username(bot.context, config('InstaUserName'))
print(profile)

print("Username: ", profile.username)
print("User ID: ", profile.userid)
print("Number of Posts: ", profile.mediacount)
print("Followers Count: ", profile.followers)
print("Following Count: ", profile.followees)
print("Bio: ", profile.biography)
print("External URL: ", profile.external_url)