# tc-superset
Talent Catalog use of Apache Superset (same technology as used by Superset)

## Building and uploading a Superset image to Amazon AWS

We refer to the superset image on our staging (test) AWS account, configured for Talent Catalog
Monitoring & Evaluation purposes as "tctalent-me"

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
