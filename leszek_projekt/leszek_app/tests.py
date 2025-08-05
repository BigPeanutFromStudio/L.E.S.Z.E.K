from django.test import TestCase
from .models import Question, Code, QuestionApplication
# Create your tests here.
class QuestionQueryTest(TestCase):
    def setUp(self):
        Question.objects.create(question="What is the capital of France?", answer_a="Paris", answer_b="London", answer_c="Berlin", answer_d="Madrid",code_id=1)
        Question.objects.create(question="What is the capital of Germany?", answer_a="Berlin", answer_b="London", answer_c="Paris", answer_d="Madrid",code_id=1)