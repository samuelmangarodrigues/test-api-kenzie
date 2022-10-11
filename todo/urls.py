from django.urls import path
from todo.views import TodoView, TodoViewId

urlpatterns=[
    path("todo/",TodoView.as_view()),
    path("todo/<int:todo_id>/",TodoViewId.as_view())
]