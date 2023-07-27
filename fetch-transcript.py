from youtube_transcript_api import YouTubeTranscriptApi
testvideoId = '1h1gzh3r7OA'

print('Fetching transcript: ', flush=True)
transcript = YouTubeTranscriptApi.get_transcript(testvideoId)

print("Writing to transcript.txt")
print(transcript)
with open('transcript-original.txt', 'w', encoding='utf-8') as f:
    for line in transcript:
        f.write(line['text'].strip() + '\n')

print('Process complete.')