---
title: "how to make a bash alias that takes a parameter"
date: "2023-11-18T17:04:40+09:00"
lastmod: "2023-11-18T17:04:48+09:00"
---


https://stackoverflow.com/questions/7131670/make-a-bash-alias-that-takes-a-parameter
```bash
myfunction() {
    #do things with parameters like $1 such as
    mv "$1" "$1.bak"
    cp "$2" "$1"
}


myfunction old.conf new.conf #calls `myfunction`
```