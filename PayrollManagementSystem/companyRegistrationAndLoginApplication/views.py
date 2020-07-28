from django.shortcuts import render
from . serializers import LoginSerializer,HolidaySerializer

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from .models import AdminUser,Holidays,Companies

# Create your views here.


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        userId = request.user.id
        username = request.user.username
        companyId = AdminUser.objects.filter(adminId=username).values('companyId')
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "userId": userId, "username": username, "companyId": companyId}, status=200)


class LogoutView(APIView):
    authentication_classes = (TokenAuthentication, )

    def post(self, request):
        logout(request)
        return Response(status=204)

# this is user defined method
# perform makemigrations
# perform migrate
# login
# api --->  http://localhost:8080/auth/login/
# logout
# api --->  http://localhost:8080/auth/logout/
# for using default method----
# type  in cmd- pip install djoser
# api ----> http://localhost:8080/auth/token/login/
# api ----> http://localhost:8080/auth/token/logout/


class HolidayView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        username = request.user.username
        companyId = AdminUser.objects.filter(adminId=username).values('companyId')
        holi = Holidays.objects.filter(companyId__in=companyId)
        serializer = HolidaySerializer(holi , many=True)
        return Response(serializer.data)

    def post(self,request):
        data = request.data
        username = request.user.username
        companyId = AdminUser.objects.filter(adminId=username).values('companyId')
        a = Companies.objects.get(companyId__in=companyId)
        serializer = HolidaySerializer(data=data)
        if serializer.is_valid():
            holidayName = serializer.validated_data['holidayName']
            date = serializer.validated_data['date']
            day = serializer.validated_data['day']
            month = serializer.validated_data['month']
            year = serializer.validated_data['year']
            hol = Holidays.objects.filter(holidayName=holidayName,companyId=a)
            if hol:
                return Response("Holiday Exist")
            else:
                serializer.save(companyId=a,holidayName=holidayName,date=date,day=day,month=month,year=year)
                return Response(serializer.data , status=201)
        return Response("message:sorry",status=400)


class HolidayViewDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self,id):
        return Holidays.objects.get(holidayId=id)   
        

    def get(self,request,id=None):
        holidayId=id
        username = request.user.username
        companyId = AdminUser.objects.filter(adminId=username).values('companyId')
        username = request.user.username
        companyId = AdminUser.objects.filter(adminId=username).values('companyId')
        a = Companies.objects.get(companyId__in=companyId)
        hol = Holidays.objects.filter(holidayId=holidayId,companyId=a)
        if hol:
            instance = self.get_object(holidayId)
            serializer = HolidaySerializer(instance)
            return Response(serializer.data)  
        else:
            return Response ("Holidays Not Exists")
        

    def put(self,request,id=None):
                holidayId=id
                data = request.data
                username = request.user.username
                companyId = AdminUser.objects.filter(adminId=username).values('companyId')
                a = Companies.objects.get(companyId__in=companyId)
                instance = self.get_object(holidayId)
                serializer = HolidaySerializer(instance,data=data)
                if serializer.is_valid():
                    holidayName = serializer.validated_data['holidayName']
                    date = serializer.validated_data['date']
                    day = serializer.validated_data['day']
                    month = serializer.validated_data['month']
                    year = serializer.validated_data['year']
                    hol = Holidays.objects.filter(holidayName=holidayName,companyId=a)
                    if hol:
                        return Response("Holiday Exist")
                    serializer.save()
                    return Response(serializer.data , status=201)
                return Response(status=400)


    def delete(self,request,id):
        holidayId = id 
        instance =  self.get_object(holidayId)
        instance.delete()
        return Response("Holiday is Deleted",status=201)