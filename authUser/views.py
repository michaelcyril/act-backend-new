from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from .serializer import UserSerializer
from django.contrib.auth import authenticate, login, logout
from .token import get_user_token
from .models import User
# import for change the password
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from rest_framework import status

# Create your views here.
# import re
#
#
# def validate_password(password):
#     pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()-_=+\\|[\]{};:'\",.<>/?])\S{8,}$"
#
#     if not password:
#         return Response({"message": "Password is required."})
#     elif len(password) < 8:
#         return Response({"message":"Password must be at least 8 characters long."})
#     elif not re.match(pattern, password):
#         return Response({"message":"Password must contain at least one digit, one lowercase letter, one uppercase letter, and one special character."})
#     else:
#         pass


@api_view(["POST", "GET"])
@permission_classes([AllowAny])
def RegisterUser(request):
    if request.method == "POST":
        data = request.data
        # validate_password(data['password'])
        username = data['username']
        # user = None
        user = User.objects.filter(username=username)
        if user:
            message = {'message': 'user does exist'}
            return Response(message)

        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            message = {'save': True}
            return Response(message)
        else:
            message = {'save': False}
            return Response(message)
    return Response({'message': "hey bro"})


# {
#     "first_name":"acts",
#     "last_name":"acts",
#     "username":"actsAdmin",
#     "email":"actsAdmin@gmail.com",
#     "password":"actsAdmin"
# }

@api_view(["POST", "GET"])
@permission_classes([AllowAny])
def LoginView(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        user_id = User.objects.values('id', 'username', 'first_name', 'last_name', 'email').get(username=username)
        # profile_id = Profile.objects.values('id', 'ward_id', 'user_id', 'phone', 'description').get(user_id=user_id)

        response = {
            'user': user_id,
            # 'profile_id': profile_id,
            'token': get_user_token(user),
        }

        return Response(response)
    else:
        response = {
            'msg': 'Invalid username or password',
        }

        return Response(response)


# {
#     "username": "mike",
#     "password": "123"
# }


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    form = PasswordChangeForm(user=request.user, data=request.data)
    if form.is_valid():
        user = form.save()
        update_session_auth_hash(request, user)
        return Response({'status': 'success'}, status=status.HTTP_200_OK)
    else:
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

# {
#     "old_password": "acts",
#     "new_password1": "123",
#     "new_password2": "123"
# }
