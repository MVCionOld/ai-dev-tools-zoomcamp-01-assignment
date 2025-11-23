from django.test import TestCase, Client
from django.urls import reverse
from datetime import date, timedelta
import json
from .models import Todo

# Create your tests here.

class TodoModelTest(TestCase):
    """Test cases for Todo model"""
    
    def test_create_todo(self):
        """Test creating a todo"""
        todo = Todo.objects.create(
            title="Test TODO",
            description="Test description",
            due_date=date.today() + timedelta(days=7)
        )
        self.assertEqual(todo.title, "Test TODO")
        self.assertEqual(todo.description, "Test description")
        self.assertFalse(todo.is_resolved)
    
    def test_todo_string_representation(self):
        """Test todo string representation"""
        todo = Todo.objects.create(title="Test TODO")
        self.assertEqual(str(todo), "Test TODO")


class TodoViewsTest(TestCase):
    """Test cases for Todo views"""
    
    def setUp(self):
        """Set up test client"""
        self.client = Client()
    
    def test_index_view(self):
        """Test index view renders correctly"""
        response = self.client.get(reverse('todos:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "My TODOs")
    
    def test_todo_list_api(self):
        """Test todo list API endpoint"""
        # Create test todos
        Todo.objects.create(title="Test TODO 1")
        Todo.objects.create(title="Test TODO 2")
        
        response = self.client.get(reverse('todos:todo_list'))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(len(data), 2)
    
    def test_todo_create_api(self):
        """Test creating a todo via API"""
        data = {
            'title': 'New TODO',
            'description': 'Test description',
            'due_date': str(date.today())
        }
        response = self.client.post(
            reverse('todos:todo_create'),
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Todo.objects.count(), 1)
    
    def test_todo_update_api(self):
        """Test updating a todo via API"""
        todo = Todo.objects.create(title="Original Title")
        
        data = {'title': 'Updated Title'}
        response = self.client.put(
            reverse('todos:todo_update', args=[todo.id]),
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        
        todo.refresh_from_db()
        self.assertEqual(todo.title, 'Updated Title')
    
    def test_todo_delete_api(self):
        """Test deleting a todo via API"""
        todo = Todo.objects.create(title="To Delete")
        
        response = self.client.delete(
            reverse('todos:todo_delete', args=[todo.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Todo.objects.count(), 0)
    
    def test_mark_todo_resolved(self):
        """Test marking a todo as resolved"""
        todo = Todo.objects.create(title="Test TODO")
        
        data = {'is_resolved': True}
        response = self.client.put(
            reverse('todos:todo_update', args=[todo.id]),
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        
        todo.refresh_from_db()
        self.assertTrue(todo.is_resolved)

