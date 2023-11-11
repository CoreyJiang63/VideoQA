import json
import openai
import requests
from requests.exceptions import RequestException
import re
from tqdm import tqdm

import time
from openai import OpenAI
import math

client = OpenAI()

cnt = 0


def read_csv(file_path):
    with open(file_path, 'r') as file:
        next(file)  # Skip the first line
        for line in file:
            yield [cell for cell in line.strip().split(',')[1:] if cell != '']
def read_video_info(video_info_path):
    video_info = []
    with open(video_info_path, 'r') as file:
        for line in file:
            path, _, total_frames = line.strip().split()
            video_info.append((path, int(total_frames)))
    video_info_dict = {path.split('/')[-1]: {'total_frames': total_frames} for path, total_frames in video_info}
    return video_info_dict


def rescale_annotations(data, video_info_dict):
    action, video_name, total_nums, *frame_numbers = data
    if video_name in video_info_dict:
        total_frames = video_info_dict[video_name]['total_frames']

        # Ensure that total_frames is an integer
        total_frames = int(total_frames)

        # Rescale frame numbers and convert them to strings
        rescaled_frame_numbers = [str(math.floor(int(frame) * 64 / total_frames)) for frame in frame_numbers]

        # Join the frame numbers into a single string separated by spaces
        rescaled_frame_number_str = ' '.join(rescaled_frame_numbers)

        # Append the tuple to the rescaled_annotations list
    # (action, video_name, total_nums, rescaled_frame_number_str)
    else:
        rescaled_frame_number_str = [frame for frame in frame_numbers]
    return (video_name, total_nums, rescaled_frame_number_str)
video_info_path = r'./video_info.txt'
csv_reader = read_csv(r'./train_sorted.csv')
video_info = read_video_info(video_info_path)

base_prompt = """
Using the given data, identify the repetitive action in a video and detail the start and end frames for each repetition.  

- Do not use the video name in the answer. 
- Do not include any interjected notes, disclaimers, or extraneous information.
- Don't need the question in the generation, only need different answers

Your output should describe the action and its repetitions as if you have observed them firsthand, with emphasis on the precision and consistency of the performance. 

The questions are focused on the total number of repetitive actions, while the answers should provide a detailed description similar to the one produced by ChatGPT. 

The answers must enumerate each repetition without any omission, noting the specific frames where the action starts and ends, mirroring the detailed and sequential format provided by ChatGPT. 
Ensure the response lacks extraneous information and present answers consecutively for each video. The JSON should be formatted with a uniform question and a descriptive answer format as demonstrated below:

Question: How many times is the repetitive action performed in the video?

```json
{
    "video_name": {
        "1": {
            "answer": "The action is repeated 11 times, starting and ending at the following frames: 1st repetition from frame 42 to 114, 2nd from frame 114 to 186, 3rd from frame 186 to 252, 4th from frame 252 to 322, 5th from frame 322 to 389, 6th from frame 389 to 452, 7th from frame 452 to 522, 8th from frame 523 to 587, 9th from frame 588 to 660, 10th from frame 660 to 734, and the 11th from frame 734 to 822."
        },
        // Same question, altering the answer to fit the new frame data if necessary.
        "2": {
            "answer": "[Your paraphrased answer]"
       },
        "3":{
            "answer": "[Your paraphrased answer]"
       }
    },
    // Continue with additional video identifiers and their corresponding answers.
    ......
}
``` 


Please provide 5  answers for each video without alternating the original meaning of the question, but paraphrase it for diversity. For each question, the answer is generated correspondingly.

Adjust this template to include the action type and specific frame numbers for each video in your dataset, and ensure that the answer style is consistent with the example provided by ChatGPT.
In the data below, each line comprises type_of_sport, video_name, count, and start and end frames for each repetitive move. And I'm just providing an example below:
stu10_35.mp4	11	42	114	114	186	186	252	252	322	322	389	389	452	452	522	523	587	588	660	660	734	734	822

- First of all， please use JSON format to reply to me.

- For one video and its annotation, generate 5 continuous answers based on the video annotations. Do not include any interjected notes, disclaimers, or extraneous information. Produce the answers consecutively. Do not pause to add notices, disclaimers, or any other commentary. 


Now, I am providing annotations from our original dataset, and please follow the instructions above to generate answers in JSON format:

"""

def json_formatted(generated_content):
    generated_content = generated_content.replace('\n', '')
    generated_content = generated_content.replace('\\', '')
    generated_content_single_space = re.sub(' +', ' ', generated_content)
    generated_content_trimmed = generated_content_single_space.strip()
    # corrected_json_string = re.sub(r",(\s*\})", r"\1", generated_content_trimmed)
    return generated_content_trimmed
