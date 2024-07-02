from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Profile
from .helpers import *

# class LoginView(APIView):

#     def post(self, request):
#         response = {}
#         response['status'] = 500
#         response['message'] = 'Something went wrong'
#         try:
#             data = request.data
#             print(data.get('username'))

#             if data.get('username') is None:
#                 response['message'] = ' Key username not found'
#                 raise Exception('Key username not found')
            
#             if data.get('password') is None:
#                 response['message'] = 'Key password is not found'
#                 raise Exception('Key password is not found')
            
#             try:
#                 check_user = User.objects.filter(username=data.get('username')).first()

#                 if check_user is None:
#                     response['message'] = 'Username is not found'
#                     raise Exception('Username is not found')
                
#                 if not Profile.objects.filter(user=check_user).first().is_verified:
#                     response['message'] = 'Your Profile is not verified'
#                     raise Exception('Profile not verified')

#                 user_obj = authenticate(username = data.get('username'), password = data.get('password') )


#                 if user_obj:
#                     login(request, user_obj)
#                     response['status'] = 200
#                     response['message'] = 'Welcome to our Blog'
#                 else:
#                     response['message'] = 'Password is not Valid'
#                     raise Exception('Password is not Valid')

                

#             except Exception as e:
#                 print(e)
            
            

#         except Exception as e:
#             print(e)

#         return Response(response)
            

class LoginView(APIView):

    def post(self, request):
        response = {
            'status': 500,
            'message': 'Something went wrong'
        }
        try:
            data = request.data
            username = data.get('username')
            password = data.get('password')
            print(f"Received login attempt for username: {username}")

            if username is None:
                response['message'] = 'Key username not found'
                raise Exception('Key username not found')

            if password is None:
                response['message'] = 'Key password is not found'
                raise Exception('Key password is not found')

            check_user = User.objects.filter(username=username).first()
            if check_user is None:
                response['message'] = 'Username is not found'
                raise Exception('Username is not found')

            profile = Profile.objects.filter(user=check_user).first()
            if profile is None:
                response['message'] = 'Profile not found'
                raise Exception('Profile not found')

            if not profile.is_verified:
                response['message'] = 'Your Profile is not verified'
                raise Exception('Profile not verified')

            user_obj = authenticate(username=username, password=password)
            if user_obj:
                login(request, user_obj)
                response['status'] = 200
                response['message'] = 'Welcome to our Blog'
            else:
                response['message'] = 'Password is not valid'
                raise Exception('Password is not valid')

        except Exception as e:
            print(f"Error during login: {e}")

        return Response(response)
    

LoginView = LoginView.as_view()

class RegisterView(APIView):

    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong'
        try:
            data = request.data

            if data.get('username') is None:
                response['message'] = ' Key username not found'
                raise Exception('Key username not found')
            
            if data.get('password') is None:
                response['message'] = 'Key password is not found'
                raise Exception('Key password is not found')
            
            try:
                check_user = User.objects.filter(username=data.get('username')).first()

                if check_user:
                    response['message'] = 'Username is already taken'
                    raise Exception('Username is already taken')

                user_obj = User.objects.create(email = data.get('username'),username = data.get('username'))
                user_obj.set_password(data.get('password'))
                user_obj.save()
                token = generate_random_string(20)
                Profile.objects.create(user=user_obj, token = token, is_verified=True)
                # send_mail_to_user(token, data.get('username'))

                response['message'] = 'User created'
                response['status'] = 200

                

            except Exception as e:
                print(e)
            
            

        except Exception as e:
            print(e)

        return Response(response)
    

RegisterView = RegisterView.as_view()