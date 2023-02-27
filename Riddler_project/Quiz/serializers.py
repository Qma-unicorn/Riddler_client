from rest_framework import serializers
from .models import *

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('id' ,'name', 'desc')
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id' ,'content')
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id','content' ,'correct')