# Define maximum number of retries
MAX_RETRIES = 3
# Define initial delay between retries in seconds
BACKOFF_DELAY = 5
json_outputs = []
def save_to_json(data, filename='./qa_annotation_1112_2.json'):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def process_line(line, video_info):
    line = rescale_annotations(line, video_info)
    prompt = base_prompt + '\n' + str(line)
    return prompt
num = 0
for line in tqdm(csv_reader, desc="Processing Lines", unit="line"):
    # if num<31:
    #     num +=1
    #     continue
    # else:
    #     print(line)
    if line[0] not in ['bench_pressing', 'benchpressing', 'pull_up', 'pullups', 'push_up', 'pushups']:
        continue

    if len(line) < 3:
        print("Invalid line:", line)
        continue
    if line[1] == 'stu9_2.mp4':
        pass
    prompt = process_line(line, video_info)
    attempt = 0
    if num<30:
        num +=1
        continue

    while attempt < MAX_RETRIES:
        try:
            # response = client.chat.completions.create(
            #     model="gpt-4-1106-preview",
            #     messages=[
            #         {"role": "system", "content": "You are a professional data annotator."},
            #         {"role": "user", "content": prompt},
            #     ],
            #     response_format={"type": "json_object"}
            # )
            #
            # original_qa_pair = response.choices[0].message.content
            # corrected_json_string = json_formatted(original_qa_pair)
            # parsed_data = json.loads(corrected_json_string)
            #
            # json_outputs.append(parsed_data)
            # save_to_json(json_outputs)  # Save after each successful API call
            break

        except RequestException as e:
            print(f"A network error occurred: {e}. Retrying in {BACKOFF_DELAY} seconds...")
            time.sleep(BACKOFF_DELAY)
            BACKOFF_DELAY *= 2  # Exponential backoff
            attempt += 1

    if attempt == MAX_RETRIES:
        print("Maximum retries reached for line:", line)

print("JSON successfully written.")
# concatenated_data = {}
#
# for item in json_outputs:
#     # Convert the string representation of dictionary to an actual dictionary
#     dict_item = eval(item)
#     concatenated_data.update(dict_item)
#
# # Convert the concatenated dictionary to a JSON string
# json_data = json.dumps(concatenated_data, indent=4)
#
# # Save to a file
# file_path = './qa_annotation_1112.json'
# with open(file_path, 'w') as file:
#     file.write(json_data)

"""

Using the given data, identify the repetitive action in a video and detail the start and end frames for each repetition.  
- Do not use the video name, action class, or type of sport in the question.  
- Do not use the video name in the answer. 
- Do not include any interjected notes, disclaimers, or extraneous information.
Your output should describe the action and its repetitions as if you have observed them firsthand, with emphasis on the precision and consistency of the performance. Format your response as a series of question-and-answer pairs in JSON, where each video is keyed by its name. The questions will be streamlined to focus on the total number of repetitive actions, while the answers should provide a detailed description similar to the one produced by ChatGPT. The answers must enumerate each repetition without any form of omission, noting the specific frames where the action starts and ends, mirroring the detailed and sequential format provided by ChatGPT. Ensure the response is devoid of any extraneous information, and present the Q&A pairs consecutively for each video. The JSON should be formatted with a uniform question template and a descriptive answer format as demonstrated below:

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

Please provide 3 QA pairs for each video without alternating the original meaning of the question, but just paraphrase it for diversity. For each question, the answer is generated correspondingly.

Adjust this template to include the action type and specific frame numbers for each video in your dataset, and ensure that the answer style is consistent with the example provided by ChatGPT.
In the data below, each line comprises type_of_sport, video_name, count, and start and end frames for each repetitive move. And I'm just providing an example below:
pull_up	stu10_35.mp4	11	42	114	114	186	186	252	252	322	322	389	389	452	452	522	523	587	588	660	660	734	734	822

- First of all，please use JSON format to reply to me.

- Please follow this format to give the final result. For one video and its annotation, generate 10 continuous question-answer pairs based on the video annotations. Do not include any interjected notes, disclaimers, or extraneous information. Simply produce the pairs consecutively. Do not pause, add notes, disclaimers, or any other commentary. 



Now, I am providing annotations from our original dataset, and please follow the instructions above to generate QA pairs in JSON format:


['battle_rope', 'stu1_0.mp4', '4', '3', '62', '62', '117', '117', '175', '175', '230']



"""