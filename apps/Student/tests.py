from django.test import TestCase, Client
from Student.models import Student

# Create your tests here.


class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(name='姬寅', sex=1, email='14831206@qq.com', profession='程序员', qq='333', phone='3222')
    
    def test_create_and_sex_show(self):
        Student.objects.create(name='姬寅1', sex=1, email='14831206@qq.com', profession='程序员', qq='333', phone='3222')
        self.assertEqual(Student.sex_show, '男', '性别内容展示不一致')

    def test_filter(self):
        Student.objects.create(name='姬寅3', sex=1, email='14831206@qq.com', profession='程序员', qq='333', phone='3222')
        name = '姬寅'
        students = Student.objects.filter(name=name)
        self.assertEqual(students.count(), 1, f'应该只存在一个记录, {name}')

    def test_get_index(self):
        clinet = Client()
        response = clinet.get('/')
        self.assertEqual(response.status_code, 200, '状态 200')
    
    def test_post_apps_Student(self):
        clinet = Client()
        data = dict(
                name='姬寅4',
                sex=1, email='14831206@qq.com', profession='程序员', qq='333', phone='3222'
        )
        response = clinet.post('/', data)
        self.assertEqual(response.status_code, 302, '状态 302')
        
        response = clinet.get('/')
        self.assertTrue(b"qq" in response.content, 'response content must `test_for_post`')
