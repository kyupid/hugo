---
title: "how to make a bash alias that takes a parameter"
date: "2023-11-18T17:04:40+09:00"
lastmod: "2023-11-18T17:39:59+09:00"
---

## 알아둘 것
- function의 이름을 1글자로하면 쉘이 인식을 하지 못하는 현상이 있음. 따라서, 2글자 이상으로 해야함.
- 앞에 `function` 이라는 키워드를 적거나 안적어도 되는데, mac os Ventura 환경에서는 `function`이 없으면 함수인지 인식을 못하는 현상이 있었음 

## 사용법
https://stackoverflow.com/questions/7131670/make-a-bash-alias-that-takes-a-parameter
```bash
myfunction() {
    #do things with parameters like $1 such as
    mv "$1" "$1.bak"
    cp "$2" "$1"
}


myfunction old.conf new.conf #calls `myfunction`
```
