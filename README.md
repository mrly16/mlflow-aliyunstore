# Xkool Aliyun OSS store plugin for MLflow
_Forked and modified from SeaOfOcean at https://github.com/SeaOfOcean/mlflow-aliyunstore_

This repository provides a MLflow plugin that allows users to use Aliyun OSS as the artifact store for MLflow.

# Usage

Pip install the package on both your client and the server

```bash
pip install mlflow_oss_artifact
```

Configure environment variables in your OS for Aliyun OSS authentication

Note: checkout [this post](https://unix.stackexchange.com/a/117470) on stackoverflow to make them permanent if necessary

```bash
export MLFLOW_OSS_ENDPOINT_URL=<oss-xx-cityname.aliyuncs.com>
export MLFLOW_OSS_KEY_ID=<your_oss_key_id>
export MLFLOW_OSS_KEY_SECRET=<your_oss_key_secret>
export MLFLOW_OSS_BUCKET_NAME=<your_bucket_name>
```

To use To use Aliyun OSS as an artifact store, an OSS URI of the form ``oss://<path>`` must be provided, as shown in the example below:

```python
import mlflow
import mlflow.pyfunc

class Mod(mlflow.pyfunc.PythonModel):
    def predict(self, ctx, inp):
        return 7

exp_name = "myexp"
mlflow.create_experiment(exp_name, artifact_location="oss://mlflow-test/")
mlflow.set_experiment(exp_name)
mlflow.pyfunc.log_model('model_test', python_model=Mod())
```

In the example provided above, the ``log_model`` operation creates three entries in the OSS storage ``oss://mlflow-test/$RUN_ID/artifacts/model_test/``, the MLmodel file
and the conda.yaml file associated with the model.
