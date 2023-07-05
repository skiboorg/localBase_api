import json

from rest_framework import filters
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .models import *
from rest_framework import generics, viewsets, parsers


class TabViewSet(viewsets.ModelViewSet):
    serializer_class = TabSerializer
    queryset = Tab.objects.all()
    lookup_field = 'id'

class ParamViewSet(viewsets.ModelViewSet):
    serializer_class = ParamSerializer
    queryset = Param.objects.all()
    lookup_field = 'id'

class RecordViewSet(viewsets.ModelViewSet):
    serializer_class = RecordSerializer
    queryset = Record.objects.all()
    lookup_field = 'id'

    def perform_create(self, serializer):
        print(self.request.data)
        data = self.request.data
        obj = serializer.save(tab_id=data['tab_id'], name=data['data']['name'])
        print(obj)
        for item in data['data']['params']:
            print(item.items())
            for k,v in item.items():
                print(k,v)
                p = Param.objects.get(name=k)
                RecordParam.objects.create(record=obj,param=p,value=v)




class ColumnViewSet(viewsets.ModelViewSet):
    serializer_class = ColumnSerializer
    queryset = Column.objects.all()
    lookup_field = 'id'

    def perform_create(self, serializer):
        last_column = Column.objects.all().last()
        serializer.save(order_num=last_column.order_num+1)

class ReorderColumns(APIView):
    def post(self, request):
        print(request.data)
        data = request.data
        i = 0
        for item in data:
            print(item)
            column = Column.objects.get(id=item['id'])
            column.order_num = i
            i += 1
            column.save()
            ii = 0
            for task_id in item['tasks']:
                task = Task.objects.get(id=task_id)
                task.order_num = ii
                task.column = column
                task.save()
                ii += 1

        return Response(status=200)