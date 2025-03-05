from googleapiclient.discovery import build

API_KEY = "AIzaSyD6nC92UOMG-yHiQ-Hmr3QB29vOYo0sxCs"  # Replace with your API Key

youtube = build("youtube", "v3", developerKey=API_KEY)

def get_videos_with_comment_counts(search_query="technology", max_results=10):
    request = youtube.search().list(
        part="snippet",
        maxResults=max_results,  
        order="viewCount",  # Get popular videos
        q=search_query,
        type="video"
    )
    response = request.execute()

    video_comment_counts = []

    for item in response["items"]:
        video_id = item["id"]["videoId"]
        video_title = item["snippet"]["title"]

        # Get video statistics (including comment count)
        video_details = youtube.videos().list(
            part="statistics",
            id=video_id
        ).execute()

        comment_count = int(video_details["items"][0]["statistics"].get("commentCount", 0))

        video_comment_counts.append({
            "Title": video_title,
            "Video ID": video_id,
            "Comments": comment_count
        })

    return video_comment_counts

# Call the function
video_data = get_videos_with_comment_counts()

# Print results
for video in video_data:
    print(f"🎥 {video['Title']} (ID: {video['Video ID']}) - 💬 {video['Comments']} comments")
