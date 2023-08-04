// import { YouTubeTranscript } from "youtube-transcript";

// const testvideoId = "1h1gzh3r7OA";

// YoutubeTranscript.fetchTranscript(testvideoId).then(console.log);

// // with open('original-transcript.txt', 'w+', encoding='utf-8') as f:
// //     for line in transcript:
// //         f.write(line['text'].strip() + '\n')

// console.log("Fetch complete.\n");

const API_KEY = "AIzaSyDpTS_Zq07uYMSwVAJz7bB7pCuNBnK6Apk";
const videoId = "1h1gzh3r7OA"; // Replace with the ID of the video you want to fetch the transcript for

function fetchTranscript() {
  fetch(
    `https://www.googleapis.com/youtube/v3/videos?part=snippet&id=${videoId}&key=${API_KEY}`
  )
    .then((response) => response.json())
    .then((data) => {
      if (data.items && data.items.length > 0) {
        const videoTitle = data.items[0].snippet.title;
        console.log(`Transcript for video "${videoTitle}" (ID: ${videoId}):`);
        fetch(
          `https://www.googleapis.com/youtube/v3/captions?part=snippet&videoId=${videoId}&key=${API_KEY}`
        )
          .then((response) => response.json())
          .then((data) => {
            if (data.items && data.items.length > 0) {
              data.items.forEach((item) => {
                console.log(`Language: ${item.snippet.language}`);
                console.log(`Transcript: ${item.snippet.trackKind}`);
                console.log("===============================");
              });
            } else {
              console.log("No transcript available.");
            }
          })
          .catch((error) => console.error("Error fetching transcript:", error));
      } else {
        console.log("Video not found.");
      }
    })
    .catch((error) => console.error("Error fetching video details:", error));
}

function handleClick() {
  fetchTranscript();
}
