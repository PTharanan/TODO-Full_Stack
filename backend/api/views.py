from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Data
from .serializers import DataSerializer

class Data_API(APIView):
    def get(self, request):
        data = Data.objects.all()
        serializer = DataSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = Data(task_tit = request.data['task_tit'], tasks = request.data['tasks'])
        data.save()
        return Response("Sucessfully Saved!!!")