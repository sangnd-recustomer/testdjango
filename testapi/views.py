import boto3

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def upload(request):
    try:

        s3 = boto3.client('s.3')
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
