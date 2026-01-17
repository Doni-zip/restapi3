from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView, Response
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin
from .models import *
from .serializers import *
from rest_framework import status

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
    
class PostListCreateView(
    ListModelMixin,
    CreateModelMixin,
    GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class PostDetailView(
    RetrieveModelMixin,
    GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

class CommentCreateView(
    CreateModelMixin,
    GenericAPIView):
    serializer_class = CommentSerializer

    def post(self, request, post_id):
        data = request.data.copy()
        data['post'] = post_id

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LikeCreateView(APIView):
    def post(self, request, post_id):
        post = Post.objects.filter(id=post_id).first()

        if not post:
            return Response(
                {'error': 'Post not found'},
                status=status.HTTP_200_OK
            )

        Like.objects.create(post=post)

        return Response(
            {'message': 'Like added'},
            status=status.HTTP_201_CREATED
        )
