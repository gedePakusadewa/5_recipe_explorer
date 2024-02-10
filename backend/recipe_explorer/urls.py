from django.urls import path
from recipe_explorer.views import LogIn, SignUp, LogOut, RecipeExplorer

urlpatterns= [
    path('login', LogIn.as_view()),
    path('signup', SignUp.as_view()),
    path('logout', LogOut.as_view()),
    path('', RecipeExplorer.as_view())
]