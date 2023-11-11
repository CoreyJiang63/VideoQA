from fractions import Fraction
import math

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


def rescale_annotations(csv_file_path, video_info_dict):
    rescaled_annotations = []
    for data in read_csv(csv_file_path):
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
            rescaled_annotations.append((action, video_name, total_nums, rescaled_frame_number_str))
    return rescaled_annotations


# File paths
csv_pth = r'./train_sorted.csv'
video_info_path = r'./video_info.txt'

# Example usage
video_info = read_video_info(video_info_path)
rescaled_annotations = rescale_annotations(csv_pth, video_info)

# Print out rescaled annotations for verification
for item in rescaled_annotations:
    print(item)
