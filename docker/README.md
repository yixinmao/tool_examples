
## Create app and Dockerfile

Source: https://docs.docker.com/get-started/

See example files in this directory

## Build and run a container

1. Creates a Docker image, which we’re going to name using the --tag option

    `$ docker build --tag=friendlyhello .`

    The built image is in your machine’s local Docker image registry:

    `$docker image ls`

2. Run the app, mapping your machine’s port 4000 to the container’s published port 80 using -p:

    `$docker run -p 4000:80 friendlyhello`

3. Now check http://localhost:4000 .
   You can also use the curl command in a shell to view the same content:

    `$curl http://localhost:4000`

- Can also run the app in the background, in detached mode:

    `$docker run -d -p 4000:80 friendlyhello`

    - This outputs container ID (can check a short version of this ID by `$docker container ls` - this ID matched the hostname on http://localhost:4000)

    - Stop the container using the ID:

        `$docker container stop 1fa4ab2cf395` 


## Share the container image

1. Log into Docker account using docker ID:

    `$docker login`

2. Tag the image.

    The notation for associating a local image with a repository on a registry is username/repository:tag . Tagging syntax: `$docker tag image username/repository:tag`. Example:

    `$docker tag friendlyhello yixinmao/get-started:part2`

    Check with `docker image ls`

3. Push the tagged image to the repository (NOTE: this step will make the image publically available!):

    `$docker push username/repository:tag`

4. Now, can pull and run the image from the remote repository on any machine:

    `$docker run -p 4000:80 username/repository:tag`


*NOTE: The above content only covers until Part 2 in the docker doc*

