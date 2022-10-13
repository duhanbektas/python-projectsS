import pandas as pd

df = pd.read_csv("datasets/youtube-ing.csv")

# 1- Display first 10 records
result = df.head(10)
# 2- Display 5 records starting from 5
result = df[5:20].head(5)
# 3- Display column names and how many columns are there on dataset
result = df.columns
result = len(df.columns)
# 4- Remove these columns from dataframe:
# (thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description)
df.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description","trending_date"],axis=1,inplace=True)
# 5- Display mean value for likes and dislikes
result = df["likes"].mean()
result = df["dislikes"].mean()

# 6- Display the title, likes and dislikes values of first 50 entry
result = df.head(50)[["title","likes","dislikes"]]

# 7- Display the most watched video
result = df[df["views"].max() == df["views"]]["title"].iloc[0]

# 8- Display the least watched video
result = df[df["views"].min() == df["views"]]["title"].iloc[0]

# 9- Display the 10 videos that are viewed the most
result = df.sort_values("views", ascending=False).head(10)[["title","views"]]

# 10- Display the mean values of likes based on category id
result = df.groupby("category_id").mean().sort_values("likes")["likes"]

# 11- Display the mean values of comments based on category id
result = df.groupby("category_id").sum().sort_values("comment_count", ascending = False)["comment_count"]

# 12- Display the count of videos on each category
result = df["category_id"].value_counts()

# 13- Create a new column to show the length of title on dataset
df["title_len"] = df["title"].apply(len)

# 14- Create a new column to display the count of "tags" used on the video for each data
# df["tag_count"] = df["tags"].apply(lambda x: len(x.split('|')))

def tagCount(tag):
    return len(tag.split('|'))

df["tag_count"] = df["tags"].apply(tagCount)

# 15- Based on like/dislike ratio, list the most popular videos

def likedislikeratio(dataset):
    likesList = list(dataset["likes"])
    dislikesList = list(dataset["dislikes"])

    commonList = list(zip(likesList,dislikesList))

    displayList = []

    for like,dislike  in commonList: 
        if (like + dislike) == 0:
            displayList.append(0)
        else:
            displayList.append(like/(like+dislike))

    return displayList
