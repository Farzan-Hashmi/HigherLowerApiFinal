from time import sleep
import pandas as pd
from googleapiclient.discovery import build



def RandomYoutubeVideos():
    api_key = 'AIzaSyArVOc9O8i4CekkyyvyhEmIrh5PU3uC6PA'
    ids = []
    viewCounts = []

   
    categories = [2, 1, 17, 22, 23, 24, 25, 26, 28]

    try:
        for number in categories:
            youtube = build('youtube', 'v3', developerKey=api_key)
            request = youtube.videos().list(
                part='statistics',
                chart='mostPopular',
                maxResults=50,
                videoCategoryId=number
            )

            print("Category: " + str(number))

            response = request.execute()
            for i in range(0, 50):
                print(i)
                ids.append(response['items'][i]['id'])
                viewCounts.append(response['items'][i]['statistics']['viewCount'])

    except Exception as e:
        print(e)
        pass

    df = pd.DataFrame(list(zip(ids, viewCounts)),
                    columns=['video_id', 'num_views'])

    with pd.option_context('display.max_rows', 999):
        print(df)
    return(df)
