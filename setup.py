from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='mlflow-oss-artifact',
    version='1.0.0',
    description='Plugin that provides Aliyun oss Artifact Store functionality for MLflow',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Liangyi Murong',
    author_email='mrly@xkool.org',
    url="https://github.com/mrly16/mlflow-aliyunstore",
    packages=find_packages(),
    install_requires=[
        'mlflow',
        'oss2'
    ],
    entry_points={
        "mlflow.artifact_repository": [
            "oss=aliyunstoreplugin.store.artifact.aliyun_oss_artifact_repo:AliyunOssArtifactRepository"
        ]
    },
    license="Apache License 2.0",
)
