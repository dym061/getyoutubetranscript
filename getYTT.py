import requests
import re
from bs4 import BeautifulSoup as bs
from youtube_transcript_api import YouTubeTranscriptApi
import sys

class YouTubeTranscriptDownloader:
    def __init__(self):
        pass

    def remove_extra_spaces(self, data):
        return data.strip()

    def clean_title(self, data):
        data = data.replace(" - YouTube", "")
        data = re.sub('<[^<]+?>', '', data)
        data = re.sub('[^A-Za-z0-9]+', ' ', data)
        return data

    def get_video_title(self, video_id):
        url = f"https://www.youtube.com/watch?v={video_id}"
        response = requests.get(url)
        soup = bs(response.content, "html.parser")
        title = soup.find("title").text.strip()
        return self.clean_title(title)

    def save_transcript(self, video_id):
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            video_title = self.get_video_title(video_id)
            file_path = f"{video_title}.txt"

            with open(file_path, "w") as file:
                for item in transcript:
                    text = item.get('text', '')
                    file.write(text + " ")
            print(f"Saved {video_id} successfully as: {file_path}")
        except Exception as err:
            print("=---------------------------------")
            print(f"ERROR: {str(err)}")         
            print("=---------------------------------")

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <VIDEOID>")
        return

    downloader = YouTubeTranscriptDownloader()

    video_id = sys.argv[1]
    downloader.save_transcript(video_id)

if __name__ == "__main__":
    main()
