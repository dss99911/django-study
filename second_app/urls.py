from django.urls import path

from . import views

# for {% url %} template tag to recognize namespace
app_name = 'second_app'

urlpatterns = [
    path('', views.index, name='index'),

    # ex: /second_app/5/
    # the 'name' value as called by the {% url %} template tag
    path('<int:question_id>/', views.detail, name='detail'),

    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/results/', views.results, name='results'),

    #https://docs.djangoproject.com/en/3.1/intro/tutorial04/#use-generic-views-less-code-is-better
    path('generic', views.IndexView.as_view(), name='generic_index'),
    path('generic/<int:pk>/', views.DetailView.as_view(), name='generic_detail'),
    path('generic/noname/<int:pk>/', views.DetailViewWithoutTemplateName.as_view(), name='generic_detail_without_template_name'),
]