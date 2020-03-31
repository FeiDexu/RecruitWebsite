
import datetime

from django.db import models

# Create your models here.


def time_detail():
    return datetime.date.today() + datetime.timedelta(days=1)


class User(models.Model):
    """用户模型"""
    # 用户id
    userid = models.AutoField(primary_key=True, verbose_name='编号')
    # 用户名
    username = models.CharField(unique=True, max_length=20, verbose_name='用户名')
    # 用户密码（数据库中保存密码的MD5摘要，登录时比较输入密码的摘要与数据中保存的是否一致）
    password = models.CharField(max_length=32, verbose_name='密码')
    # 用户真实姓名
    realname = models.CharField(max_length=20, default='', null=True, verbose_name='真实姓名')
    # 性别
    sex = models.BooleanField(default=True, null=True, verbose_name='性别')
    # 生日
    birth = models.DateTimeField(auto_now_add=True, null=True, verbose_name='生日')
    # 用户介绍
    intro = models.CharField(max_length=256, default='', verbose_name='用户介绍')
    # 手机号
    tel = models.CharField(unique=True, max_length=20, verbose_name='手机号')
    # 邮箱
    email = models.CharField(unique=True, max_length=255, default='', verbose_name='邮箱')
    # 注册时间
    regdate = models.DateTimeField(auto_now_add=True, verbose_name='注册时间')
    # 用户积分
    point = models.IntegerField(default=0, verbose_name='积分')
    # 是否网站会员
    ismember = models.BooleanField(default=False, verbose_name='是否会员')
    # 最近登录时间
    lastvisit = models.DateTimeField(auto_now_add=True, verbose_name='最近登录')

    class Meta:
        db_table = 'tb_user'
        verbose_name = '用户表'
        verbose_name_plural = '用户表'


class District(models.Model):
    """地区"""
    # 地区id
    distid = models.AutoField(primary_key=True, verbose_name='编号')
    # 父级行政区（省级行政区的父级为None）
    parent = models.ForeignKey('self', on_delete=models.DO_NOTHING, db_column='pid', default='', verbose_name='父级行政区', null=True)
    # 地区名字
    name = models.CharField(max_length=255, verbose_name='名字')
    # 该地区是否热门城市
    ishot = models.BooleanField(default=False, verbose_name='是否热门城市', null=True)
    # 地区介绍
    intro = models.CharField(max_length=255, default='', verbose_name='介绍', null=True)

    class Meta:
        db_table = 'tb_district'
        verbose_name = '地区表'
        verbose_name_plural = '地区表'

    def to_dict(self,):
        return {
            'distid': self.distid,
            'parentid': self.parent,
            'name': self.name,
            'ishot': self.ishot,
            'intro': self.intro,
        }


class Boss(models.Model):
    """boss表"""
    bossid = models.AutoField(primary_key=True, verbose_name='编号')
    # 公司id
    company = models.ForeignKey(to='Company', on_delete=models.DO_NOTHING, db_column='companyid', verbose_name='公司')
    # 老板姓名
    bossname = models.CharField(max_length=255, verbose_name='老板')
    # 老板介绍
    intro = models.CharField(max_length=255, default='', null=True, verbose_name='介绍')

    class Meta:
        db_table = 'tb_boss'
        verbose_name = 'boss表'
        verbose_name_plural = 'boss表'


class Recruiter(models.Model):
    """招聘人"""
    # 招聘人id
    recruiterid = models.AutoField(primary_key=True, verbose_name='编号')
    # 招聘人名字
    name = models.CharField(max_length=255, verbose_name='名字')
    tel = models.CharField(max_length=20, verbose_name='联系方式')
    # 服务评价
    servstar = models.IntegerField(default=0, verbose_name='评价')
    # 介绍
    intro = models.CharField(max_length=255, default='', null=True, verbose_name='介绍')
    # 招聘人负责的招聘职位
    recruit = models.ForeignKey(to='RecruiterRecruit', on_delete=models.DO_NOTHING, db_column='recruitid', related_name='+', null=True, verbose_name='负责职位')
    # 所属公司
    company = models.ForeignKey(to='Company', on_delete=models.DO_NOTHING, db_column='companyid', verbose_name='公司')

    class Meta:
        db_table = 'tb_recruiter'
        verbose_name = '招聘人表'
        verbose_name_plural = '招聘人表'


