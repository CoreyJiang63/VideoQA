import json
import openai
import requests
from requests.exceptions import RequestException
import re

# Define maximum number of retries
MAX_RETRIES = 5
# Define initial delay between retries in seconds
BACKOFF_DELAY = 1

from openai import OpenAI
client = OpenAI(api_key = "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")

# openai.api_key = "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"
cnt = 0

# def read_csv(file_path):
#     with open(file_path, 'r') as file:
#         next(file)  # Skip the first line
#         batch = []  # List to collect lines
#         for line in file:
#             batch.append([cell for cell in line.strip().split(',')[1:] if cell != ''])
#             if len(batch) == 5:  # Check if we have accumulated 10 lines
#                 yield batch
#                 batch = []  # Reset the batch
#         if batch:  # Yield any remaining lines if less than 10
#             yield batch

def read_csv(file_path):
    with open(file_path, 'r') as file:
        next(file)  # Skip the first line
        for line in file:
            yield [cell for cell in line.strip().split(',')[1:] if cell != '']



csv_reader = read_csv(r'E:\RepCountA\LLSP\annotation\train_sorted.csv')

base_prompt = """
Using the given data, identify the repetitive action in a video and detail the start and end frames for each repetition. Your output should describe the action and its repetitions as if you have observed them firsthand, with emphasis on the precision and consistency of the performance. Format your response as a series of question and answer pairs in JSON, where each video is keyed by its name. The questions will be streamlined to focus on the total number of repetitive actions, while the answers should provide a rich description similar to the one produced by ChatGPT. The answers must enumerate each repetition without any form of omission, noting the specific frames where the action starts and ends, mirroring the detailed and sequential format provided by ChatGPT. Ensure the response is devoid of any extraneous information, and present the Q&A pairs consecutively for each video. The JSON should be formatted with a uniform question template and a descriptive answer format as demonstrated below:

```json
{
    "video_identifier": {
        "1": {
            "question": "How many times is the repetitive action performed in the video?",
            "answer": "The action, identified as a pull-up, is repeated 11 times. The pull-up action is repeated 11 times, starting and ending at the following frames: 1st repetition from frame 42 to 114, 2nd from frame 114 to 186, 3rd from frame 186 to 252, 4th from frame 252 to 322, 5th from frame 322 to 389, 6th from frame 389 to 452, 7th from frame 452 to 522, 8th from frame 523 to 587, 9th from frame 588 to 660, 10th from frame 660 to 734, and the 11th from frame 734 to 822."
        },
        // Repeat this format for the remaining questions, altering the answer to fit the new frame data if necessary.
        "2": {
            "question": "[Your paraphrased question, describing the same question as above]",
            "answer": "[Your paraphrased answer]"
       },
        "3":{
            "question": "[Your paraphrased question, describing the same question as above]",
            "answer": "[Your paraphrased answer]"
       }
    },
    // Continue with additional video identifiers and their corresponding Q&A pairs
    ......
}
``` 

Please provide 3 QA pairs for each video, without alternating the original meaning of the question, but just paraphrase it for the purpose of diversity. For each question, answer is generated correspondingly.

Adjust this template to include the action type and specific frame numbers for each video in your dataset, and ensure that the answer style is consistent with the example provided by ChatGPT.
In this below data, each line is comprised of type_of_sport, video_name, count, start and end frames for each repetitive move. And I'm just providing an example below:
pull_up	stu10_35.mp4	11	42	114	114	186	186	252	252	322	322	389	389	452	452	522	523	587	588	660	660	734	734	822

Now I am providing annotations from our original dataset, and please follow the instructions above to generate QA pairs in JSON format:

"""

def json_formatted(generated_content):
    generated_content = generated_content.replace('\n', '')
    generated_content = generated_content.replace('\\', '')
    generated_content_single_space = re.sub(' +', ' ', generated_content)
    generated_content_trimmed = generated_content_single_space.strip()
    # corrected_json_string = re.sub(r",(\s*\})", r"\1", generated_content_trimmed)
    return generated_content_trimmed

json_outputs = []

for line in csv_reader:
    if cnt <= 10:
        # print(str(line))
        prompt = base_prompt + '\n' + str(line)
        attempt = 0
        while attempt < MAX_RETRIES:
            try:
                # Assuming `client` is defined and set up correctly elsewhere in your code
                response = client.chat.completions.create(
                    model="gpt-4-1106-preview",
                    messages=[
                        {"role": "system", "content": "You are an expert in original label annotator."},
                        {"role": "user", "content": prompt},
                    ],
                    response_format={"type": "json_object"}
                )

                original_qa_pair = response.choices[0].message.content
                print(original_qa_pair)
                corrected_json_string = json_formatted(original_qa_pair)
                print(corrected_json_string)
                parsed_data = json.loads(corrected_json_string)
                print(parsed_data)
                # formatted_json = json.dumps(parsed_data, indent=4)

                json_outputs.append(parsed_data)
                break  # Break out of the retry loop if successful

            except RequestException as e:
                print(f"A network error occurred: {e}. Retrying in {BACKOFF_DELAY} seconds...")
                time.sleep(BACKOFF_DELAY)
                BACKOFF_DELAY *= 2  # Double the delay for the next retry
                attempt += 1
        if attempt == MAX_RETRIES:
            print("Maximum retries reached. Moving to the next line.")
        cnt += 1

# with open('repcount/qa_annotation.json', 'w') as json_file:
#     json.dump(json_outputs, json_file, indent=4)
#     print("JSON successfully written.")

concatenated_data = {}

for item in json_outputs:
    # Convert the string representation of dictionary to an actual dictionary
    dict_item = eval(item)
    concatenated_data.update(dict_item)

# Convert the concatenated dictionary to a JSON string
json_data = json.dumps(concatenated_data, indent=4)

# Save to a file
file_path = 'repcount/qa_annotation.json'
with open(file_path, 'w') as file:
    file.write(json_data)