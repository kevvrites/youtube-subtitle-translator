import os
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY")

from langchain.llms import OpenAI
llm = OpenAI(model_name="text-ada-001", temperature=1.0)

translate = "Translate the following line to Simplified Chinese: "
transcript = open('transcript.txt')

with open('chinese_transcript.txt', 'w', encoding='utf-8') as file:
    for line in transcript:
        transLine = llm(translate + line)
        file.write(transLine + '\n')
file.close()