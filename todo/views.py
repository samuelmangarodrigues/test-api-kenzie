from urllib import response
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView,Request,Response,status
from todo.models import Todo
from todo.serializers import TodoSerializer

class TodoView(APIView):
    def get(self,_:Request):

        all_todo=Todo.objects.all()
        serialized = TodoSerializer(instance = all_todo, many=True)
    

        return Response(serialized.data,status.HTTP_200_OK)
    
    def post(self,request:Request):

        serialized = TodoSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)

        try:
            serialized.save()


            return Response(serialized.data,status.HTTP_201_CREATED)

        except ValueError as err:
            return Response(*err.args)

class TodoViewId(APIView):

    def get(self, _: Request, todo_id: int):
        try:
            todo = get_object_or_404(Todo, pk=todo_id)
            serialized = TodoSerializer(todo)

            return Response(serialized.data, status.HTTP_200_OK)

        except Http404:
            return Response({"detail": "Task not found."}, status.HTTP_404_NOT_FOUND)


    def patch(self,request:Request,todo_id: int):
        try:
            todo = get_object_or_404(Todo,pk=todo_id)
            serialized = TodoSerializer(instance=todo,data=request.data)
            serialized.is_valid(raise_exception=True)
            serialized.save()
            

            return Response(serialized.data,status.HTTP_200_OK)
        
        except Http404:
            return Response({"Detail":"Todo not find"},status.HTTP_404_NOT_FOUND)


    def delete(self, _: Request, todo_id: int):
        try:
            todo = get_object_or_404(Todo, pk=todo_id)
            todo.delete()
            serialized = TodoSerializer(todo)

            return Response({"message":"deleted"}, status.HTTP_200_OK)

        except Http404:
            return Response({"detail": "Todo not found."}, status.HTTP_404_NOT_FOUND)
    
    def put(self,_: Request, todo_id:int):
        try:
            todo=get_object_or_404(Todo,pk=todo_id)
            todo.completed = True
            todo.save()
            serialized = TodoSerializer(todo)

            return Response(serialized.data, status.HTTP_200_OK)
        except Http404:

            
            return Response({"detail":"Todo not find"}, status.HTTP_404_NOT_FOUND)
