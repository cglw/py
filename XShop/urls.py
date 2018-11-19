"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
# from django.contrib import admin
import xadmin
from XShop.settings import MEDIA_ROOT
from django.views.static import serve
from goods.views import GoodsListViewSet, CategoryViewset, HotSearchsViewset, BannerViewset
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from users.views import SmsCodeViewset, UserViewset

router = DefaultRouter()

router.register(r'goods', GoodsListViewSet)
router.register(r'categorys', CategoryViewset, base_name="categorys")
router.register(r'hotsearchs', HotSearchsViewset, base_name="hotsearchs")

router.register(r'codes', SmsCodeViewset, base_name="codes")
router.register(r'users', UserViewset, base_name="users")

# 轮播图url
router.register(r'banners', BannerViewset, base_name="banners")
goods_list = GoodsListViewSet.as_view({
    'get': 'list',
})


from django.contrib import admin

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'docs/', include_docs_urls(title="xshop")),

    # drf自带的token认证模式
    url(r'^api-token-auth/', views.obtain_auth_token),
    # jwt的token认证模式
    url(r'^login/', obtain_jwt_token),

]
