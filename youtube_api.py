import os
import googleapiclient.discovery
import pandas as pd
import json
from datetime import datetime
import s3fs

def process_comments(response_items):
		comments = []
		for comment in response_items:
				author_name = comment['snippet']['topLevelComment']['snippet']['authorDisplayName']
				comment_text = comment['snippet']['topLevelComment']['snippet']['textOriginal']
				comment_time = comment['snippet']['topLevelComment']['snippet']['publishedAt']
				comment_likes = comment['snippet']['topLevelComment']['snippet']['likeCount']
				comment_info = {'author': author_name, 'comment': comment_text, 'published_at': comment_time, 'Number_of_likes': comment_likes}
				comments.append(comment_info)
		print(f'Finished processing {len(comments)} comments.')
		return comments

def run_youtube_etl():
	os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
	api_service_name = "youtube"
	api_version = "v3"
	DEVELOPER_KEY = "AIzaSyD6nC92UOMG-yHiQ-Hmr3QB29vOYo0sxCs"
	youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey = DEVELOPER_KEY)
	request = youtube.commentThreads().list(
			part="snippet, replies",
			videoId = 'h0xOdfMJTJI'
		)
	response = request.execute()
	comments_list=[]
	# used a while loop that looked for the nextPageToken in each response to retrieve all comments.
	while response.get('nextPageToken', None):
		request = youtube.commentThreads().list(
				part='id,replies,snippet',
				# videoId='8LlcAwQ0Mrw',
				videoId = 'h0xOdfMJTJI',
				pageToken=response['nextPageToken']
			)
		response = request.execute()
		comments_list.extend(process_comments(response['items']))

	comments_df = pd.DataFrame(comments_list)
	comments_df.to_csv('s3://dhruva-airflow-youtube-bucket/youtube_comments_data.csv')