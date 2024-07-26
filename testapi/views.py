import boto3
from boto3 import Session
from typing import Optional

from rest_framework.decorators import api_view
from rest_framework.response import Response

assume_role_cache: dict = {}


def filter_none_values(kwargs: dict) -> dict:
    """Returns a new dictionary excluding items where value was None"""
    return {k: v for k, v in kwargs.items() if v is not None}


def assume_session(
        role_session_name: str,
        role_arn: str,
        duration_seconds: Optional[int] = None,
        region_name: Optional[str] = None,
) -> boto3.Session:
    """
    Returns a session with the given name and role.
    If not specified, duration will be set by AWS, probably at 1 hour.
    If not specified, region will be left unset.
    Region can be overridden by each client or resource spawned from this session.
    """
    assume_role_kwargs = filter_none_values(
        {
            "RoleSessionName": role_session_name,
            "RoleArn": role_arn,
            "DurationSeconds": duration_seconds,
        }
    )
    credentials = boto3.client("sts").assume_role(**assume_role_kwargs)["Credentials"]
    create_session_kwargs = filter_none_values(
        {
            "aws_access_key_id": credentials["AccessKeyId"],
            "aws_secret_access_key": credentials["SecretAccessKey"],
            "aws_session_token": credentials["SessionToken"],
            "region_name": region_name,
        }
    )
    return boto3.Session(**create_session_kwargs)


@api_view(["GET"])
def upload(request):
    try:

        session = assume_session(
            "MyCustomSessionName",
            "arn:aws:iam::397128298131:role/ecsTaskExecutionRole",
            region_name="us-east-1",
        )
        s3 = session.client('s3')
        response = s3.list_buckets()
        for bucket in response:
            print(bucket.name)
        return Response({"message": "Upload!"})
    except Exception as e:
        return Response({"error": str(e)})


@api_view(["GET"])
def sendmail(request):
    try:
        return Response({"message": "Mail sent!"})
    except Exception as e:
        return Response({"error": str(e)})
