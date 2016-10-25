from django.shortcuts import render
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
from video.models import Video


DEVELOPER_KEY = "AIzaSyDiarbwPOxSkXmNPfdv8UtHcZM6KySpk34"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def youtube_search(keyword, page_token, max_results=10):
    """
    youtube_search함수 개선

    1. youtube_search 함수의 arguments에 pageToken 추가
    2. 받은 pageToken값을 youtube.search()실행 시 list의 인자로 추가
    3. search뷰에서 request.GET에 pageToken값을 받아오도록 설정
    4. template에서 이전페이지/다음페이지 a태그 href에 GET parameter가 추가되도록 설정
    """
    youtube = build(
        YOUTUBE_API_SERVICE_NAME,
        YOUTUBE_API_VERSION,
        developerKey=DEVELOPER_KEY
    )

    search_response = youtube.search().list(
        q=keyword,
        part="id,snippet",
        maxResults=max_results,
        pageToken=page_token,
        type='video'
    ).execute()

    videos = Video.objects.all()

    video_id_list = []
    for item in search_response['items']:
        video_id_list.append(item['id']['videoId'])
    str_id = ",".join(video_id_list)

    search_response2 = youtube.videos().list(
        part="id,snippet,statistics,contentDetails",
        id=str_id,
    ).execute()

    exist_list = Video.objects.filter(youtube_id__in=video_id_list)
    exist_id_list = [video.youtube_id for video in exist_list]
    for item in search_response2['items']:
        cur_video_id = item['id']
        if cur_video_id in exist_id_list:
            item['is_exist'] = True

    if search_response.get('prevPageToken'):
        search_response2['prevPageToken'] = search_response['prevPageToken']
    if search_response.get('nextPageToken'):
        search_response2['nextPageToken'] = search_response['nextPageToken']

    return search_response2