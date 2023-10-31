import openai
import os
import random
import json
import re

openai.api_key = "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"

file_path = "./qa_annotations.json"

prompt = """
Task: Sequence video verification
Dataset: CSV
**Prompt**  

I want you to act as a professional annotator. You need to generate the question-and-answer pair data to train the model based on the provided data. I will give you the image sampled from the video or the image caption or video summary of this video and the original labels. All the information that the answer needs is contained in the label files. Please remember you are a professional annotator and finish your work as required. Do not consider to briefly generate your output.

There are some rules you need to obey:  

1) For generating questions based on the provided image:

- Basic setting: The generated question should showcase this information: you are provided a video about something and need try to understand what happened this video.

- Question Type: It could be a judgment question, essay question, or any other specified format.
  - If you want to create judgement question. Please ensure the response is No or Yes with the same probability.  Note that the probability of each response, i.e. Yes's and No's, should be equal and balanced, so ensure a balance in question devising.
- Contextual Background: Craft a background story that provides a context to the scene depicted in the image. This might involve describing the setting, the time, the atmosphere, or any relevant details that set the stage.

- Motivation: Explain the motivation or reason behind the question. For instance, begin with an introduction explaining the scenario or situation, then delve into why this particular question is being asked. Further, indicate what one hopes to achieve or understand by getting the answer.

- Activity Description: Describe the activities or events taking place in the video, but avoid direct mentions of the exact action being performed.

- Variety in Storytelling: Ensure a diverse range of background stories. Repeating the same story or context should be avoided.

- Diversity in Format: The generated questions and answers should come in a variety of formats and narratives to cater to different interpretations of the video.


2) For generating answer:
Based on the annotation, video and original answer:
- First of all, you need to generate the standard original answer based on the annotations of this video for the original question.
- Following the generated question by you, you need to write many details. Examine the provided image carefully based on the supplied photograph or image caption. Describe the scene in great detail, focusing on the primary action. 
- Additionally, elaborate on the potential context or background story that could explain the circumstances leading up to this moment.
     
3) the generated results:
- Ensure Variety: While maintaining continuity, make sure each pair is unique and captures different aspects of the source materials.
- Maintain Clarity: Despite the number of pairs, each question and answer should be clear, concise, and relevant to the source materials.


4) the output format:

- First of all, please use JSON format to reply to me.
- Please follow this format to give the final result. Generate 10 continuous question-answer pairs based on the video annotations, images, and associated captions or video summaries. Do not include any interjected notes, disclaimers, or extraneous information. Simply produce the pairs consecutively. Do not pause, add notes, disclaimers, or any other commentary. Just provide 10 uninterrupted Q&A pairs.

    ```json
    {
        "1":{
            "Original question": "This is the question provided by me or generated by you",
            "Original answer": "This is the answer you created based on the annotation and the original question",
            "The question with details": "Here is Your generated question, elaborated in depth, which should adhere to the requirements and incorporate more narrative or motivation elements",
            "The answer with details": "Here is Your answer, expanded and detailed, elaborated in depth, which should offer a comprehensive understanding by explaining the context, reasons, scene knowledge, action motivations, or other pertinent information.",
        },
        "2":{[Hint: Here the requirement is the same, while the content should be different]},
        ...
        "10":{[Hint: Here the requirement is the same, while the content should be different]},
    }

    ```
    Keep note that ten qa pairs are needed.
    Now I am providing you with specific details about the 10 qa pair you need to generate.
    
    - Question 1.2: 
    - Original question: what actions happened in the sequence video?
    - Original simple answer: As shown in JSON, it is the annotations of this video, that describe the action occurring sequence.
"""


# label = """
 
