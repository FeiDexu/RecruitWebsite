from django.contrib import admin

from web.models import *
# Register your models here.


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):

    # def show_all_distinct
    list_display = ('distid', 'name', 'ishot', 'intro')
    # 设置每页最大展示
    list_per_page = 30
    # 设置检索字段
    search_fields = ('distid', 'name', 'intro')
    # 设置排序字段
    ordering = ('distid', )
    # 可以修改的字段
    list_display_links = ('name', 'ishot', 'intro')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('userid', 'username', 'password', 'realname', 'sex', 'tel', 'intro', 'email',
                    'regdate', 'point', 'ismember', 'lastvisit')
    list_per_page = 30
    # 设置排序字段
    ordering = ('userid',)
    list_display_links = ('username', 'password', 'realname', 'sex', 'tel', 'email', 'intro', 'point', 'ismember')
    search_fields = ('userid', 'username', 'relaname', 'tel', 'intro', 'email')


@admin.register(Recruiter)
class RecruiterAdmin(admin.ModelAdmin):
    list_display = ('recruiterid', 'name', 'tel', 'servstar', 'intro', 'recruit', 'company')
    list_per_page = 30
    # 设置排序字段
    ordering = ('recruiterid',)
    list_display_links = ('name', 'tel', 'intro', 'recruit', 'company')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('companyid', 'distinct', 'name', 'member', 'hot', 'market', 'mainphoto')
    list_per_page = 30
    # 设置排序字段
    ordering = ('companyid',)
    list_display_links = ('distinct', 'name', 'member', 'hot', 'market', 'mainphoto')


@admin.register(CompanyPhoto)
class CompanyPhotoAdmin(admin.ModelAdmin):
    list_display = ('photoid', 'company', 'path')
    list_per_page = 30
    # 设置排序字段
    ordering = ('photoid',)
    list_display_links = ('company', 'path')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('tagid', 'content')
    list_per_page = 30
    # 设置排序字段
    ordering = ('tagid',)
    list_display_links = ('content', )


@admin.register(LoginLog)
class LoginLogAdmin(admin.ModelAdmin):
    list_display = ('logid', 'user', 'ipaddr', 'logdate', 'devcode')
    list_per_page = 30
    # 设置排序字段
    ordering = ('logid',)
    # list_display_links = ('distinct', 'name', 'member', 'hot', 'market', 'mainphoto')


@admin.register(Privilege)
class PrivilegeAdmin(admin.ModelAdmin):
    list_display = ('privid', 'method', 'url', 'detail', )
    list_per_page = 30
    # 设置排序字段
    ordering = ('privid',)
    list_display_links = ('method', 'url', 'detail', )


@admin.register(RecruitType)
class RecruitTypeAdmin(admin.ModelAdmin):
    list_display = ('typeid', 'name',)
    list_per_page = 30
    # 设置排序字段
    ordering = ('typeid',)
    list_display_links = ('name',)


@admin.register(Recruit)
class RecruitAdmin(admin.ModelAdmin):
    list_display = ('recruitid', 'name', 'number', 'min_salary', 'max_salary', 'detail', 'pubdate', 'street',
                    'hassubway', 'type', 'distinct_level2', 'distinct_level3', 'company', 'boss', 'recruiter')
    list_per_page = 30
    # 设置排序字段
    ordering = ('recruitid',)
    list_display_links = ('name', 'number', 'min_salary', 'max_salary', 'detail', 'pubdate', 'street',
                          'hassubway', 'type', 'distinct_level2', 'distinct_level3', 'company', 'boss', 'recruiter')


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('recordid', 'user', 'recruit', 'recorddate')
    list_per_page = 30
    # 设置排序字段
    ordering = ('recordid',)
    # list_display_links = ('distinct', 'name', 'member', 'hot', 'market', 'mainphoto')


@admin.register(Apply)
class ApplyAdmin(admin.ModelAdmin):
    list_display = ('applyid', 'user', 'recruit', 'addtime')
    list_per_page = 30
    # 设置排序字段
    ordering = ('applyid',)
    list_display_links = ('user', 'recruit', 'addtime')


@admin.register(RecruitTag)
class RecruitTagAdmin(admin.ModelAdmin):
    list_display = ('recruit_tag_id', 'recruit', 'tag',)
    list_per_page = 30
    # 设置排序字段
    ordering = ('recruit_tag_id',)
    list_display_links = ('recruit', 'tag')

#
# @admin.register(Role)
# class RoleAdmin(admin.ModelAdmin):
#     list_display = ('roleid', 'rolename', 'privs',)
#     list_per_page = 30
#     # 设置排序字段
#     ordering = ('roleid',)
    # list_display_links = ('rolename', 'privs')


@admin.register(RolePrivilege)
class RolePrivilegeAdmin(admin.ModelAdmin):
    list_display = ('role_priv_id', 'role', 'priv',)
    list_per_page = 30
    # 设置排序字段
    ordering = ('role_priv_id',)
    list_display_links = ('role', 'priv')


@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('user_role_id', 'user', 'role',)
    list_per_page = 30
    # 设置排序字段
    ordering = ('user_role_id',)
    list_display_links = ('user', 'role')


