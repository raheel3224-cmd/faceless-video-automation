import argparse
from config import get_env
from video import generate_video
from dropbox_upload import upload_to_dropbox
from publish.youtube import upload_youtube
from publish.facebook_instagram import post_facebook_video, post_instagram_reel
def main(run_now=False):
    # 1) Generate script (simple stub)
    script = "Every day is a new chance to grow. Stay focused, stay strong, and keep moving forward."
    # 2) Generate video
    video_path = generate_video(script)
    # 3) Upload to Dropbox
    dropbox_link = upload_to_dropbox(video_path, get_env("DROPBOX_ACCESS_TOKEN"))
    print("Dropbox link:", dropbox_link)
    title = "Daily Motivation - Keep Moving Forward"
    description = script
    # 4) Upload YouTube
    yt_id = upload_youtube(
        video_path, title, description,
        get_env("YOUTUBE_CLIENT_ID"),
        get_env("YOUTUBE_CLIENT_SECRET"),
        get_env("YOUTUBE_REFRESH_TOKEN")
    )
    print("YouTube video ID:", yt_id)
    # 5) Post Facebook + Instagram (using Dropbox link)
    fb_resp = post_facebook_video(
        get_env("FB_PAGE_ID"),
        get_env("FB_PAGE_ACCESS_TOKEN"),
        dropbox_link,
        title,
        description
    )
    print("Facebook:", fb_resp)
    ig_resp = post_instagram_reel(
        get_env("IG_USER_ID"),
        get_env("FB_PAGE_ACCESS_TOKEN"),
        dropbox_link,
        description
    )
    print("Instagram:", ig_resp)
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-now", action="store_true")
    args = parser.parse_args()
    if args.run_now:
        main(run_now=True)
