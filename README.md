# manim_data

## Run docker container

See [official manim docker repository](https://hub.docker.com/r/manimcommunity/manim) also.

###  bash 

`sudo docker-compose run main /bin/bash`

### create movie

`sudo docker-compose run manim`

### jupyter

`sudo docker-compose up` , open `http:localhost:8888/lab` in browser, and put the token in the log of compose to browser.
if you run it on wsl2, you should open by browser of wsl2 (and maybe need to configuration of X server)

## TODO

### enhancement

- use `marino` instead of `jupyter`