import pandas as pd
import numpy as np
 
#if you don't know the column names 
followers = pd.read_csv("followers.csv")
followings = pd.read_csv("followings.csv")


followersList = followers['0'].tolist()
followingsList = followings['0'].tolist()
MyUnfollowers = []

for i in followingsList:
    if i not in followersList:
        MyUnfollowers.append(i)

print(MyUnfollowers, len(MyUnfollowers))