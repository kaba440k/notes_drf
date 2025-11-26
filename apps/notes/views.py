from rest_framework import generics, status
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models import Note
from .serializers import NoteSerializer, NoteCreateSerializer, NoteUpdateSerializer

class NoteListCreateView(generics.ListCreateAPIView):
    queryset = Note.objects.all()

    def get_serializer_class(self):
        # Возвращает подходящий сериализатор в зависимости от запроса
        if self.request.method == 'POST':
            return NoteCreateSerializer
        return NoteSerializer

    def get(self, requests, *args, **kwargs):
        #Обрабатывает Get запрос для получения списка заметок
        return super().get(requests, *args, **kwargs)

