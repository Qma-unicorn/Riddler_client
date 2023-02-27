from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime

from .models import *
from .serializers import *

def IndexView(request):
    return render(request, 'index.html')
def QuizesView(request):
    return render(request, 'tests.html')
def QuizView(request, quiz_id):
    questions = Quiz.objects.get(id=quiz_id).get_questions()
    QA = {}
    i = 0
    for question in questions:
        answers = Question.objects.get(id=question.id).get_answers()
        QA.update({i : {question : answers}})
        i +=1

    length = len(questions)
    return render(request, 'test.html', {'data' : QA, 'length' : length, 'quiz_id' : quiz_id})

def ResultView(request):
    if request.method == 'POST':
        RQA = request.POST.dict()
        score = 0
        count = 0
        quiz = Quiz.objects.filter(id=RQA['quiz_id']).first()
        del RQA['quiz_id']
        correctAnswers = {}
        for AnswerId in RQA:
            try:
                correctAnswer = ''
                question = Answer.objects.filter(id=RQA[AnswerId]).first().question
                answer = Answer.objects.filter(id=RQA[AnswerId], correct=True).first()
                if answer is not None:
                    score += 1
                    correctAnswer = answer
                else:
                    answer = Answer.objects.filter(id=RQA[AnswerId]).first()
                    correctAnswer = Answer.objects.filter(question = question, correct=True).first()

                correctAnswers.update({question: {answer.content: correctAnswer.content}})
            except:
                pass
        if not Marks_Of_User.objects.filter(token = RQA['csrfmiddlewaretoken']).first():
            mask = Marks_Of_User(name=RQA['name'], job=RQA['job'], spec=RQA['spec'], quiz=quiz, score = score, count = len(quiz.get_questions()), token = RQA['csrfmiddlewaretoken'])
            mask.save()
            for AnswerId in RQA:
                try:
                    item = Marks_Of_User_item(marks = mask, answer = Answer.objects.filter(id=RQA[AnswerId]).first(), date = datetime.now())
                    item.save()
                except:
                    pass

        count = len(quiz.get_questions())
        per = int(score / count * 100)

        return render(request, 'result.html', {'score': score,
                                               'count' : count,
                                               'per' : per,
                                               'quiz' : quiz,
                                               'name': RQA['name'],
                                               'QA' : correctAnswers,
                                               }
                                                )
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
def QuizesApi(request):
    quizes = Quiz.objects.filter(active = True).all()
    serializer = QuizSerializer(quizes, many=True)
    return JsonResponse(serializer.data, safe = False)