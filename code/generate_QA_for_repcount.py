import json
import csv

# Function to read CSV data and return a dictionary with video name as key and action class as value
def read_csv_to_dict(file_path):
    video_data = {}
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header line
        for line in csv_reader:
            _, action_class, video_name_with_ext, *rest = line
            video_name = video_name_with_ext.split('.')[0]  # Get the video name without extension
            video_data[video_name] = action_class
    return video_data

# Function to load QA values from the given JSON file
def load_qa_values(json_file_path):
    with open(json_file_path, 'r') as file:
        return json.load(file)

# Function to create the transformed data structure
def create_transformed_data_structure(video_name, action_class,  answer):
    return {
        "dataset": "repcounta",
        "class_0": action_class,
        "label_0": [],  # Populate this as per your requirement
        "video_0": f"{action_class}/{video_name}",
        "class_1": None,
        "label_1": None,
        "video_1": None,
        "QA": [{"from": "human", "value": "How many times is the repetitive action performed in the video?"}] +
              [{"from": "gpt", "value":  answer['answer']}]
    }

# Main execution
csv_data_dict = read_csv_to_dict('/Users/ironieser/Documents/shanghaitech/project/llm4video/train_sorted.csv')
qa_values = load_qa_values('/Users/ironieser/Documents/shanghaitech/project/llm4video/qa_annotation_1112_3.json')

transformed_data = []
for qa_item in qa_values:
    for video_name_with_ext, answers in qa_item.items():
        video_name = video_name_with_ext.split('.')[0]
        if video_name in csv_data_dict:
            action_class = csv_data_dict[video_name]
            for _ ,answer in answers.items():
                data_structure = create_transformed_data_structure(video_name, action_class, answer)
                transformed_data.append(data_structure)

# Save the transformed data to a JSON file
output_file_path = '/Users/ironieser/Documents/shanghaitech/project/llm4video/transformed_data_2.json'
with open(output_file_path, 'w') as json_file:
    json.dump(transformed_data, json_file, indent=4)

print(f"JSON data has been transformed and saved to {output_file_path}")
