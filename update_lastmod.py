import os
from datetime import datetime

# 주어진 디렉토리 경로
directory_path = './content/posts'

# 디렉토리 내의 모든 파일에 대해 반복
for filename in os.listdir(directory_path):
    if filename.endswith('.md'):  # 마크다운 파일만 처리
        file_path = os.path.join(directory_path, filename)

        # 파일의 마지막 수정 시간을 RFC 3339 포맷으로 가져옵니다
        last_modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))
        formatted_last_modified_time = last_modified_time.strftime('%Y-%m-%dT%H:%M:%S+09:00')

        # 파일 내용을 읽고 수정합니다
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.readlines()

        # `lastmod` 라인을 찾아 확인 및 업데이트합니다
        updated = False
        for i, line in enumerate(content):
            if line.startswith('lastmod:'):
                # 현재 `lastmod` 값과 파일의 마지막 수정 시간을 비교합니다
                current_lastmod = line.strip().split(' ')[1].strip('"')
                if current_lastmod != formatted_last_modified_time:
                    content[i] = f'lastmod: "{formatted_last_modified_time}"\n'
                    updated = True
                break

        # `lastmod` 값이 업데이트된 경우, 수정된 내용을 파일에 다시 씁니다
        if updated:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.writelines(content)