class Company(models.Model):
    """公司"""
    # 公司id
    companyid = models.AutoField(primary_key=True, verbose_name='编号')
    # 所属行政区域
    distinct = models.ForeignKey(to='District', on_delete=models.DO_NOTHING, db_column='distid', verbose_name='行政区')
    # 公司名字
    name = models.CharField(max_length=255, verbose_name='名字')
    # 成员数量
    member = models.IntegerField(default=1, verbose_name='成员数量')
    # 热度
    hot = models.IntegerField(default=0, null=True, verbose_name='热度')
    # 公司介绍
    intro = models.CharField(max_length=511, default='', null=True, verbose_name='介绍')
    # 上市情况
    market = models.CharField(max_length=256, default='', null=True, verbose_name='经营情况')
    # 公司图片（图片上传到阿里云oss，数据库只保存地址）
    mainphoto = models.CharField(max_length=255, default='', null=True, verbose_name='图片')

    class Meta:
        db_table = 'tb_company'
        verbose_name = '公司'
        verbose_name_plural = '公司'


class RecruiterCompany(models.Model):
    """招聘人公司中间实体"""
    id = models.AutoField(primary_key=True, verbose_name='编号')
    # 招聘人id
    recruiter = models.ForeignKey(to=Recruiter, on_delete=models.DO_NOTHING, db_column='recruiterid', verbose_name='招聘人')
    # 公司id
    company = models.ForeignKey(to=Company, on_delete=models.DO_NOTHING, db_column='companyid', verbose_name='公司')

    class Meta:
        db_table = 'tb_recruiter_company'
        unique_together = (('recruiter', 'company'),)
        verbose_name = '招聘人公司表'
        verbose_name_plural = '招聘人公司表'


class BossCompany(models.Model):
    """boss公司中间实体"""
    id = models.AutoField(primary_key=True, verbose_name='编号')
    # 招聘人id
    boss = models.ForeignKey(to=Boss, on_delete=models.DO_NOTHING, db_column='bossid', verbose_name='boss')
    # 公司id
    company = models.ForeignKey(to=Company, on_delete=models.DO_NOTHING, db_column='compayid', verbose_name='公司')

    class Meta:
        db_table = 'tb_boss_company'
        unique_together = (('boss', 'company'),)
        verbose_name = 'boss-公司表'
        verbose_name_plural = 'boss-公司表'


class CompanyPhoto(models.Model):
    """公司图片"""
    # 图片id
    photoid = models.AutoField(primary_key=True, verbose_name='编号')
    # 图片对应的公司
    company = models.ForeignKey(to=Company, on_delete=models.DO_NOTHING, db_column='companyid', verbose_name='公司')
    # 图片资源路径
    path = models.CharField(max_length=255, default='', null=True, verbose_name='图片')

    class Meta:
        db_table = 'tb_company_photo'
        verbose_name = '公司图片'
        verbose_name_plural = '公司图片'


class Tag(models.Model):
    """职位标签"""
    # 标签id
    tagid = models.AutoField(primary_key=True, verbose_name='序号')
    # 标签内容
    content = models.CharField(max_length=20, default='', null=True, verbose_name='标签')

    class Meta:
        db_table = 'tb_tag'
        verbose_name = '职位标签'
        verbose_name_plural = '职位标签'


class LoginLog(models.Model):
    """登录日志"""
    # 日志ID
    logid = models.BigAutoField(primary_key=True, verbose_name='序号')
    # 登录的用户
    user = models.ForeignKey(to=User, on_delete=models.DO_NOTHING, db_column='userid', verbose_name='用户')
    # 登录的IP地址
    ipaddr = models.CharField(max_length=255, verbose_name='ip地址')
    # 登录的日期
    logdate = models.DateTimeField(auto_now_add=True, verbose_name='登录日期')
    # 登录的设备编码
    devcode = models.CharField(max_length=255, default='', verbose_name='设备编码')

    class Meta:
        db_table = 'tb_login_log'
        verbose_name = '登录日志'
        verbose_name_plural = '登录日志'


