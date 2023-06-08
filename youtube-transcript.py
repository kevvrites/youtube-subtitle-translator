from youtube_transcript_api import YouTubeTranscriptApi
import os
from dotenv import load_dotenv

load_dotenv()

from langchain.llms import OpenAI
llm = OpenAI(model_name="text-davinci-003", temperature=1.0)

videoId = input("Enter video ID:")
print('Fetching transcript: ', flush=True)
transcript = YouTubeTranscriptApi.get_transcript(videoId)
clean = "Clean up the text in the transcript. Fix spacing errors and spelling errors. Remove the ums and ahs. "

print("Writing to transcript.txt")
with open('transcript.txt', 'w', encoding='utf-8') as f:
    for line in transcript:
        fixedLine = llm(clean + line['text'])
        f.write(fixedLine + '\n')

print('Process complete.', flush=True)
