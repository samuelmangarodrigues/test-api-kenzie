from rest_framework.test import APITestCase
from todo.models import Todo

class TodoViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.url = "/api/todo/"
        cls.task_one = {
	        "description":"testando"
        }
        cls.patch_task={
            "description":"atualizado"
        }
        cls.id_task=3

    def test_create_task(self)-> None:
        response = self.client.post(self.url, self.task_one)
        self.assertEqual(response.status_code, 201)
