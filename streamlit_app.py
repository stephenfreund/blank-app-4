import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)


import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from oauth2client.client import OAuth2WebServerFlow
import webbrowser

import os
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

# === Load Secrets from Environment Variables ===
CLIENT_ID = os.environ["CLIENT_ID"]
CLIENT_SECRET = os.environ["CLIENT_SECRET"]


# === Function to Save File to Google Drive ===
def save_file_to_drive(local_file_path, drive_file_name):
    gauth = GoogleAuth()

    # Manually configure client configuration
    gauth.DEFAULT_SETTINGS["client_config"] = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "redirect_uris": ["http://localhost:8080"],
        "project_id": "flowco-439910",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "javascript_origins": ["http://localhost:8080"],
    }

    gauth.LocalWebserverAuth()

    drive = GoogleDrive(gauth)

    file1 = drive.CreateFile(
        {"title": "Hello.txt"}
    )  # Create GoogleDriveFile instance with title 'Hello.txt'.
    file1.SetContentString("Beep!")  # Set content of the file from given string.
    file1.Upload()

    st.write(f"File '{drive_file_name}' has been uploaded to Google Drive.")


if st.button("BORP"):
    local_path = "path/to/your/local_file.txt"
    drive_name = "uploaded_file.txt"
    save_file_to_drive(local_path, drive_name)


# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive


# gauth = GoogleAuth()
# gauth.LocalWebserverAuth()  # Creates local webserver and auto handles authentication.

# drive = GoogleDrive(gauth)

# file1 = drive.CreateFile(
#     {"title": "Hello.txt"}
# )  # Create GoogleDriveFile instance with title 'Hello.txt'.
# file1.SetContentString("Beep!")  # Set content of the file from given string.
# file1.Upload()
