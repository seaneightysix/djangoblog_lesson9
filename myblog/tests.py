import datetime
from django.utils.timezone import utc
from django.test import TestCase
from django.contrib.auth.models import User
from myblog.models import Post, Genre
from django.test import Client


class FrontEndTestCase(TestCase):
    """test views provided in the front-end"""
    fixtures = ['myblog_test_fixture.json', ]
    c = Client()

    def setUp(self):
        self.now = datetime.datetime.utcnow().replace(tzinfo=utc)
        self.timedelta = datetime.timedelta(15)
        author = User.objects.get(pk=1)
        for count in range(1, 11):
            post = Post(title="Post %d Title" % count,
                        text="foo",
                        author=author,
                        published_date = self.now
                        )
            post.save()

    
    def test_list_only_published(self):
        resp = self.client.get('/')
        # the content of the rendered response is always a bytestring
        resp_text = resp.content.decode(resp.charset)
        self.assertTrue("Recent Posts" in resp_text)
        for count in range(1, 11):
            title = "Post %d Title" % count
            self.assertContains(resp, title, count=1)
    
    def test_details_only_published(self):
        for count in range(1, 11):
            title = "Post %d Title" % count
            post = Post.objects.get(title=title)
            resp = self.c.get('/myblog/%d/' % post.pk)
            self.assertEqual(resp.status_code, 200)
            self.assertContains(resp, title)


class PostTestCase(TestCase):
    fixtures = ['myblog_test_fixture.json', ]

    def test_string_representation(self):
        expected = "This is a title"
        p1 = Post(title=expected)
        actual = str(p1)
        self.assertEqual(expected, actual)

    def setUp(self):
        self.user = User.objects.get(pk=1)


class GenreTestCase(TestCase):

    def test_string_representation(self):
        expected = "poetry"
        c1 = Genre(name=expected)
        actual = str(c1)
        self.assertEqual(expected, actual)