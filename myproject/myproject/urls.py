from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^$', 'acortar.views.pagina'),
    url(r'^(\d)+$', 'acortar.views.redirigirUrl'),
    url(r'.*' , 'acortar.views.notFound'),

)
