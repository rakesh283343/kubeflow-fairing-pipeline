### How to run the code:

**Step 1:**
Create a kubeflow cluster on GKE

**Step 2:**
- Update GCP project ID in build.sh at line no - 2.
- Authenticate with a service account to perform push and pull from GCR in code.py at line no - 4.
- Update GCP project ID for DOCKER_REGISTRY and BASE_IMAGE in code.py at line no - 13,14.
- Create GCS bucket and update value in code.py at line no - 17.
- Run below command to build docker image and push it to GCR.
```bash
$ cd train
$ bash build.sh
```

**Step 3:**
- Update GCP project ID in pipeline.py at line no - 15
- Run below command to build kubeflow pipeline.
```bash
$ python3 pipeline.py
```

**Step 4:**
- Upload kubeflow pipeline zip on kubeflow dashboard and run the experiment.
