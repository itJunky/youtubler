from googleapiclient.discovery import build
from config import token


def ytb_get_videos_list(q='arduino+dmx'):
    with build('youtube', 'v3', developerKey=token) as youtube:
        response = youtube.search().list(
                    q=q,
                    maxResults=3,
                    type='video',
                    part='id, snippet'
                ).execute()
    #for video in response['items']:
    #    print(video)

    return response['items']

