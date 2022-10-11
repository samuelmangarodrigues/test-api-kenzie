from pydoc import describe
from django.test import TestCase
from todo.models import Todo

class TodoTest(TestCase):

    @classmethod
    def setUpTestData(cls)-> None:
        
        cls.description="Primeira descrição"
        cls.todo_obj:Todo = Todo.objects.create(
            description= cls.description
        )
    
    def test_todo_fields(self):

        self.assertIsInstance(self.todo_obj, Todo)
        self.assertIsInstance(self.todo_obj.description,str)
        self.assertEqual(self.todo_obj.description,self.description)
        self.assertFalse(self.todo_obj.completed)
    