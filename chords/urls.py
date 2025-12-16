from django.urls import path

from . import views


urlpatterns = [
    # path('', views.list, name='chords_list'),
    path('', views.ChordListView.as_view(), name='chords_list'),
    # path('/<int:pk>', views.details, name='chords_details'),
    path('/<int:pk>', views.ChordDetailView.as_view(), name='chords_details'),
    # path('/create', views.create, name='chords_create')
    path('/create', views.ChordCreateView.as_view(), name='chords_create')
]
