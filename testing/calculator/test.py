from unittest import TestCase
import mock
from unittest.mock import patch
from main import Calculator, Blog
import main


def mock_add_side_effect(a, b):
    return a + b


class TestCalculator(TestCase):
    def setUp(self):
        self.calc = Calculator()

    # def test_add1(self):
    #     answer = self.calc.add(2, 4)
    #     self.assertEqual(answer, 6)

    @patch('main.Calculator.add', return_value=9)
    def test_add2(self, add):
        self.assertEqual(add(2, 3), 9)

    def test_add3(self):
        with patch('main.Calculator.add') as mock_add:
            mock_add.return_value = 6
            answer = mock_add(2, 4)
            self.assertEqual(answer, 6)

    def test_add4(self):
        with patch('main.Calculator.add', return_value=6) as mock_add:
            answer = mock_add(2, 4)
            self.assertEqual(answer, 6)

    @patch('main.Calculator.add')
    def test_add5(self, mock_add):
        mock_add.return_value = 9
        self.assertEqual(mock_add(2, 3), 9)

    @patch('main.Calculator.add', side_effect=mock_add_side_effect)
    def test_add6(self, mock_add):
        self.assertEqual(mock_add(2, 3), 5)
        self.assertEqual(mock_add(7, 3), 10)

    @patch('main.Calculator.add')
    def test_add7(self, add):
        add.side_effect = mock_add_side_effect
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(7, 3), 10)

    @patch('main.Blog')
    def test_blog_posts(self, MockBlog):
        blog = MockBlog()

        blog.posts.return_value = [
            {
                'userId': 1,
                'id': 1,
                'title': 'Test Title',
                'body': 'Far out in the uncharted backwaters of the unfashionable  end  of the  western  spiral  arm  of  the Galaxy\ lies a small unregarded yellow sun.'
            }
        ]

        response = blog.posts()
        self.assertIsNotNone(response)
        self.assertIsInstance(response[0], dict)
        # Additional assertions

        # The mock is equivalent to the original
        assert MockBlog is main.Blog
        assert MockBlog is not Blog
        # The mock was called
        assert MockBlog.called
        # We called the posts method with no arguments
        blog.posts.assert_called_with() 
        # We called the posts method once with no arguments
        # blog.posts.assert_called_with(1, 2, 3) - This assertion is False and will fail since we called blog.posts with no arguments
        blog.posts.assert_called_once_with() 
        # Reset the mock object
        blog.reset_mock() 
        # After resetting, posts has not been called.
        blog.posts.assert_not_called() 


