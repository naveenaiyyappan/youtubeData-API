#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install --upgrade google-api-python-client


# In[2]:


from googleapiclient.discovery import build


# In[3]:


Api_key="AIzaSyAaMNdWCIskZHlfMnGURgzW9fHA37be0iY"


# In[4]:


api_service_name = "youtube"
api_version = "v3"
youtube=build("youtube","v3",developerKey=Api_key)


# In[5]:


Channel_ids=['UCk3JZr7eS3pg5AGEvBdEvFg','UCHGktfcQq2BY_8tGPHwvm7g','UC-j7LP4at37y3uNTdWLq-vQ','UCs5zOg5Ad0QAkRPJsYiRm9g','UC_exm4hbJ2zV-4SrqrL9IRw','UC7RZIGGgAp8P4z354boxGtg','UCEdq6cRs1Jux6FuCl1zkwUw','UCAuhPbhpIDhUquHYkOPyX4w','UCZM82IdwJeS1''As0lPZu5_Xg','UC3aHdsm-cfKcLyVe1O8Xu6A']


# In[6]:


Api_key="AIzaSyAaMNdWCIskZHlfMnGURgzW9fHA37be0iY"
pi_service_name = "youtube"
api_version = "v3"
youtube=build("youtube","v3",developerKey=Api_key)
channel_id=Channel_ids
request = youtube.channels().list(
    part="snippet,contentDetails,statistics",
    id=channel_id
)
Cha1response = request.execute()


# In[7]:


Cha1response


# In[8]:


print(Cha1response.keys())


# In[9]:


Cha1response["items"]


# In[52]:


channel_information={ "channelName":response['items'][0]['snippet']["title"],
    "channel_description":response['items'][0]['snippet']["description"],
    "playlistId":response['items'][0]['contentDetails']['relatedPlaylists']['uploads'],
    "video":response["items"][0]["statistics"]["videoCount"],
    "subscribers":response["items"][0]["statistics"]["subscriberCount"],
    "views":response["items"][0]["statistics"]["viewCount"]
}


# In[11]:


channel_information={
    "channelName":Cha1response['items'][0]['snippet']["title"],
    "channel_description":Cha1response['items'][0]['snippet']["description"],
    "playlistId":Cha1response['items'][0]['contentDetails']['relatedPlaylists']['uploads'],
    "video":Cha1response["items"][0]["statistics"]["videoCount"],
    "subscribers":Cha1response["items"][0]["statistics"]["subscriberCount"],
    "views":Cha1response["items"][0]["statistics"]["viewCount"]
}


# In[36]:


channel_information


# In[131]:


playlist=["UUZM82IdwJeS1As0lPZu5_Xg,UUk3JZr7eS3pg5AGEvBdEvFg,UU3aHdsm-cfKcLyVe1O8Xu6A,UU-j7LP4at37y3uNTdWLq-vQ,UUs5zOg5Ad0QAkRPJsYiRm9g,UUHGktfcQq2BY_8tGPHwvm7g,UU_exm4hbJ2zV-4SrqrL9IRw,UU7RZIGGgAp8P4z354boxGtg,UUEdq6cRs1Jux6FuCl1zkwUw,UUAuhPbhpIDhUquHYkOPyX4w"]


# In[13]:


youtube = build("youtube","v3",developerKey=Api_key)
request = youtube.playlists().list(
    part="snippet,contentDetails",
    id="UU-j7LP4at37y3uNTdWLq-vQ,UUk3JZr7eS3pg5AGEvBdEvFg,UU_exm4hbJ2zV-4SrqrL9IRw,UUHGktfcQq2BY_8tGPHwvm7g,UUEdq6cRs1Jux6FuCl1zkwUw,UU7RZIGGgAp8P4z354boxGtg,UU3aHdsm-cfKcLyVe1O8Xu6A,UUs5zOg5Ad0QAkRPJsYiRm9g,UUAuhPbhpIDhUquHYkOPyX4w,UUZM82IdwJeS1As0lPZu5_Xg"
)
playlist = request.execute()


# In[14]:


print(playlist)


# In[15]:


playlist["items"]


# In[16]:


youtube = build("youtube","v3",developerKey=Api_key)
request = youtube.videos().list(
    part="snippet,contentDetails",
    id="BsLQx3tbhnI,hozPADLu53c,C-JTbeva6H8,F9ZjrHSb2s0,0dP4F1ZyRTA,sl5k6U5khKA,xGN1YM9gU5I,20cEEqv29iE,Y4W0cJvUno8,lFZaIiwfpfI"
)
videoid = request.execute()


