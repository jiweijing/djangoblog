from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = 'django运维系统'
    site_title = 'django 学习'
    index_title = '首页'


custom_site = CustomSite(name='cus_admin')
