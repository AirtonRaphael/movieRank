from .views import Index, Login, Register


from django.urls import path

urlpatterns = [
    path('index', Index.as_view(), name='index'),
    path('login', Login.as_view(), name='login'),
    path('register', Register.as_view(), name='register')
]