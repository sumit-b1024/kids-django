from django.urls import path
from . import views
app_name = 'quiz'

urlpatterns = [
    path('', views.index, name='home'),
    path('mathtopicselection/', views.mathtopicselection, name="mathtopicselection"),
    path('numbersintro/', views.numbersintro, name="numbersintro"),
    path('additionintro/', views.additionintro, name="additionintro"),
    path('numberquiz/', views.numberquiz, name="numberquiz"),
    path('additionquiz/', views.additionquiz, name="additionquiz"),

    path('englishtopicselection/', views.englishtopicselection, name="englishtopicselection"),
    path('englishtopicselection/a_e/', views.a_e, name="a_e"),
    path('englishtopicselection/f_j/', views.f_j, name="f_j"),
    path('englishtopicselection/k_o/', views.k_o, name="k_o"),
    path('englishtopicselection/p_t/', views.p_t, name="p_t"),
    path('englishtopicselection/u_z/', views.u_z, name="u_z"),
    
    path('creativelearning/', views.creativelearning, name="creativelearning"),
    path('creativelearningdev/', views.creativelearningDev, name="creativelearningDev"),
    path('draw/', views.mathDraw, name="mathDraw"),
]