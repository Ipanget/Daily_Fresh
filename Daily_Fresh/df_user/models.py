from django.db import models
from db.base_model import BaseModel

# Create your models here.


class AccountInfoManger(models.Manager):
    """ 账户模型管理器类 """
    def add_one_passport(self, username, password, email):
        """添加用户注册信息"""
        # 1.获取self所在模型类
        models_class = self.model
        # 2.创建model_class模型类对象
        obj = models_class(username=username, password=password, email=email)
        # 3.保存进数据库
        obj.save()
        return obj

    def get_one_passport(self, username, password=None):
        """用户和密码校验"""
        if password is None:
            # 校验用户名是否重名
            obj = self.filter(username=username).exists()
            return obj
        else:
            # 登录校验
            obj = self.filter(username=username, password=password).exists()
            return obj


class AccountInfo(BaseModel):
    """ 账户模型类 """
    username = models.CharField(max_length=20, verbose_name='用户名')
    password = models.CharField(max_length=40, verbose_name='密码')
    email = models.EmailField(max_length=20, verbose_name='邮箱')

    objects = AccountInfoManger()

    class Meta:
        db_table = 's_user_account'  # 指定表名
