import json
import random
import os

cnt = 0

with open("./dongsx/VideoQA/label_bank.json") as f:
    label_bank = json.load(f)

def formatted_json(file_path):
    # Step 1: Read and parse the original JSON
    with open(file_path, 'r', encoding="utf-8") as file:
        original_json = json.load(file)

    # Step 2: Read and parse the mapping TXT to create reverse mapping (label -> list of videos)
    label_video_mapping = {}
    with open('./dongsx/VideoQA/train_split.txt', 'r') as file:
        for line in file:
            video, label = line.strip().split()
            if label not in label_video_mapping:
                label_video_mapping[label] = []
            label_video_mapping[label].append(video)

    # Step 3: Generate the new JSON
    new_json = []
    #print(label_video_mapping)

    for label, videos in label_video_mapping.items():
        if label in original_json:  # Check if the label exists in the original JSON
            qa_pairs = original_json[label]
            
            videos_data = []
            for video in videos:
                # Randomly sample a QA pair for this video
                qa_pair_key = random.choice(list(qa_pairs.keys()))
                qa_pair = qa_pairs[qa_pair_key]
                
                # Extract the required QA
                question = qa_pair["The question with details"]
                answer = qa_pair["The answer with details"]
                
                video_data = {
                    "dataset": "CSV",
                    "class_0": f"{label}",
                    "label_0": label_bank[label],
                    "video_0": f"{label}/{video}",
                    "class_1": None,
                    "video_1": None,
                    
                    "QA": {"q": question, "a": answer}
                }
                
                videos_data.append(video_data)
            
            label_entry =  {"videos": videos_data}
            
            new_json.append(video_data)

    # Save the new JSON
    new_file_path = f"./formatted_jsons/new_json{cnt}.json"
    with open(new_file_path, 'w') as file:
        json.dump(new_json, file, indent=4)

    print("New JSON generated successfully.")

folder_path = ".\\qa_annotations"
json_files = []

for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith(".json"):
            json_files.append(os.path.join(root, file))
for json_file in json_files:
    formatted_json(json_file)
    cnt += 1