import instaloader
from instaloader import Profile, Post
instance = instaloader.Instaloader()

post = Post.from_shortcode(instance.context, "Bxe5w5EAjDS")
instance.download_post(post,target="folderName")
##################
instance.download_hashtag(hashtag="your_hashtag_here",max_count=10)
##################
instance.login(user="your_username",passwd="your_password")
profile = Profile.from_username(instance.context, username="username_of_interest")

for highlight in instance.get_highlights(user=profile):
    # highlight is a Highlight object
    for item in highlight.get_items():
        # item is a StoryItem object
        instance.download_storyitem(item, '{}/{}'.format(highlight.owner_username, highlight.title))

##################
instance.login(user="your_username",passwd="your_password")
profile = Profile.from_username(instance.context, username="username_here")
instance.download_stories(userids=[profile.userid],filename_target='{}/stories'.format(profile.username))

###############

instance.login(user="your_username",passwd="your_password")
instance.download_saved_posts()
###############

instance.login(user="your_username",passwd="your_password")
instance.download_profile(profile_name="username_here")<LeftMouse>
