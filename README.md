# Tweet Miner

A bot that mines tweets of specific topics.

## What does TweetMiner do?

It is a simple way to download streaming tweets by just specifying the words you want to track. The program will download and write tweets into files for future postprocessing of the data.  It is dockerized so that you don't have to worry about dependencies or complex ways to execute the code.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine. 


### Prerequisites

Install [Docker](https://www.docker.com/get-started) in your computer (if you already don't have it). Once installed, try to get your docker version on the command line

```sh 
docker --version
```
It's been tested on  ```Docker version 19.03.5``` but upper versions may work as well.

### Credentials

Make sure to create a file in this folder named ```.env``` with your personal credentials in [Twitter Development](https://developer.twitter.com/): 

```
API_KEY=XXXXXXXXXXXXXX
API_SECRET_KEY=XXXXXXXXXXXXXX

ACCESS_TOKEN=XXXXXXXXXXXXXX
ACCESS_TOKEN_SECRET=XXXXXXXXXXXXXX
```

### Running

In the main folder run

```sh
make build-run
```

This will create the image and run the container. By default image name is *tweetminer* and container name *tweets*. 
The program will create a folder *./data* where the tweets will be stored in files.

### Stopping container and deleting image

If you just want to stop the running container type

```
make stop
```

To restart the container run

```
make start
```

but if you want to get rid of everything in this project (images and containers), i.e. remove them, then type

```
make remove
```
