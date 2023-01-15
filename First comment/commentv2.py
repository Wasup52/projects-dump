from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

CLIENT_SECRET_FILE = (
    "client_secret.json" # This is the file you get from the Google API Console
)
SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]

flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
credentials = flow.run_console()
youtube = build("youtube", "v3", credentials=credentials)

youtube.videos().rate(rating="like", id="wjRgs9N_zUs")

