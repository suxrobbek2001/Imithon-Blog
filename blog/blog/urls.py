from django.contrib import admin
from django.urls import path

from blogapp.views import LoginView, RoyhatView, BlogView, MaqolaView, LoGout, All_BlogView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView, name="login"),
    path('royhat/', RoyhatView, name="royhat"),
    path('blog/', All_BlogView, name="blog"),
    path('blog/submit', BlogView, name='submit'),
    path('maqola/<int:son>/', MaqolaView, name="maqola"),
    path('logout/', LoGout, name="logout"),
]