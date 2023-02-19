from googleapiclient.discovery import build
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests
from datetime import datetime

def get_subscriber_count(q):
    channel_id = "UC-lHJZR3Gqxm24_Vd_AJ5Yw"
    api_key='AIzaSyCOooVUvF7tiEAT9yZ5xLjSrKHa0_v9kTg'
    youtube = build('youtube', 'v3', developerKey=api_key)
     
    request = youtube.search().list(
         part='id,snippet',
        q=q,
        type='video',
       maxResults=50 )

    response = request.execute()

    #print(response)

    for item in response['items']:
        if q in item['snippet']['channelTitle']:
            channel_id=item['snippet']['channelId']
        #for key,value in item.items(): 
            #print(key,value)


        

    request = youtube.channels().list(
        part='snippet',
        id=channel_id,
        maxResults=1
    )

    responses = request.execute()


    profile_picture_url = responses['items'][0]['snippet']['thumbnails']['default']['url']


    request = youtube.channels().list(part="statistics", id=channel_id)
    respon = request.execute()
    subscriber_count = int(respon["items"][0]["statistics"]["subscriberCount"])
    return subscriber_count/1000000

def get_url(q):
    channel_id = "UC-lHJZR3Gqxm24_Vd_AJ5Yw"
    api_key='AIzaSyCOooVUvF7tiEAT9yZ5xLjSrKHa0_v9kTg'
    youtube = build('youtube', 'v3', developerKey=api_key)
     
    request = youtube.search().list(
         part='id,snippet',
        q=q,
        type='video',
       maxResults=50 )

    response = request.execute()

    #print(response)

    for item in response['items']:
        if q in item['snippet']['channelTitle']:
            channel_id=item['snippet']['channelId']
        #for key,value in item.items(): 
            #print(key,value)

    # Get image data from URL
    #response = requests.get(profile_picture_url)
    #image_data = response.content

    # Create directory for images if it doesn't exist
    #if not os.path.exists('static/img'):
        #os.makedirs('static/img')

    # Save image data as PNG file
    #with open("static/img/search.png", 'wb') as f:
        #f.write(image_data)

   
    def get_channel_stats(youtube, channel_id):
        request = youtube.channels().list(
            part="snippet,contentDetails,statistics",
            id=channel_id
        )
        response = request.execute()
        
        return response['items']


    def get_video_list(youtube, upload_id):
        video_list = []
        request = youtube.playlistItems().list(
            part="snippet,contentDetails",
            playlistId=upload_id,
            maxResults=50
        )
        next_page = True
        while next_page:
            response = request.execute()
            data = response['items']

            for video in data:
                video_id = video['contentDetails']['videoId']
                if video_id not in video_list:
                    video_list.append(video_id)

            
            if 'nextPageToken' in response.keys():
                next_page = True
                request = youtube.playlistItems().list(
                    part="snippet,contentDetails",
                    playlistId=upload_id,
                    pageToken=response['nextPageToken'],
                    maxResults=50
                )
            else:
                next_page = False

        return video_list


    def get_video_details(youtube, video_list):
        stats_list=[]

        # Can only get 50 videos at a time.
        for i in range(0, len(video_list), 50):
            request= youtube.videos().list(
                part="snippet,contentDetails,statistics",
                id=video_list[i:i+50]
            )

            data = request.execute()
            for video in data['items']:
                title=video['snippet']['title']
                published=video['snippet']['publishedAt']
                description=video['snippet']['description']
                if 'tags' in video['snippet'].keys():
                    tag_count= len(video['snippet'])
                else: 
                    tag_count = 0
                view_count=video['statistics'].get('viewCount',0)
                like_count=video['statistics'].get('likeCount',0)
                dislike_count=video['statistics'].get('dislikeCount',0)
                comment_count=video['statistics'].get('commentCount',0)
                stats_dict=dict(title=title, description=description, published=published, tag_count=tag_count, view_count=view_count, like_count=like_count, dislike_count=dislike_count, comment_count=comment_count)
                stats_list.append(stats_dict)

        return stats_list
         

    channel_stats = get_channel_stats(youtube, channel_id)
    upload_id = channel_stats[0]['contentDetails']['relatedPlaylists']['uploads']
    video_list = get_video_list(youtube, upload_id)
    video_data = get_video_details(youtube, video_list)
        
    embed_video = video_list[0]
    return embed_video


