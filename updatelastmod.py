import re
from datetime import datetime
import sys
import os

# 주어진 디렉토리 경로
directory_path = './content/posts'

# 현재 시각을 RFC 3339 포맷으로 가져옵니다
current_time = datetime.now().strftime('%Y-%m-%dT%H:%M:%S+09:00')

# 디렉토리 내의 모든 파일에 대해 반복
for filename in os.listdir(directory_path):
    if filename.endswith('.md'):  # 마크다운 파일만 처리
        file_path = os.path.join(directory_path, filename)

        # 파일 내용을 읽고 수정합니다
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.readlines()

        # `lastmod` 라인을 찾아 업데이트합니다
        for i, line in enumerate(content):
            if line.startswith('lastmod:'):
                content[i] = f'lastmod: "{current_time}"\n'
                break

        # 수정된 내용을 파일에 다시 씁니다
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(content)
