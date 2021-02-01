from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^course/$', views.CourseListView.as_view(), name='courses'),
    url(r'^course/(?P<pk>\d+)$', views.CourseDetailView.as_view(), name='course-detail'),
    url(r'^card/(?P<pk>\d+)$', views.CardListView.as_view(), name='cards'),
    url(r'^card/(?P<pk>\d+)$', views.CardDetailView.as_view(), name='card-detail')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += [
    url(r'^course/create/$', views.CourseCreate.as_view(), name='course_create'),
    url(r'^user/create/$', views.UserCreate.as_view(), name='user_create'),
]