def getAll(q):
    channel_id = "UC-lHJZR3Gqxm24_Vd_AJ5Yw"
    api_key='AIzaSyCOooVUvF7tiEAT9yZ5xLjSrKHa0_v9kTg'
    youtube = build('youtube', 'v3', developerKey=api_key)
     
    request = youtube.search().list(
         part='id,snippet',
        q=q,
        type='video',
       maxResults=50 )

    response = request.execute()

    #print(response)

    for item in response['items']:
        if q in item['snippet']['channelTitle']:
            channel_id=item['snippet']['channelId']
        #for key,value in item.items(): 
            #print(key,value)


        

    request = youtube.channels().list(
        part='snippet',
        id=channel_id,
        maxResults=1
    )

    responses = request.execute()


    profile_picture_url = responses['items'][0]['snippet']['thumbnails']['default']['url']

    #print(response)

    for item in response['items']:
        if q in item['snippet']['channelTitle']:
            channel_id=item['snippet']['channelId']
        #for key,value in item.items(): 
            #print(key,value)

    # Get image data from URL
    response = requests.get(profile_picture_url)
    image_data = response.content

    # Create directory for images if it doesn't exist
    if not os.path.exists('static/img'):
        os.makedirs('static/img')

    # Save image data as PNG file
    with open("static/img/search.png", 'wb') as f:
        f.write(image_data)

    channel_ids = ['UCG8rbF3g2AMX70yOd8vqIZg', # Logan Paul
                   'UCi3OE-aN09WOcN9d2stCvPg', # Charli Damelio
                    'UCIwFjwMjI0y7PDBVEO9-bkQ', # Justin Bieber
                   'UCX6OQ3DkcsbYNE6H8uQQuVA', # Mr Beast
                   'UCBdw4dLCLLHmTgAOnW4V0hQ'#The Rock
                   'UC-lHJZR3Gqxm24_Vd_AJ5Yw'#PewDiePie
                  ]

    def get_channel_stats(youtube, channel_id):
        request = youtube.channels().list(
            part="snippet,contentDetails,statistics",
            id=channel_id
        )
        response = request.execute()
        
        return response['items']


    def get_video_list(youtube, upload_id):
        video_list = []
        request = youtube.playlistItems().list(
            part="snippet,contentDetails",
            playlistId=upload_id,
            maxResults=50
        )
        next_page = True
        while next_page:
            response = request.execute()
            data = response['items']

            for video in data:
                video_id = video['contentDetails']['videoId']
                if video_id not in video_list:
                    video_list.append(video_id)

            
            if 'nextPageToken' in response.keys():
                next_page = True
                request = youtube.playlistItems().list(
                    part="snippet,contentDetails",
                    playlistId=upload_id,
                    pageToken=response['nextPageToken'],
                    maxResults=50
                )
            else:
                next_page = False

        return video_list


    def get_video_details(youtube, video_list):
        stats_list=[]

        # Can only get 50 videos at a time.
        for i in range(0, len(video_list), 50):
            request= youtube.videos().list(
                part="snippet,contentDetails,statistics",
                id=video_list[i:i+50]
            )

            data = request.execute()
            for video in data['items']:
                title=video['snippet']['title']
                published=video['snippet']['publishedAt']
                description=video['snippet']['description']
                if 'tags' in video['snippet'].keys():
                    tag_count= len(video['snippet'])
                else: 
                    tag_count = 0
                view_count=video['statistics'].get('viewCount',0)
                like_count=video['statistics'].get('likeCount',0)
                dislike_count=video['statistics'].get('dislikeCount',0)
                comment_count=video['statistics'].get('commentCount',0)
                stats_dict=dict(title=title, description=description, published=published, tag_count=tag_count, view_count=view_count, like_count=like_count, dislike_count=dislike_count, comment_count=comment_count)
                stats_list.append(stats_dict)

        return stats_list
         

    channel_stats = get_channel_stats(youtube, channel_id)
    upload_id = channel_stats[0]['contentDetails']['relatedPlaylists']['uploads']
    video_list = get_video_list(youtube, upload_id)
    video_data = get_video_details(youtube, video_list)
    df=pd.DataFrame(video_data)
    df['title_length'] = df['title'].str.len()
    df["view_count"] = pd.to_numeric(df["view_count"])
    df["like_count"] = pd.to_numeric(df["like_count"])
    df["dislike_count"] = pd.to_numeric(df["dislike_count"])
    df["comment_count"] = pd.to_numeric(df["comment_count"])

    #df['published'] =  pd.to_datetime(df['published'], format='%Y-%m-%dT%H:%M:%SZ')

    #datetime_str = '2022-12-24T20:59:59Z'
    #datetime_obj = datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%SZ')
    #output_str = datetime_obj.strftime('%m-%Y')
    #print(output_str)  # Output: '12-2022'

    # Convert 'published' column to datetime objects
    df['published'] = pd.to_datetime(df['published'])

    # Create new column with formatted strings
    df['published'] = df['published'].dt.strftime('%m-%Y')


    data = df.copy()

    df_sorted = data[data['published'].str.contains('2022')].sort_values('published')

    df_sorted['published'] = pd.to_datetime(df_sorted['published'])

    df_sorted['published'] = df_sorted['published'].dt.strftime('%m')



    df_sorted['view_count'] = (df_sorted['view_count'] / 10000000)




    plot = sns.lineplot(x='published', y='view_count', data=df_sorted, errorbar=None)
    plot.set(title='Views per month in 2022', xlabel='Months in 2022', ylabel='Number of Views(in 10 Millions)')
    #plt.show()


    plot = sns.lineplot(x='published', y='view_count', data=df_sorted, errorbar=None)
    plot.set(title='Views per month in 2022', xlabel='Months in 2022', ylabel='Number of Views(in 10 Millions)')


    # Save the plot as an image
    filename = "static/img/data_image.png"
    plt.savefig(filename, dpi=300, bbox_inches='tight')







    #print(plt.plot(df_sorted["published"], df_sorted["view_count"]))


