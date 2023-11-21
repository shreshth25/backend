from rest_framework.response import Response
from rest_framework import status


def CustomResponse(message = '', data = {} , status = status.HTTP_200_OK):
    return Response(
        {
            "message": message,
            "data":data,
            "status":status
        },
        status=status
    )