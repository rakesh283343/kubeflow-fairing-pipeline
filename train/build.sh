#!/bin/bash
export UI_IMG_PATH=gcr.io/<GCP PROJECT ID>/lightgbm-model
tag=latest
docker rmi -f ${UI_IMG_PATH}:$tag
docker build -t ${UI_IMG_PATH}:$tag -f Dockerfile .
gcloud auth configure-docker --quiet
docker push ${UI_IMG_PATH}:$tag