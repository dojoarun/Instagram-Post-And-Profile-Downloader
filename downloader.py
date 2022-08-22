import instaloader
from instaloader import Profile, Post
instagramUserName = input("Enter Username : ")
instagramPassword = input("Enter Password : ")
targetUserName = input("Enter Target Username : ")
instance = instaloader.Instaloader()
instance.login(user=instagramUserName,passwd=instagramPassword)
instance.download_profile(profile_name=targetUserName)
