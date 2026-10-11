from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.db.utils import IntegrityError

from .forms import RegForm, AuthForm, EditEmailForm, EditPasswordForm, EditUsernameForm, ReviewForm
from .models import SightModel, ReviewModel, InformationModel


import uuid


User = get_user_model()


def main_page(request):
    sight = SightModel.objects.all()
    return render(request, 'main.html', {"form": sight})
                  

def sight_page(request, id):
    state_review = False
    sight = SightModel.objects.get(id=id)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST) 
        if review_form.is_valid():
            text = review_form.cleaned_data["text"]
            grade = review_form.cleaned_data["grade"]
            if request.user.is_authenticated:
                review = ReviewModel.objects.filter(username__id=request.user.id).exists()
                if review == True:
                    state_review = True
                    review_check = ReviewModel.objects.filter(sight__id=id).all()
                    return render(request, 'sight.html', {
                            "form": sight, 
                            "review_form": review_form, 
                            "reviews": review_check, 
                            "id": id,
                            "state": state_review
                        })
                sight.reviewmodel_set.create(description=text, grade=grade, username=request.user)
                return redirect('sight', id=id)
            else:
                return redirect('auth')
    else:
        review_form = ReviewForm()
    review_check = ReviewModel.objects.filter(sight__id=id).all()
    
    return render(request, 'sight.html', {
        "form": sight, 
        "review_form": review_form, 
        "reviews": review_check, 
        "id": id,
        "state": state_review
    })



def reg_page(request):
    reg_form = RegForm(request.POST)
    if reg_form.is_valid():
        username = reg_form.cleaned_data["username"]
        email = reg_form.cleaned_data["email"]
        password = reg_form.cleaned_data["password"]
        try:
            user = User.objects.create_user(username, email, password)
            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, user)
                return redirect("main")
            else:
                return HttpResponse("invalid login")
        except IntegrityError:
            return HttpResponse("a user with that name already exists.")
    return render(request, 'reg.html', {"form": reg_form})


def auth_page(request):
    auth_form = AuthForm(request.POST)
    if auth_form.is_valid():
        username = auth_form.cleaned_data["username"]
        password = auth_form.cleaned_data["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            return HttpResponse("invalid password or login")
    else:
        return render(request, 'auth.html', {"form": auth_form})


def info_page(request):
    info = InformationModel.objects.all()
    return render(request, 'info.html', {"form": info})


def logout_func(request):
    logout(request)
    redirect("main")

#внизу сделал ИИ(gemini)
def profile_page(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        username = request.user.username
        email = request.user.email
        
        # Передаем формы в контекст, чтобы они отображались на странице
        return render(request, 'profile.html', {
            "user_id": user_id, 
            "username": username, 
            "email": email,
            "username_form": EditUsernameForm(),
            "email_form": EditEmailForm(),
            "password_form": EditPasswordForm(),
        })
    else:
        return redirect('auth')


def edit_username(request):
    try:
        username = request.user.username
        user = User.objects.get(username=username)
        
        # Принимаем и валидируем форму
        form = EditUsernameForm(request.POST)
        if form.is_valid():
            new_username = form.cleaned_data.get("username")
            user.username = new_username
            user.save()
            
            resp = HttpResponse()
            resp.status_code = 204
            return resp
        else:
            resp = HttpResponse("Некорректный логин")
            resp.status_code = 400
            return resp
            
    except User.DoesNotExist:
        resp = HttpResponse()
        resp.status_code = 404
        return resp
    except Exception as e:
        resp = HttpResponse()
        resp.status_code = 500
        return resp


def edit_email(request):
    try:
        username = request.user.username
        user = User.objects.get(username=username)
        
        # Принимаем и валидируем форму
        form = EditEmailForm(request.POST)
        if form.is_valid():
            new_email = form.cleaned_data.get("email") 
            user.email = new_email
            user.save()
            
            resp = HttpResponse()
            resp.status_code = 204
            return resp
        else:
            resp = HttpResponse("Некорректная почта")
            resp.status_code = 400
            return resp
            
    except User.DoesNotExist:
        resp = HttpResponse()
        resp.status_code = 404
        return resp
    except Exception as e:
        resp = HttpResponse()
        resp.status_code = 500
        return resp


def edit_password(request):
    try:
        username = request.user.username
        user = User.objects.get(username=username)
        
        # Принимаем и валидируем форму
        form = EditPasswordForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get("password") 
            user.set_password(password)
            user.save()
            
            resp = HttpResponse()
            resp.status_code = 204
            return resp
        else:
            resp = HttpResponse("Некорректный пароль")
            resp.status_code = 400
            return resp
            
    except User.DoesNotExist:
        resp = HttpResponse()
        resp.status_code = 404
        return resp
    except Exception as e:
        resp = HttpResponse()
        resp.status_code = 500
        return resp


def delete_user(request):
    try:
        username = request.user.username
        user = User.objects.get(username=username)
        user.delete()
        resp = HttpResponse()
        resp.status_code = 204
        return redirect("main")
    except User.DoesNotExist:
        resp = HttpResponse()
        resp.status_code = 404
        return resp
    except Exception as e:
        resp = HttpResponse()
        resp.status_code = 500
        return resp