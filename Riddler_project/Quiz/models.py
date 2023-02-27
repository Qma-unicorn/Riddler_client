from django.db import models

class Quiz(models.Model):
    objects = None
    active = models.BooleanField(default=False)
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)
    def __str__(self):
        return self.name

    def get_questions(self):
        return self.question_set.all()


class Question(models.Model):
    objects = None
    content = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    def get_answers(self):
        return self.answer_set.all()


class Answer(models.Model):
    content = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f"question: {self.question.content}, answer: {self.content}, correct: {self.correct}"
class Marks_Of_User(models.Model):
    token = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    spec = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.FloatField()
    count = models.IntegerField()
    def __str__(self):
        return str(self.name + '|' + self.job + '|' + self.quiz.name)
class Marks_Of_User_item(models.Model):
    marks = models.ForeignKey(Marks_Of_User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    date = models.DateTimeField()