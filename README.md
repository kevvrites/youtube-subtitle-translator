# youtube subtitle translator

## Libraries
- [youtube-transcript-api](https://pypi.org/project/youtube-transcript-api/) (Python)
- [openai api](https://openai.com/blog/openai-api) (Python)

## Function
- Using OpenAI, clean the youtube auto-generated subtitles and translate each line.
- Makes it easier to input into YouTube (already divided by timestamp).
- translates into Simplified Chinese (can edit easily via variable change).

## How to Use
1. clone this repo (edit prompts as needed)
2. Run with 
    > python youtube-transcript.py
3. Input youtube video ID (ending of URL)
4. Outputs will be in the text files.

## Future Improvements
- Input URL and parse string for video ID (prob need regex to certify, also different youtube.com/ and youtu.be links when shared)
- Have the text files retain the transcription format so they can be directly uploaded.