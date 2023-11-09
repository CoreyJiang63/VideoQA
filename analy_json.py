import json
from pathlib import Path

# 设置文件路径
pull_up_path = Path('/Users/ironieser/Documents/shanghaitech/project/llm4video/data/pull_up.jsonl')
pull_up_answer_path = Path('/Users/ironieser/Documents/shanghaitech/project/llm4video/data/pull_up_answer.jsonl')

# 读取pull_up.jsonl文件和pull_up_answer.jsonl文件
# 并根据question_id来映射image与text
combined_data = {}
with pull_up_path.open('r') as file:
    for line in file:
        entry = json.loads(line.strip())
        combined_data[entry['question_id']] = {
            'image': entry['image'],
            'text': None  # 初始化text
        }

with pull_up_answer_path.open('r') as file:
    for line in file:
        entry = json.loads(line.strip())
        if entry['question_id'] in combined_data:
            combined_data[entry['question_id']]['text'] = entry['text']

# 提取video_name和frame_index
def extract_video_frame(image_path):
    parts = image_path.split('/')
    video_name = parts[0]
    frame_index = int(parts[1].split('_')[1].split('.')[0])
    return video_name, frame_index

# 排序数据
sorted_items = sorted(combined_data.items(), key=lambda item: extract_video_frame(item[1]['image']))

# 生成最终数据
final_data = [{'question_id': q_id, 'image': info['image'], 'text': info['text']}
              for q_id, info in sorted_items if info['text'] is not None]

# 保存最终数据
output_path = Path('/Users/ironieser/Documents/shanghaitech/project/llm4video/data/combined_sorted.json')
with output_path.open('w') as outfile:
    json.dump(final_data, outfile, indent=4)

print(f'Data has been combined, sorted by video name and frame index, and saved to {output_path}')
