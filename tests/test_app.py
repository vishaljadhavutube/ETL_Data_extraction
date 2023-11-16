import unittest
from app import app


class FlaskAppTest(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_index_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Upload a PDF file', response.data)

    def test_upload_file(self):
        pdf_content = b'%PDF-1.5\nTest PDF content'
        with app.test_request_context('/', method='POST', data={'file': (BytesIO(pdf_content), 'test.pdf')}):
            response = self.app.post('/')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Extracted Data', response.data)
            self.assertIn(b'Test PDF content', response.data)

if __name__ == '__main__':
    unittest.main()