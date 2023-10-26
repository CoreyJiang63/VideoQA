import cv2
import os

def images_to_video(image_folder, filelist_path, output_path, fps):
    # 从文件列表加载图像文件名
    with open(filelist_path, 'r') as f:
        image_files = [line.strip() for line in f.readlines()]

    # 从第一张图像中获取图像尺寸作为视频尺寸
    image_path = os.path.join(image_folder, image_files[0])
    first_image = cv2.imread(image_path)
    height, width, _ = first_image.shape

    # 创建视频编码器
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(output_path, cv2.CAP_FFMPEG, fourcc, fps, (width, height))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 可根据需要更改编码器
    video = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    # 逐帧写入图像到视频
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        image = cv2.imread(image_path)
        video.write(image)

    # 释放资源
    video.release()

    print(f'视频已保存至：{output_path}')

# 设置输入图像文件夹、文件列表、输出视频路径和帧率
input_folder = '/Users/ironieser/Documents/shanghaitech/project/llm4video/data/video/chenyijun'
filelist = '/Users/ironieser/Documents/shanghaitech/project/llm4video/data/video/chenyijun/filelist.txt'
output_video = '/Users/ironieser/Documents/shanghaitech/project/llm4video/data/video/csv_53_chenyijun.mp4'
frame_rate = 25

# 调用函数将图像合成为视频
images_to_video(input_folder, filelist, output_video, frame_rate)