class Privilege(models.Model):
    """权限"""
    # 权限id
    privid = models.AutoField(primary_key=True, verbose_name='序号')
    # 权限对应的方式
    method = models.CharField(max_length=15, default='', null=True, verbose_name='方式')
    # 权限对应的url
    url = models.CharField(max_length=1024, default='', null=True, verbose_name='对应url')
    # 权限描述
    detail = models.CharField(max_length=255, default='', null=True, verbose_name='描述')

    class Meta:
        db_table = 'tb_privilege'
        verbose_name = '权限管理'
        verbose_name_plural = '权限管理'


class RecruitType(models.Model):
    """职位所属类型"""
    # 类型id
    typeid = models.AutoField(primary_key=True, verbose_name='编号')
    # 类型名
    name = models.CharField(max_length=255, default='', null=True, verbose_name='类型')

    class Meta:
        db_table = 'tb_recruit_type'
        verbose_name = '职位类型'
        verbose_name_plural = '职位类型'


class Recruit(models.Model):
    """职位信息"""
    # 职位id
    recruitid = models.AutoField(primary_key=True, verbose_name='序号')
    # 职位名字
    name = models.CharField(max_length=50, verbose_name='名字')
    # 招聘数量
    number = models.IntegerField(default=1, verbose_name='招聘数量')
    # 最低薪水
    min_salary = models.IntegerField(default=0, null=True, verbose_name='最低薪水')
    # 最高薪水
    max_salary = models.IntegerField(default=0, null=True, verbose_name='最高薪水')
    # 职位详情
    detail = models.CharField(max_length=511, default='', null=True, verbose_name='职位详情')
    # 职位发布日期
    pubdate = models.DateField(auto_now_add=True, null=True, verbose_name='发布日期')
    # 办公地址
    street = models.CharField(max_length=255, default='', null=True, verbose_name='办公地址')
    # 地铁交通情况
    hassubway = models.IntegerField(default=False, null=True, verbose_name='交通情况')
    # 职位类型
    type = models.ForeignKey(to=RecruitType, on_delete=models.DO_NOTHING, db_column='typeid', verbose_name='职位类型')
    # 职位所属二级行政区
    distinct_level2 = models.ForeignKey(to=District, null=True, on_delete=models.DO_NOTHING, db_column='distid2', related_name='+', verbose_name='二级行政区')
    # 职位所属三级行政区
    distinct_level3 = models.ForeignKey(to=District, null=True, on_delete=models.DO_NOTHING, db_column='distid3', related_name='+', verbose_name='三级行政区')
    # 职位所属公司
    company = models.ForeignKey(to=Company, on_delete=models.DO_NOTHING, db_column='companyid', verbose_name='公司')
    # 老板
    boss = models.ForeignKey(to=Boss, default='', null=True, on_delete=models.DO_NOTHING, db_column='bossid', verbose_name='老板')
    # 招聘发布者
    recruiter = models.ForeignKey('RecruiterRecruit', models.DO_NOTHING, db_column='recruiterid', related_name='+', verbose_name='招聘人')

    class Meta:
        db_table = 'tb_recruit'
        verbose_name = '职位信息'
        verbose_name_plural = '职位信息'


class RecruiterRecruit(models.Model):
    """招聘人职位中间实体"""
    recruiter_recruit_id = models.AutoField(primary_key=True, verbose_name='序号')
    # 招聘人
    recruiter = models.ForeignKey(to=Recruiter, null=True, on_delete=models.DO_NOTHING, db_column='recruiterid', verbose_name='招聘人')
    # 职位
    recruit = models.ForeignKey(to=Recruit, null=True, on_delete=models.DO_NOTHING, db_column='recruitid', verbose_name='职位')

    class Meta:
        db_table = 'tb_recruiter_recruit'
        unique_together = (('recruiter', 'recruit'),)
        verbose_name = '招聘人负责职位'
        verbose_name_plural = '招聘人负责职位'


