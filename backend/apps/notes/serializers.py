from django.utils.html import escape
from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = [
            'id',
            'title',
            'content',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id','created_at', 'updated_at']

    def validate_title(self, value):
        # Проверка наличия заголовка и обход XSS атаки
        if not value.strip():
            raise serializers.ValidationError('Заголовок не может быть пустым')
        return escape(value.strip())

    def validate_content(self, value):
        # Проверка наличия содержания и обход XSS атаки
        if not value.strip():
            raise serializers.ValidationError('Содержание не может быть пустым')
        return escape(value.strip())

class NoteCreateSerializer(NoteSerializer):
    pass

class NoteUpdateSerializer(NoteSerializer):
    # Для обновления заметок, делает поля необязательными
    title = serializers.CharField(required=False)
    content = serializers.CharField(required=False)