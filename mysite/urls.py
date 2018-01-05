from django.conf.urls import include, url ,patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'polls/',include('polls.urls',namespace='polls')),
    url(r'^admin/', include(admin.site.urls)),

    
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
               
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 


