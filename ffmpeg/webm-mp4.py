import subprocess
ffmpeg=r'D:\ffmpeg-master-latest-win64-gpl-shared\bin'
def convert_webm_to_mp4(input_file, output_file):
    # 使用FFmpeg执行命令行命令
    subprocess.call([ffmpeg, '-i', input_file, output_file])

# 示例用法
input_file = '1.webm'
output_file = 'output.mp4'
convert_webm_to_mp4(input_file, output_file)