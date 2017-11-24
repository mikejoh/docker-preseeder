# docker-preseeder
This project was created for fun, i haven't tested the whole build chain with this Debian preseed.cfg server, but it should work as long as you have a good understanding on how your preseed.cfg shoudl look like.

## Todo
[ ] Serve the preseed.cfg via a volume to the container

## Getting started
1. Clone this repo.
2. Build the Docker image.
```
docker build . -t preseeder
```
3. Run the Docker container.
```
docker run -d -p 8080:80 preseeder
```
4. You should now be able to browse to: http://localhost:8080/ here you'll get the choice to download the preseed.cfg file and also to see the calculated MD5 hash of the preseed.cfg file.
