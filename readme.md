
# kyu blog wiki with hugo



## 방향

쉽게 접근해서 작성   
쉽게 접근해서 검색   
검색할땐 디렉토리구조나 태그는 중요하지 않음   
웹에서 검색가능해야함 모바일에서도 비로접속   
공개 리포지토리   
깃 푸쉬 풀 용이   
jetbrains 깃 클라이언트 쓰는게 젤 편함   
어디 날라가는게 걱정이니까 깃헙 백업이 젤중요   

비공개 - 공개하기 어려운 정보가 담긴 문서 (비밀번호 등), 회사 관련, 회사관련 쑬때도 특별히 학습하여 공유할것은 공개로   
공개 - 학습한 내용 등   


블로그스타일   
날짜 내림차순으로 쭉 나열   
제목, 어떤 글인지, 내용, 수정날짜,   
마크다운 가독성있게 표시

## 설정

front matter중 lastmod를 자동으로 업데이트 하기 위해서 `.git/hooks/pre-commit`파일을 생성한다.   
`pre-commit`의 내용은 `pre-commit.py`를 참고한다. 