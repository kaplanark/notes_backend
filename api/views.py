# from rest_framework import generics, permissions
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from .models import Note
from .serializers import NoteSerializer
from rest_framework_simplejwt import authentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

User = get_user_model()

class ApiView(APIView):
    def get(request, *args, **kwargs):
        return Response('Api is runing',status=status.HTTP_200_OK)
    
class UserCreate(APIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserDetail(APIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.JWTAuthentication,)

    def get_object(self):
        return self.request.user

class NoteListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    # TODO 0. all notes

    def get(self, request, *args, **kwargs):
        notes = Note.objects.filter(user=request.user.id)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # TODO 1. create
    def post(self, request, *args, **kwargs):
        data = {
            'img': request.data.get('img'),
            'title': request.data.get('title'),
            'text': request.data.get('text'),
            'color': request.data.get('color'),
            'categories': request.data.get('categories'),
            'show': request.data.get('show'),
            'pinned': request.data.get('pinned'),
            'archived': request.data.get('archived'),
            'trashed': request.data.get('trashed'),
            'user': request.user.id
        }
        serializer = NoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # TODO 2. update
    def put(self, request, note_id, *args, **kwargs):
        note_instance = self.get_object(note_id, request.user.id)
        if not note_instance:
            return Response(
                {"res": "Object with note id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'img': request.data.get('img'),
            'title': request.data.get('title'),
            'text': request.data.get('text'),
            'color': request.data.get('color'),
            'categories': request.data.get('categories'),
            'show': request.data.get('show'),
            'pinned': request.data.get('pinned'),
            'archived': request.data.get('archived'),
            'trashed': request.data.get('trashed'),
            'user': request.user.id
        }
        serializer = NoteSerializer(
            instance=note_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # TODO 3. delete
    def delete(self, request, note_id, *args, **kwargs):
        note_instance = self.get_object(note_id, request.user.id)
        if not note_instance:
            return Response(
                {"res": "Object with note id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        note_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )

class NoteDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, note_id, user_id):
        try:
            return Note.objects.get(id=note_id, user=user_id)
        except Note.DoesNotExist:
            return None

    # TODO 3. retrieve
    def get(self, request, note_id, *args, **kwargs):
        note_instance = self.get_object(note_id, request.user.id)
        if not note_instance:
            return Response(
                {"res": "Object with note id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = NoteSerializer(note_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # TODO 4. update
    def put(self, request, note_id, *args, **kwargs):
        note_instance = self.get_object(note_id, request.user.id)
        if not note_instance:
            return Response(
                {"res": "Object with note id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'img': request.data.get('img'),
            'title': request.data.get('title'),
            'text': request.data.get('text'),
            'color': request.data.get('color'),
            'categories': request.data.get('categories'),
            'show': request.data.get('show'),
            'pinned': request.data.get('pinned'),
            'archived': request.data.get('archived'),
            'trashed': request.data.get('trashed'),
            'user': request.user.id
        }
        serializer = NoteSerializer(
            instance=note_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # TODO 5. Delete
    def delete(self, request, note_id, *args, **kwargs):
        note_instance = self.get_object(note_id, request.user.id)
        if not note_instance:
            return Response(
                {"res": "Object with note id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        note_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )