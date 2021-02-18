facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0
#
# for post in facebook_posts:
#     # try to get the number of likes
#     try:
#         likes = post['Likes']
#     # catch an exception if likes key is not found
#     except KeyError:
#         likes = 0
#     else:
#         total_likes = total_likes + likes

# Another solution
for post in facebook_posts:
    try:
        total_likes = total_likes + post["Likes"]
    except:
        total_likes += 0
        # pass also works

print(total_likes)