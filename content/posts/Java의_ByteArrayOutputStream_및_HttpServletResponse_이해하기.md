---
title: 'Java의_ByteArrayOutputStream_및_HttpServletResponse_이해하기'
date: 2023-11-24T23:56:29+09:00
lastmod: "2023-11-25T00:32:42+09:00"
---

```
유니코드: 모든 문자열을 나타내기 위한 통일된 체계
UTF-8: 이 체계를 가지고 실제로 화면에 나타내기 위한 방법
```

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

## 추가

- 회사 내 서비스 모듈들 중에 뒷단에 있는 모듈은 바로 HttpServletResponse의 outputStream을 flush 하지않고 ByteArrayOutputStream을 사용한다
- 가장 큰 이유는 MSA 궂로 되어있기때문에 뒷단에서 화면단까지 네트워크 I/O를 최대한 줄이기 위함이 아닌가 싶다. 한번에 전송하니까.

### 직접 `OutputStream`에 `write` 수행
- **버퍼링**: 작은 내부 버퍼를 사용하여 데이터를 임시 저장. **버퍼가 가득 차거**나 혹은 `flush`가 호출될 때 데이터를 전송.
- **실시간 전송**: 데이터는 스트림을 통해 연속적으로 전송되어 실시간성에 유리할 수 있음.
- **메모리 효율**: 전체 데이터를 메모리에 저장하지 않아 큰 데이터 처리 시 메모리 사용이 효율적일 수 있음.
- **오류 처리 복잡성**: 전송 중 발생한 오류를 처리하기가 더 복잡할 수 있음.

### `ByteArrayOutputStream` 를 중간에 같이 사용
- **데이터 모음**: 모든 데이터를 메모리 내의 큰 버퍼에 저장할 수 있음.
- **한 번에 전송**: 저장된 데이터를 한 번에 전송하여 네트워크 I/O를 최소화할 수 있음.
- **데이터 무결성**: 전송 전 데이터를 검증하고 관리할 수 있어 오류 처리에 유리.
- **메모리 사용량**: 큰 데이터를 다룰 경우 전체 데이터를 메모리에 저장하기 때문에 메모리 사용량이 증가할 수 있음.