#     ```json
#     "1.2":[
#         "take up the test paper",
#         "tear the test paper",
#         "put down the test paper",
#         "put down the test paper",
#         "take up the glass rod",
#         "point the glass rod to evaporating dish",
#         "point the glass rod to test paper",
#         "put down the glass rod",
#         "take up the tweezer",
#         "clamp the tweezer",
#         "put down the test paper",
#         "put down the tweezer"
#     ],
#     ```json
#     "1.3":[
#         "take up the test paper",
#         "tear the test paper",
#         "put down the test paper",
#         "put down the test paper",
#         "take up the glass rod",
#         "clamp the tweezer",
#         "put down the test paper",
#         "put down the tweezer"
#     ],
#     ```
# """

# Generate two labels

# Load the JSON data from your file
with open('..\dongsx\VideoQA\label_bank.json', 'r') as json_file:
    data = json.load(json_file)

# Initialize an empty list to store the generated strings
generated_strings = []

# Extract mother classes from the subclass keys
mother_classes = sorted(set(mother_class.split('.')[0] for mother_class in data.keys()))
subclasses = [subclass for subclass in data.keys()]

def generate_pairs(sequence):
    pairs = []
    for i in range(len(sequence)):
        for j in range(i, len(sequence)):
            mother_class_i = sequence[i].split('.')[0]
            mother_class_j = sequence[j].split('.')[0]
            if mother_class_i == mother_class_j:
                pairs.append((sequence[i], sequence[j]))
    return pairs

pairs = generate_pairs(subclasses)

strings_list = []
for pair in pairs:
    if pair[0] in data and pair[1] in data:
        result = f'\n```json\n"{pair[0]}": [\n'
        result += ',\n'.join([f'    "{step}"' for step in data[pair[0]]])
        result += '\n],\n'
        result += f'"{pair[1]}": [\n'
        result += ',\n'.join([f'    "{step}"' for step in data[pair[1]]])
        result += '\n]\n```json\n'
        # json_string = json.dumps(result, indent=4)
        json_string = result
        strings_list.append(json_string)

label = random.choice(strings_list)

# Load the JSON file
with open('..\dongsx\VideoQA\label_bank.json', 'r') as json_file:
    data = json.load(json_file)

# Initialize an empty list to store the formatted strings
formatted_strings = []

# Iterate through the JSON data and format each section
for key, values in data.items():
    class_label_str = key.split('.')[0]
    if int(class_label_str) >= 7:
        formatted_string = f'```json\n "{key}":[\n'
        for value in values:
            formatted_string += f'    "{value}",\n'
        formatted_string += ']\n```'
        formatted_strings.append(formatted_string)

# print(formatted_strings)

final_output = '\n'.join(formatted_strings)
# print(final_output)


def csv_annotation(label):
    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": prompt + '\n' + label}
    ]

    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        stream=False
    )
    
    return res["choices"][0]["message"]["content"]

for label in formatted_strings:

    generated_content = csv_annotation(label)
    generated_content = generated_content.replace('\n', '')
    generated_content_single_space = re.sub(' +', ' ', generated_content)
    generated_content_trimmed = generated_content_single_space.strip()
    corrected_json_string = re.sub(r",(\s*})","\g<1>", generated_content_trimmed)

    parsed_data = json.loads(corrected_json_string)
    formatted_data = parsed_data
    for key, value in parsed_data.items():
        formatted_data[key] = {
            "Question": value.get("Original question", ""),
            "Answer": value.get("Original answer", ""),
            "Detailed Question": value.get("The question with details", ""),
            "Detailed Answer": value.get("The answer with details", "")
        }

    formatted_json = json.dumps(formatted_data, indent=4)

    # Extract class from label
    clean_string = label.replace('json', '').replace('`', '').strip()
    clean_string = clean_string.rsplit(',', 1)[0] + "]"
    json_string = '{' + clean_string + '}'
    #print(json_string)
    data = json.loads(json_string)
    subclass_label = list(data.keys())[0]


    if not os.path.exists(file_path):
        # Create a new JSON structure if file doesn't exist
        data = {}
    else:
        # Read existing data
        with open(file_path, 'r') as file:
            data = json.load(file)

    # Add new data under the subclass label
    data[subclass_label] = formatted_json

    # Write the updated data back to the file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
