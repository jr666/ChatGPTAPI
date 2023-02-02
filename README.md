# ChatGPTAPI
An expansion to the official OpenAI API code

## Prereqs
-docker
-docker-compose
-OpenAI API Key

## Download with git clone

```
$  git clone https://github.com/jr666/ChatGPTAPI.git
Cloning into 'ChatGPTAPI'...
remote: Enumerating objects: 28, done.
remote: Counting objects: 100% (28/28), done.
remote: Compressing objects: 100% (25/25), done.
remote: Total 28 (delta 5), reused 22 (delta 2), pack-reused 0
Receiving objects: 100% (28/28), 213.01 KiB | 2.05 MiB/s, done.
Resolving deltas: 100% (5/5), done.
```
## Deploy with docker compose

```
$  cd ChatGPTAPI
$  docker-compose up -d
[+] Building 0.8s (10/10) FINISHED
 => [internal] load build definition from dockerfile                                                                            0.0s
 => => transferring dockerfile: 228B                                                                                            0.0s
 => [internal] load .dockerignore                                                                                               0.0s
 => => transferring context: 2B                                                                                                 0.0s
 => [internal] load metadata for docker.io/library/python:3.8-slim-buster                                                       0.7s
 => [internal] load build context                                                                                               0.0s
 => => transferring context: 217.82kB                                                                                           0.0s
 => [1/5] FROM docker.io/library/python:3.8-slim-buster@sha256:47fb3866234b8137a41017681aef5d98516b5223d791e2caae3e5323ae32983  0.0s
 => CACHED [2/5] WORKDIR /app                                                                                                   0.0s
 => CACHED [3/5] COPY requirements.txt /app                                                                                     0.0s
 => CACHED [4/5] RUN pip3 install -r requirements.txt                                                                           0.0s
 => [5/5] COPY . /app                                                                                                           0.0s
 => exporting to image                                                                                                          0.0s
 => => exporting layers                                                                                                         0.0s
 => => writing image sha256:7858165eb43d3a7735f99bdd8272f57cdc55e200d37583c77b05c5937072b464                                    0.0s
 => => naming to docker.io/library/chatgptapi-webgpt                                                                            0.0s
[+] Running 2/2
 - Network chatgptapi_default     Created                                                                                       0.0s
 - Container chatgptapi-webgpt-1  Started                                                                                       0.5s
```

## Expected result

Listing containers must show one container running and the port mapping as below:
```
$  docker-compose ps
NAME                  IMAGE               COMMAND                  SERVICE             CREATED              STATUS              PORTS
chatgptapi-webgpt-1   chatgptapi-webgpt   "python3 -m flask ru…"   webgpt              About a minute ago   Up About a minute   0.0.0.0:5000->5000/tcp
```

After the application starts, navigate to [http://localhost:5000](http://localhost:5000) in your web browser 


Stop and remove the containers
```
$ docker-compose down
```
