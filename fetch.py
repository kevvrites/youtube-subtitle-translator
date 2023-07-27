from youtube_transcript_api import YouTubeTranscriptApi
# TODO: make video ID variable / input via copypaste link
# TODO: regex to make youtube.com/w= and youtu.be/ both work


testvideoId = '1h1gzh3r7OA'

transcript = YouTubeTranscriptApi.get_transcript(testvideoId)

with open('original-transcript.txt', 'a+', encoding='utf-8') as f:
    for line in transcript:
        f.write(line['text'].strip() + '\n')

print("Fetch complete.\n")