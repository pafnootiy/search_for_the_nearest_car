
from django.contrib import admin
from django.urls import path
from searching_app.views import (
    create_cargo,
    get_cargo_list,
    get_cargo,
    update_machine,
    update_cargo,
    delete_cargo,
)

urlpatterns = [
    path('cargo/', create_cargo, name='create_cargo'),
    path('cargo/list/', get_cargo_list, name='get_cargo_list'),
    path('cargo/<int:cargo_id>/', get_cargo, name='get_cargo'),
    path('machine/<int:machine_id>/', update_machine, name='update_machine'),
    path('cargo/<int:cargo_id>/', update_cargo, name='update_cargo'),
    path('cargo/<int:cargo_id>/delete/', delete_cargo, name='delete_cargo'),
    path('admin/', admin.site.urls),
]
