from youtube_transcript_api import YouTubeTranscriptApi
import os
from dotenv import load_dotenv

load_dotenv()

testvideoId = '1h1gzh3r7OA'
from langchain.llms import OpenAI
llm = OpenAI(model_name="text-davinci-003", temperature=1.0)

# videoId = input("Enter video ID:")
print('Fetching transcript: ', flush=True)
transcript = YouTubeTranscriptApi.get_transcript(testvideoId)
clean = "Given a transcript line, please clean up the text by fixing spacing errors, correcting spelling errors, and removing any 'ums' and 'ahs'. Return the cleaned version of the input line."

print("Writing to transcript.txt")
with open('transcript.txt', 'w', encoding='utf-8') as f:
    for line in transcript:
        fixedLine = llm(clean + line['text'].strip())
        f.write(fixedLine)

print('Process complete.', flush=True)