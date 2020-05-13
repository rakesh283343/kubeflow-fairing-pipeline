#Import required Python packages
import os
import sys
os.system("gcloud auth activate-service-account --key-file SERVICE_ACCOUNT_KEY.json")
os.system("gcloud auth configure-docker --quiet")
from time import gmtime, strftime
from kubeflow import fairing
from kubeflow.fairing.frameworks import lightgbm

print("INFO: Step 1")

# Setting up google container repositories (GCR) for storing output containers
DOCKER_REGISTRY = 'gcr.io/<GCP PROJECT ID>/fairing-job'
BASE_IMAGE = 'gcr.io/<GCP PROJECT ID>/lightgbm:latest'

# Set gcs_bucket variable to an existing bucket name if that is desired.
gcs_bucket = "<GCS Bucket name>"

# Training data path
partitioned_train_data = ['gs://fairing-lightgbm/regression-example-dist/regression.train_0',
                        'gs://fairing-lightgbm/regression-example-dist/regression.train_1',
                        'gs://fairing-lightgbm/regression-example-dist/regression.train_2',
                        'gs://fairing-lightgbm/regression-example-dist/regression.train_3']

print("INFO: Step 2")

# parameters of model training
params = {
    'task': 'train',
    'boosting_type': 'gbdt',
    'objective': 'regression',
    'metric': 'l2',
    'metric_freq': 1,
    'num_leaves': 31,
    'learning_rate': 0.05,
    'feature_fraction': 0.9,
    'bagging_fraction': 0.8,
    'bagging_freq': 5,
    "n_estimators": 10,
    "is_training_metric": "true",
    "valid_data": "gs://fairing-lightgbm/regression-example/regression.test",
    "train_data": ",".join(partitioned_train_data),
    'verbose': 1,
    "verbose_eval": 1,
    "model_output": "{}/lightgbm/example/model_{}.txt".format(gcs_bucket, strftime("%Y_%m_%d_%H_%M_%S", gmtime())),
    "num_machines": 4,
    "tree_learner": "data"

}

print("INFO: Step 3")

# Execute model training
lightgbm.execute(config=params,
                          docker_registry=DOCKER_REGISTRY,
                          base_image=BASE_IMAGE,
                          cores_per_worker=2, # Allocating 2 CPU cores per worker instance
                          memory_per_worker=0.5, # Allocating 0.5GB of memory per worker instance
                          stream_log=True)

print("INFO: Step 4")
sys.exit()
