from django.test import TestCase,Client

# Create your tests here.
import datetime 
from django.utils import timezone
from .models import Question 

from django.core.urlresolvers import reverse


def create_question(question_text,day) :
    time = timezone.now() + datetime.timedelta(day)
    return Question.objects.create(question_text=question_text,pub_feild = time)


class QuestionViewTests(TestCase):

    #client = Client();

    def test_index_view_with_no_questions(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'],[])

    def test_index_view_with_a_past_question(self):
        create_question(question_text="Past_question.",day=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list']
            ,['<Question: Past_question.>'])


    def test_index_view_with_a_future_question(self):
        create_question(question_text="Past_question.",day=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response,"No polls are available.",status_code=200)
        self.assertQuerysetEqual(
            response.context['latest_question_list']
            ,[])
        

    def test_index_view_with_future_question_and_past_question(self):
        create_question(question_text="Past_question.",day = -30)
        create_question(question_text="future_question.",day = 30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list']
            ,['<Question: Past_question.>'])


    def test_index_view_with_two_past_questions(self):
        create_question(question_text="Past_question1.",day=-30)
        create_question(question_text="Past_question2.",day=-20)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list']
            ,['<Question: Past_question2.>','<Question: Past_question1.>'])
       

class QuestionIndexDetailTests(TestCase) :

    def test_detail_view_with_a_future_question(self) :
        future_question = create_question(question_text="Future Question",day=30)
        reponse = self.client.get(reverse('polls:detail',args=(future_question.id,)))
        self.assertEqual(reponse.status_code,404)

    def test_detail_view_with_a_past_question(self):
        past_question = create_question(question_text="Past Question",day=-30)
        reponse = self.client.get(reverse('polls:detail',args=(past_question.id,)))
        self.assertContains(reponse,past_question.question_text,status_code=200)


class QuestionMethodTests(TestCase) :

    def test_was_published_recently_with_future_question(self) :

        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_feild=time)
        self.assertEqual(future_question.was_published_recently(),False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is older than 1 day.
        """
        past_time =  timezone.now() - datetime.timedelta(days=30)
        past_question = Question(pub_feild=past_time)
        self.assertEqual(past_question.was_published_recently(),False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() should return True for questions whose
        pub_date is within the last day.
        """
        recent_time =  timezone.now() - datetime.timedelta(hours=1)
        recent_question = Question(pub_feild=recent_time)
        self.assertEqual(recent_question.was_published_recently(),True)
        
