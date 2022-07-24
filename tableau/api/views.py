from .models import Employee
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EmployeeSerializer

@api_view(['GET', 'POST'])
def employee_get_view(request):
    if request.method == "GET":
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


