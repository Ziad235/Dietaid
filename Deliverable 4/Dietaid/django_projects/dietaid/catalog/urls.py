from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('books/', views.BookListView.as_view(), name='books'),
    #path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'), # pk short for primary key
]

urlpatterns += [
    path('create_diagnosis/', views.create_diagnosis, name = 'create-diagnosis'),
]

urlpatterns += [
    path('diagnosis/', views.diagnosis_detail_view, name ='diagnosis-detail'),
]

urlpatterns+=[
    path('generate_mealplan/', views.generate_mealplan, name = 'generate-mealplan'),
]

urlpatterns+=[
    path('mealplan/', views.mealplan_detail_view, name='mealplan-detail'),
]

urlpatterns+=[
    path('edit_mealplan/', views.edit_mealplan, name = 'edit-mealplan'),
]