# tc-superset
Talent Catalog use of Apache Superset (same technology as used by Sopact)

https://superset.apache.org/

## Building and uploading a Superset image to Amazon AWS

In this example We refer to the superset image on our staging (test) AWS account, configured for Talent Catalog
Monitoring & Evaluation purposes as "tctalent-me".

Specify the platform to be used. It is currently recommended to use the amd64 platform - which is
an X86_64 architecture that we use on AWS. Superset also supports builds specifically for Apple 
computers, which now use a different architecture: arm64. 
If you are developing on a new Apple Mac, Docker build will download by default an arm64 version 
which will not run on AWS (you will get an Exec error at start up when the arm64 image tries to
execute a shell script running on a non arm64 processor).
See https://superset.apache.org/docs/installation/docker-builds/#working-with-apple-silicon 
which shows how you can request that Docker loads the amd64 version even if you are running on a 
new Apple arm64 computer by setting the following environment variable.

```
export DOCKER_DEFAULT_PLATFORM=linux/amd64  
```

Build the Superset image by running the following from the docker directory:
```
docker build -t tctalent-me:latest .
```

Push the image up to an Amazon repository in the Amazon Elastic Container Registry (ECR).
See https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-push-ecr-image.html

For example (using the Talent Catalog staging (test) AWS account):

Link Docker to AWS (once you have done this, Docker will stay connected to your AWS for 12 hours)
```
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 231168606641.dkr.ecr.us-east-1.amazonaws.com
```

Tag the Docker image we are going to push
```
docker tag tctalent-me:latest 231168606641.dkr.ecr.us-east-1.amazonaws.com/tctalent-me
```

And then push that image
```
docker push 231168606641.dkr.ecr.us-east-1.amazonaws.com/tctalent-me
```
