from django.conf.urls import url
from . import views


urlpatterns = [
    url('^login/$', views.login),  # 用户登录视图
    url('^login_check/$', views.login_check),  # 用户登录验证

    url('^register/$', views.register),  # 用户注册视图
    # url('^register_handle/$', views.register_handle),  # 处理用户注册信息
    url('^register_check/$', views.check_user_exist),  # 验证用户名是否存在

    url('^goods/$', views.home_list_page),  # 首页首页商品信息

    url('^$', views.user),  # 个人信息页

    url('^order$', views.order),  # 用户订单页面

    url('^goods/(\d+)/', views.goods_detail),  # 商品详情页

    url('^cart/$', views.cart_show),  # 购物车页显示

    url('^list/$', views.goods_list),  # 商品列表页

    url('^address/$', views.address),  # 用户地址页面

]

