from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='mlflow_oss_artifact',
    version='2.0.1',
    description='Plugin that provides Aliyun oss Artifact Store functionality for MLflow',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Liangyi Murong',
    author_email='mrly@xkool.org',
    url="https://github.com/mrly16/mlflow-aliyunstore/archive/refs/tags/2.0.1.tar.gz",
    packages=find_packages(),
    install_requires=[
        'mlflow',
        'oss2'
    ],
    entry_points={
        "mlflow.artifact_repository": [
            "oss=mlflow_oss_artifact.store.artifact.aliyun_oss_artifact_repo:AliyunOssArtifactRepository"
        ]
    },
    license="Apache License 2.0",
)
