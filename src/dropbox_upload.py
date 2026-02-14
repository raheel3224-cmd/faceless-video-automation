import dropbox, os
from dropbox.exceptions import ApiError
def upload_to_dropbox(file_path, token, folder="/FacelessVideos"):
    dbx = dropbox.Dropbox(token)
    filename = os.path.basename(file_path)
    dest_path = f"{folder}/{filename}"
    with open(file_path, "rb") as f:
        dbx.files_upload(f.read(), dest_path, mode=dropbox.files.WriteMode.overwrite)
    # Create shareable link
    try:
        link = dbx.sharing_create_shared_link_with_settings(dest_path).url
    except ApiError:
        links = dbx.sharing_list_shared_links(path=dest_path).links
        link = links[0].url if links else None
    # Force direct download link
    if link:
        link = link.replace("?dl=0", "?dl=1")
    return link
