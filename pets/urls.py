from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^api/v1/pets/$',
        views.get_post_pets,
        name='get_post_pets'
    ),
    url(
        r'^api/v1/pets/(?P<pk>[0-9]+)$',
        views.get_delete_update_pets,
        name='get_delete_update_pets'
    )
]