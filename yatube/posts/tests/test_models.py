from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import Group, Post

LEN_OF_POSTS = 15
User = get_user_model()


class PostModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='test_name')
        cls.post = Post.objects.create(
            author=cls.user,
            text='Тестовый пост более 15 символов!',
        )
        cls.group = Group.objects.create(
            title='Тестовая группа',
            slug='Тестовый слаг',
            description='Тестовое описание',
        )

    def test_verbose_name(self):
        '''Проверка заполнения verbose_name'''
        field_verboses = {'text': 'Текст поста',
                          'pub_date': 'Дата публикации',
                          'group': 'Группа',
                          'author': 'Автор'}
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                error_name = f'Поле {field} ожидало значение {expected_value}'
                self.assertEqual(
                    self.post._meta.get_field(field).verbose_name,
                    expected_value, error_name)

    def test_title_help_text(self):
        '''Проверка заполнения help_text'''
        field_help_texts = {'text': 'Введите текст поста',
                            'group': 'Группа, относительно поста'}
        for field, expected_value in field_help_texts.items():
            with self.subTest(field=field):
                error_name = f'Поле {field} ожидало значение {expected_value}'
                self.assertEqual(
                    self.post._meta.get_field(field).help_text,
                    expected_value, error_name)

    def test_models_have_correct_object_names(self):
        """Проверяем, что у моделей корректно работает __str__."""
        post = PostModelTest.post
        error_name = f"Вывод не имеет {LEN_OF_POSTS} символов"
        expected_object_name = post.text[:15]
        self.assertEqual(expected_object_name, str(post), error_name)

    def test_models_title_filed(self):
        """Проверяем, что есть название группы"""
        group = PostModelTest.group
        expected_object_name = group.title
        self.assertEqual(expected_object_name, str(group))
