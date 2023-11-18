#!/usr/bin/env python3
import subprocess
from datetime import datetime
import os

# 현재 시간을 RFC 3339 포맷으로 설정
current_time = datetime.now().strftime('%Y-%m-%dT%H:%M:%S+09:00')

# git 루트 디렉토리의 절대 경로를 가져옴
git_root = subprocess.check_output(['git', 'rev-parse', '--show-toplevel']).decode().strip()

# 수정된 파일 목록을 가져옴
modified_files = subprocess.check_output(['git', 'diff', '--cached', '--name-only', '--diff-filter=ACM']).decode().splitlines()

for file in modified_files:
    # content/posts/ 디렉토리 내의 .md 파일만 처리
    if file.startswith('content/posts/') and file.endswith('.md'):
        full_path = os.path.join(git_root, file)
        with open(full_path, 'r+') as f:
            content = f.readlines()
            f.seek(0)
            updated = False
            for line in content:
                if line.startswith('lastmod:'):
                    f.write(f'lastmod: "{current_time}"\n')
                    updated = True
                else:
                    f.write(line)
            if updated:
                # 파일 내용을 업데이트하고 스테이징
                f.truncate()
                subprocess.run(['git', 'add', file])
