from django.test import TestCase
from django.urls import reverse
from ayomi_website.authentication.models import MyUser


class SignupViewTest(TestCase):
    def setUp(self):
        self.test_user = MyUser.objects.create_user(username='testuser',
                                                    password='testpassword',
                                                    email='testuser@email.fr')
        self.test_user.save()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/inscription/')
        self.assertEqual(response.status_code, 200)

    def test_post_save_user_and_redirect_to_home(self):
        response = self.client.post('/inscription/',
                                    data={'username': 'testusername',
                                          'first_name': 'testfirstname',
                                          'last_name': 'testlastname',
                                          'email': 'test@email.com',
                                          'password1': 'TestPassword1*',
                                          'password2': 'TestPassword1*'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/'))
        self.assertEqual(MyUser.objects.latest('id').username, 'testusername')

    def test_post_fail(self):
        response = self.client.post('/inscription/',
                                    data={'username': 'testusernamefalse',
                                          'first_name': 'testfirstname',
                                          'last_name': 'testlastname',
                                          'email': 'test@email.com'})
        self.assertEqual(response.status_code, 200)
        self.assertFalse(
            MyUser.objects.latest('id').username == 'testusernamefalse')

    def test_get_show_redirect_to_signup(self):
        response = self.client.get('/inscription/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/signup.html')


class AccountViewTest(TestCase):
    def setUp(self):
        self.test_user = MyUser.objects.create_user(username='testuser',
                                                    password='testpassword',
                                                    email='testuser@email.fr')
        self.test_user.save()

    def test_account_view_uses_correct_user(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('account'))
        self.assertEqual(str(response.context['user']), 'testuser')
        self.assertEqual(response.status_code, 200)

    def test_account_view_uses_correct_template(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('account'))

        self.assertEqual(str(response.context['user']), 'testuser')
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'authentication/account.html')

    def test_account_view_redirect_to_login_if_user_not_authenticated(self):
        response = self.client.get(reverse('account'))

        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(''))


class ChangeEmailViewTest(TestCase):
    def setUp(self):
        self.test_user = MyUser.objects.create_user(username='testuser',
                                                    password='testpassword',
                                                    email='testuser@email.fr')
        self.test_user.save()

    def test_change_email_view_modify_email(self):
        self.client.login(username='testuser', password='testpassword')
        self.assertEqual(MyUser.objects.get(username='testuser').email,
                         'testuser@email.fr')
        response = self.client.post('/change_email/',
                                    data={'email': 'test2@email.com'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/account.html')
        self.assertEqual(MyUser.objects.get(username='testuser').email,
                         'test2@email.com')

    def test_change_email_view_uses_correct_template(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post('/change_email/',
                                    data={'email': 'test2@email.com'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/account.html')

    def test_view_redirect_to_login_if_user_not_authenticated(self):
        response = self.client.post('/change_email/',
                                    data={'email': 'test2@email.com'})

        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(''))
