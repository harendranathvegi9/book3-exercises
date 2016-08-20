from django.test import TestCase
from django.core.urlresolvers import resolve
from .views import index
from django.shortcuts import render_to_response
from django.test import RequestFactory
import mock


class MainPageTests(TestCase):

    ###############
    #### Setup ####
    ###############

    @classmethod
    def setUpClass(cls):
        super(MainPageTests,cls).setUpClass()
        request_factory = RequestFactory()
        cls.request = request_factory.get('/')
        cls.request.session = {}

    ##########################
    ##### Testing routes #####
    ##########################

    def test_root_resolves_to_main_view(self):
        main_page = resolve('/')
        self.assertEqual(main_page.func, index)

    def test_returns_appropriate_html_response_code(self):
        resp = index(self.request)
        self.assertEquals(resp.status_code, 200)

    #####################################
    #### Testing templates and views ####
    #####################################

    def test_returns_exact_html(self):
        resp = index(self.request)
        self.assertEquals(
            resp.content,
            render_to_response("index.html").content
        )

    def test_index_handles_logged_in_user(self):
        # Create a session that appears to have a logged in user
        self.request.session = {"user": "1"}

        with mock.patch('main.views.User') as user_mock:

            # Tell the mock what to do when called
            config = {'get_by_id.return_value': mock.Mock()}
            user_mock.configure_mock(**config)

            # Run the test
            resp = index(self.request)

            # Ensure we return the state of the session back to normal
            self.request.session = {}

            expected_html = render_to_response(
                'user.html', {'user': user_mock.get_by_id(1)}
            )
            self.assertEquals(resp.content, expected_html.content)
            


class User(models.Model):

    name = model.CharField()
    pwd = model.CharField()
    birthdate = model.DateField()

    def get_sign():
        if birthdate.month == "Jan":
            return "Capricorn"
        elif birthdate.monty == "Feb"
           return "Sagitarius"

    def is_active_twitter_user():
        # call twitter with
        # is user.name a user on twitter
        is_active = twitter.check_user(user.name)
        return is_active


def test_get_sign()
    myuser = User("jj", "pwd", "Jan")
    self.assertEquals(myuser.get_sign(), "Capricorn")

    myuser = User("jj", "pwd", "Feb")
    self.assertEquals(myuser.get_sign(), "Sagitarius")

    myuser = User("jj", "pwd", "32")
    self.assertEquals(myuser.get_sign(), "Sagitarius")




--- test.py

