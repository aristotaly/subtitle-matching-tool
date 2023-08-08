import os
import re
import chardet
import shutil
import mimetypes

def convert_to_utf8(file_path):
    with open(file_path, 'rb') as file:
        rawdata = file.read()
        result = chardet.detect(rawdata)
        encoding = result['encoding']

        if encoding != 'utf-8':
            with open(file_path, 'r', encoding=encoding) as file:
                content = file.read()
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f'Converted {file_path} to UTF-8.')

def rename_subtitle(video_file, subtitle_file):
    subtitle_new_name = os.path.splitext(video_file)[0] + '.srt'
    shutil.move(subtitle_file, subtitle_new_name)
    print(f'Renamed {subtitle_file} to {subtitle_new_name}.')

def is_video(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)
    return mime_type and mime_type.startswith('video')

def main(directory_path):
    for root, _, files in os.walk(directory_path):
        video_files = [file for file in files if is_video(os.path.join(root, file))]
        srt_files = [file for file in files if file.endswith('.srt')]

        for srt_file in srt_files:
            convert_to_utf8(os.path.join(root, srt_file))

        for video_file in video_files:
            season_episode_pattern = re.compile(r'S\d{2}E\d{2}')
            video_season_episode = season_episode_pattern.search(video_file)

            if video_season_episode:
                matching_srt_file = next((srt for srt in srt_files if video_season_episode.group() in srt), None)
                if matching_srt_file:
                    rename_subtitle(video_file, os.path.join(root, matching_srt_file))

if __name__ == "__main__":
    directory_path = os.getcwd() # Get the current working directory
    main(directory_path)
