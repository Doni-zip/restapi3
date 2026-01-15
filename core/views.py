from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView, Response
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin
from .models import Client
from .serializers import ClientSerializer

# class ClientView(APIView):
#     def get(self, request):
#         clients = Client.objects.all()
#         serializer = ClientSerializer(clients, many=True)

#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = ClientSerializer(data=request.data)

#         if serializer.is_valid(raise_exceptions=True):
#             serializer.save()
#             return Response(serializer.data)
        
# class ClientView(GenericAPIView):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer
    
#     def get(self, request):
#         clients = self.get_queryset()
#         serializer = self.get_serializer(clients, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)

#         if serializer.is_valid(raise_exceptions=True):
#             serializer.save()
#             return Response(serializer.data)


# APIView -> GenericAPIView + Миксины
# ListModelMixin - позволяет показыать список


class ClientListCreateView(
    GenericAPIView,
    ListModelMixin,
    CreateModelMixin
):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)

class ClientRetreiveUpdateDeleteView(
    GenericAPIView,
    UpdateModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin
):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk=pk)
    
    def put(self, request, pk):
        return self.update(request, pk=pk)
    
    def patch(self, request, pk):
        return self.update(request, pk=pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)