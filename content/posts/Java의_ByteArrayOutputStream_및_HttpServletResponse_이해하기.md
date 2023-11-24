---
title: 'Java의_ByteArrayOutputStream_및_HttpServletResponse_이해하기'
date: 2023-11-24T23:56:29+09:00
lastmod: "2023-11-25T00:01:12+09:00"
---

# Java의 ByteArrayOutputStream 및 HttpServletResponse 이해하기

## ByteArrayOutputStream의 기본 이해
Java의 `ByteArrayOutputStream` 클래스는 데이터를 바이트 배열 형태로 저장하는 내부 버퍼(`buf`)를 가지고 있다. 이 데이터는 사용 방식에 따라 문자열, 이미지, 오디오 등이 될 수 있다.      

## Spring과 HttpServletResponse의 사용

Spring에서 `HttpServletResponse`의 `OutputStream`에 데이터를 쓰는 과정은 다음과 같다

#### 문자열 데이터 응답 예시
```java
public void sendResponse(HttpServletResponse response) {
    String responseData = "응답 메시지";
    byte[] utf8Bytes = responseData.getBytes("UTF-8");
    response.setContentType("text/plain; charset=UTF-8");
    response.setContentLength(utf8Bytes.length);
    try (OutputStream outputStream = response.getOutputStream()) {
        outputStream.write(utf8Bytes);
        outputStream.flush();
    } catch (IOException e) {
    }
}
```

#### 작동 원리
- 문자열은 UTF-8로 인코딩되어 바이트 배열로 변환된다.
- 클라이언트는 이 바이트 스트림을 UTF-8로 디코딩하여 문자열로 표시한다.
- 따라서 예를 들어, ISO-...이런거 쓰면 잘못된 디코딩방식으로 문자열이 이상하게 표시된다. 
