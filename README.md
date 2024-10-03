# YouTube Caption Downloader

This project is a Python script that uses Playwright to download captions from YouTube videos.

## Repository

The project is hosted on GitHub:

```
git@github.com:jonatw/playwright-yt-captions.git
```

## Prerequisites

Before you begin, ensure you have met the following requirements:

* You have installed Python 3.7 or later.
* You have a Windows/Linux/Mac machine.
* You have installed Chrome browser (required for Playwright).

## Installation

To install the YouTube Caption Downloader, follow these steps:

1. Clone the repository:
   ```
   git clone git@github.com:jonatw/playwright-yt-captions.git
   cd playwright-yt-captions
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Install the Playwright browsers:
   ```
   playwright install
   ```

## Usage

To use the YouTube Caption Downloader:

1. Open the `app.py` file.
2. At the bottom of the file, replace the YouTube URL with the video you want to download captions for:
   ```python
   download_youtube_captions('https://www.youtube.com/watch?v=YOUR_VIDEO_ID')
   ```
3. Run the script:
   ```
   python app.py
   ```

The script will download the captions and save them as `captions.json` in the same directory.

## How it works

The script uses Playwright to:
1. Launch a headless Chrome browser.
2. Navigate to the specified YouTube video.
3. Intercept network requests to capture the URL of the caption file.
4. Download the caption file and save it as JSON.

## Dependencies

- playwright==1.47.0

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request.