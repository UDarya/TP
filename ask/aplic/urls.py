from django.conf import settings
from django.conf.urls import include,patterns, url
from aplic import views

urlpatterns = patterns('',
	url(r'login', views.login, name="login"),
	url(r'signup', views.signup, name="signup"),
	url(r'sort', views.sort, name="sort"),
	url(r'answer/(?P<q_id>\d+)', views.answer, name="answer"),
	#rl(r'^(?P<question_id>\\d+)/$', views.answer, name='answer'),
	url(r'^$', views.index),	
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )