# YouTube Transcript Downloader

The Python script is designed to download and save the transcript of a YouTube video using the video's unique ID. It utilizes the youtube_transcript_api to fetch the transcript, and BeautifulSoup to scrape the video title from the YouTube page. The script is structured around a class that manages the download and storage of the transcript in a text file named after the video title, ensuring the title is cleaned of unnecessary characters and HTML tags for use as a filename.

## Features

- **Fetch Video Title**: Retrieves the video title from YouTube using the video's ID.
- **Clean Video Title**: Processes the title to remove unwanted characters and HTML tags, making it suitable for use as a filename.
- **Download Transcript**: Uses the youtube_transcript_api to download the transcript of a YouTube video.
- **Save Transcript**: Writes the downloaded transcript to a text file named after the video's title.
- **Command-line Interface**: Allows users to specify the video ID directly via command-line arguments, making it easy to use in scripts or batch operations.

## Methods

### __init__(self)
Initializes the downloader with a specific output folder. Currently, this method does nothing with the passed output_folder, as it's not implemented in the method body.

### remove_extra_spaces(self, data)
Removes leading and trailing spaces from the provided string, ensuring that the text is neatly formatted.

### clean_title(self, data)
Cleans the video title by removing the "- YouTube" suffix, any HTML tags, and non-alphanumeric characters, which makes the string safe for use as a filename.

### get_video_title(self, video_id)
Fetches the video's webpage using the video ID, extracts the title using BeautifulSoup, and cleans it using the clean_title method.

### save_transcript(self, video_id)
Attempts to download the video transcript using the youtube_transcript_api. If successful, it saves the transcript text to a file named after the cleaned video title. Handles exceptions by printing error messages.

## How to Run

To run the script from the command line, you need to have Python installed on your system, as well as the necessary libraries (requests, re, bs4, and youtube_transcript_api). You can install these libraries using pip if they are not already installed:

`pip install requests beautifulsoup4 youtube_transcript_api`

Once the dependencies are installed, you can run the script using the following command, where VIDEOID is the unique identifier for the YouTube video you want to download the transcript for:

`python getYTT.py VIDEOID`

For example, if you have a video ID like dQw4w9WgXcQ, you would run:

`python getYTT.py dQw4w9WgXcQ`