# In[17]:


print(videoid)


# In[18]:


videoid["items"]


# In[19]:


def get_channel_videos(chennal_id):
    request = youtube.channels().list(id=channel_id,
                                      part="contentDetails").execute()
    playlist=request["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
    videos=[]
    next_page_token=None
    
    while 1:
        request = youtube.playlistItems().list(playlistId=playlist,
                                               part="snippet",
                                               maxResults=50,
                                               pageToken=next_page_token).execute()
        videos+=request["items"]
        next_page_token=request.get('nextPageToken')
        
        if next_page_token is None:
            break
    return videos
        


# In[20]:


videos = get_channel_videos(['UCk3JZr7eS3pg5AGEvBdEvFg','UCHGktfcQq2BY_8tGPHwvm7g','UC-j7LP4at37y3uNTdWLq-vQ','UCs5zOg5Ad0QAkRPJsYiRm9g','UC_exm4hbJ2zV-4SrqrL9IRw','UC7RZIGGgAp8P4z354boxGtg','UCEdq6cRs1Jux6FuCl1zkwUw','UCAuhPbhpIDhUquHYkOPyX4w','UCZM82IdwJeS1As0lPZu5_Xg','UC3aHdsm-cfKcLyVe1O8Xu6A'])


# In[21]:


len(videos)


# In[22]:


for video in videos:
    print(video["snippet"]["title"])


# In[23]:


videoIDS=["BsLQx3tbhnI",
           "hozPADLu53c",
           "C-JTbeva6H8",
           "F9ZjrHSb2s0",
           "0dP4F1ZyRTA",
           "sl5k6U5khKA",
           "xGN1YM9gU5I",
           "20cEEqv29iE",
           "Y4W0cJvUno8",
           "lFZaIiwfpfI"]


# In[44]:


Api_key="AIzaSyAaMNdWCIskZHlfMnGURgzW9fHA37be0iY"
pi_service_name = "youtube"
api_version = "v3"
youtube=build("youtube","v3",developerKey=Api_key)
request = youtube.commentThreads().list(
    part="snippet,replies",
    videoId="BsLQx3tbhnI"
)
comments= request.execute()


# In[45]:


print(comments)


# In[46]:


comments["items"]


# In[26]:


Api_key="AIzaSyAaMNdWCIskZHlfMnGURgzW9fHA37be0iY"
pi_service_name = "youtube"
api_version = "v3"
youtube=build("youtube","v3",developerKey=Api_key)
video_id="BsLQx3tbhnI"
comments=[]
request = youtube.commentThreads().list(
    part="snippet,replies",
    videoId=video_id
).execute()

while request:
    for item in request ["items"]:
        comment_information ={
            "Comment_Id":item["snippet"]["topLevelComment"]["id"],
            "Comment_Text":item["snippet"]["topLevelComment"]["snippet"]["textDisplay"],
            "Comment_Author":item["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"],
            "Comment_Published":item["snippet"]["topLevelComment"]["snippet"]["publishedAt"]
        }
        comments.append(comment_information)
        


# In[3]:


pip install pymongo


# In[12]:


from pymongo import MongoClient


# In[13]:


cloud_client=MongoClient("mongodb+srv://naveenaiyyappan:Rink@cluster0.od0r49h.mongodb.net/?retryWrites=true&w=majority")


# In[73]:


import json


# In[14]:


db=cloud_client["youtubedata"]


# In[82]:


mycoll0=db["channel"]


# In[30]:


mycoll2=db["playlist"]


# In[31]:


mycoll3=db["videos"]


# In[43]:


mycoll4=db["comment"]


# In[23]:


db=cloud_client["youtubeDB1"]


# In[24]:


mycol5=db["informationC"]


# In[25]:


mycol5.insert_one(channel_information)


# In[26]:


for i in mycol5.find():
    print(i)


# In[90]:


mycoll0.insert_one(Cha1response)


# In[91]:


for i in mycoll0.find():
    print(i)


# In[35]:


mycoll2.insert_one(playlist)


# In[36]:


for i in mycoll2.find():
    print(i)


# In[38]:


mycoll3.insert_one(video)


# In[40]:


for i in mycoll3.find():
    print(i)


# In[47]:


mycoll4.insert_one(comments)


# In[48]:


for i in mycoll4.find():
    print(i)


# In[ ]:





# In[49]:


import pandas as pd


# In[92]:


pd.DataFrame(list(Cha1response))


# In[54]:


pd.DataFrame(list(playlist))


# In[55]:


pd.DataFrame(list(video))


# In[57]:


pd.DataFrame(list(comments))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




