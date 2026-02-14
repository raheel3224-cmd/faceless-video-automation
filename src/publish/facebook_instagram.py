import requests
def post_facebook_video(page_id, page_token, video_url, title, description):
    url = f"https://graph.facebook.com/v19.0/{page_id}/videos"
    data = {
        "file_url": video_url,
        "title": title,
        "description": description,
        "access_token": page_token
    }
    r = requests.post(url, data=data)
    return r.json()
def post_instagram_reel(ig_user_id, page_token, video_url, caption):
    # Step 1: Create container
    url = f"https://graph.facebook.com/v19.0/{ig_user_id}/media"
    data = {
        "media_type": "REELS",
        "video_url": video_url,
        "caption": caption,
        "access_token": page_token
    }
    r = requests.post(url, data=data).json()
    creation_id = r.get("id")
    # Step 2: Publish
    publish_url = f"https://graph.facebook.com/v19.0/{ig_user_id}/media_publish"
    r2 = requests.post(publish_url, data={
        "creation_id": creation_id,
        "access_token": page_token
    }).json()
    return r2
