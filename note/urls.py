# yourapp/urls.py
from django.urls import path
from . import api_views

urlpatterns = [
    path("api/notes/", api_views.NoteListCreateView.as_view(), name="note-list-create"),
    path("api/notes/<int:pk>/", api_views.NoteDetailView.as_view(), name="note-detail"),
]
