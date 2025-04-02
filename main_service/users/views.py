import uuid
import json


from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import User
from django.http import JsonResponse



@csrf_exempt
def register_page(request):
    if request.method == "GET":
        return render(request, "users/register.html")

    elif request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid JSON"}, status=400)

        email = data.get("email")
        username = data.get("username")
        password = data.get("password")

        if not email or not username or not password:
            return JsonResponse({"message": "All fields are required"}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({"message": "Username already taken"}, status=400)

        if User.objects.filter(email=email).exists():
            return JsonResponse({"message": "Email already registered"}, status=400)

        user = User(id=uuid.uuid4(), email=email, username=username)
        user.set_password(password)
        user.save()

        return JsonResponse({"message": "User registered successfully"}, status=201)


@csrf_exempt
def login_page(request):
    if request.method == "GET":
        return render(request, "users/login.html")

    if request.method == "POST":
        try:
            data = json.loads(request.body)
            email = data.get("email")
            password = data.get("password")

            if not email or not password:
                return JsonResponse({"message": "Email and password are required"}, status=400)

            user = User.objects.filter(email=email).first()

            if not user:
                return JsonResponse({"message": "User with this email does not exist"}, status=404)

            if not user.check_password(password):
                return JsonResponse({"message": "Incorrect password"}, status=401)

            return JsonResponse({"message": "Login successful"}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid JSON"}, status=400)

    return JsonResponse({"message": "Method not allowed"}, status=405)