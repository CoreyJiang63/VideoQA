#!/bin/bash

# 输入文件夹路径和文件名模式
input_folder="/Users/ironieser/Documents/shanghaitech/project/llm4video/img/003/"
input_pattern="%04d.png"

# 输出文件名和每行图像数量
output_filename="output.png"
images_per_row=10

# 使用find命令获取所有符合模式的图像文件，并排序
input_files=$(find "$input_folder" -name "$input_pattern" | sort)

# 初始化拼接命令
concat_command=""

# 遍历图像文件列表
count=0
for file in $input_files
do
    concat_command+=" -i $file"
    count=$((count+1))
    if [ $((count % images_per_row)) -eq 0 ]; then
        # 当达到每行图像数量时，拼接并重置concat_command
        ffmpeg $concat_command -filter_complex "nullsrc=size=WIDTHxHEIGHT [base];"
        concat_command=""
    fi
done

# 拼接剩余的图像
if [ -n "$concat_command" ]; then
    ffmpeg $concat_command -filter_complex "nullsrc=size=WIDTHxHEIGHT [base];"
fi

# 生成最终拼接的图像
ffmpeg -i "[base][0]overlay=shortest=1[out]" -map "[out]" -pix_fmt yuv420p "$output_filename"
