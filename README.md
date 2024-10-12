# 10hLoop

```
docker build -t my-moviepy-app .
```


```
docker run -v $(pwd)/input.mp3:/app/input.mp3 -v $(pwd)/image.png:/app/image.png -v $(pwd)/output:/app/output my-moviepy-app
```

