from .helpers import TestCase


class TestHotel(TestCase):

    def test_list(self):
        rv = self.client.get('/hotels')
        assert "Hello world!" in rv.data

    def test_add(self):
        rv = self.client.post('/hotels/add', {})
        assert "added" in rv.data

    def test_search(self):
        rv = self.client.get('/hotels/find', {})
        assert "searched for" in rv.data


