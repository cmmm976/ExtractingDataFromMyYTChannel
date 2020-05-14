# -*- coding: utf-8 -*-

import os
import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/youtube']

API_SERVICE_NAME = 'youtubeAnalytics'
API_VERSION = 'v2'
CLIENT_SECRETS_FILE = 'code_secret_client_CENSORED-q9a8cohev91q75c8qskfmqmibojae7ah.apps.googleusercontent.com.json'
RESULTS = open("myBestVideoData.json", "w")
TEST = ''
def get_service():
  flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
  credentials = flow.run_console()
  return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)

def execute_api_request(client_library_function, **kwargs):
  response = client_library_function(
    **kwargs
  ).execute()

  print(type(response))
  print(response)
  RESULTS.write(str(response))
  RESULTS.close()

if __name__ == '__main__':
  # Disable OAuthlib's HTTPs verification when running locally.
  # *DO NOT* leave this option enabled when running in production.
  os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

  youtubeAnalytics = get_service()
  TEST = execute_api_request(
      youtubeAnalytics.reports().query,
      ids='channel==MINE',
      startDate='2018-05-13',
      endDate='2019-05-13',
      dimensions='day',
      metrics = 'views,estimatedMinutesWatched,likes,dislikes,subscribersGained,comments,shares,annotationClickThroughRate,annotationClickableImpressions,averageViewDuration,averageViewPercentage',
      sort='day'

  )

