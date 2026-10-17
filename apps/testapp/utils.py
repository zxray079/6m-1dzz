from django.urls import include, path
from apps.testapp.views import PublicDataView, SecretModeratorView


urlpatterns = [
    path('public/', PublicDataView.as_view(), name='public-data'),
    path('secret/', SecretModeratorView.as_view(), name='secret-data'),
    path("api/v1/testapp/", include("apps.testapp.urls"))

]