class Record(models.Model):
    """浏览记录表"""
    # 浏览id
    recordid = models.BigAutoField(primary_key=True, verbose_name='序号')
    # 用户
    user = models.ForeignKey(to=User, null=True, on_delete=models.DO_NOTHING, db_column='userid', verbose_name='用户')
    # 职位
    recruit = models.ForeignKey(to=Recruit, on_delete=models.DO_NOTHING, db_column='recruitid', verbose_name='职位')
    # 浏览时间
    recorddate = models.DateTimeField(auto_now_add=True, verbose_name='浏览时间')

    class Meta:
        db_table = 'tb_record'
        unique_together = (('user', 'recruit'),)
        verbose_name = '浏览记录'
        verbose_name_plural = '浏览记录'


class Apply(models.Model):
    """职位申请记录表"""
    # 浏览id
    applyid = models.BigAutoField(primary_key=True, verbose_name='浏览序号')
    # 用户id
    user = models.ForeignKey(to=User, null=True, on_delete=models.DO_NOTHING, db_column='userid', verbose_name='用户')
    # 职位id
    recruit = models.ForeignKey(to=Recruit, null=True, on_delete=models.DO_NOTHING, db_column='recruitid', verbose_name='职位')
    # 添加收藏时间
    addtime = models.DateTimeField(auto_now_add=True, verbose_name='添加收藏时间')

    class Meta:
        db_table = 'tb_apply'
        unique_together = (('user', 'recruit'),)
        verbose_name = '用户收藏'
        verbose_name_plural = '用户收藏'


class RecruitTag(models.Model):
    """职位标签中间表"""
    # id
    recruit_tag_id = models.AutoField(primary_key=True, verbose_name='序号')
    # 职位id
    recruit = models.ForeignKey(to=Recruit, null=True, on_delete=models.DO_NOTHING, db_column='recruitid', verbose_name='职位')
    # 标签id
    tag = models.ForeignKey(to=Tag, null=True, on_delete=models.DO_NOTHING, db_column='tagid', verbose_name='标签')

    class Meta:
        db_table = 'tb_recruit_tag'
        unique_together = (('recruit', 'tag'),)
        verbose_name = '职位对应的标签'
        verbose_name_plural = '职位对应的标签'


class Role(models.Model):
    """角色表"""
    # 角色id
    roleid = models.AutoField(primary_key=True, verbose_name='角色id')
    # 角色名
    rolename = models.CharField(max_length=255, null=True, verbose_name='角色名')
    # 角色对应的权限
    privs = models.ManyToManyField(to=Privilege, through='RolePrivilege', default=0, verbose_name='对应权限')

    class Meta:
        db_table = 'tb_role'
        verbose_name = '角色'
        verbose_name_plural = '角色'


# class UserRecruit(models.Model):
#     """角色表"""
#     # 角色id
#     roleid = models.AutoField(primary_key=True)
#     # 角色名
#     rolename = models.CharField(max_length=255)
#     # 角色对应的权限
#     privs = models.ManyToManyField(to=Privilege, through='RolePrivilege')
#
#     class Meta:
#         managed = False
#         db_table = 'tb_role'


class RolePrivilege(models.Model):
    """角色权限中间实体"""
    # 角色权限id
    role_priv_id = models.AutoField(primary_key=True, verbose_name='序号')
    # 角色
    role = models.ForeignKey(to=Role, null=True, on_delete=models.DO_NOTHING, db_column='roleid', verbose_name='角色')
    # 权限
    priv= models.ForeignKey(to=Privilege, null=True, on_delete=models.DO_NOTHING, db_column='privid', verbose_name='权限')

    class Meta:
        db_table = 'tb_role_privilege'
        unique_together = (('role', 'priv'),)
        verbose_name = '角色权限'
        verbose_name_plural = '角色权限'


class UserRole(models.Model):
    """用户角色中间实体"""
    # 用户角色id
    user_role_id = models.AutoField(primary_key=True, verbose_name='序号')
    # 用户
    user = models.ForeignKey(to=User, on_delete=models.DO_NOTHING, db_column='userid', verbose_name='用户id')
    # 角色
    role = models.ForeignKey(to=Role, null=True, on_delete=models.DO_NOTHING, db_column='roleid', verbose_name='角色id')

    class Meta:
        db_table = 'tb_user_role'
        unique_together = (('user', 'role'),)
        verbose_name = '用户角色'
        verbose_name_plural = '用户角色'
