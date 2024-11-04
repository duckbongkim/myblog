# from django.contrib import admin
# from django.db.models.query import QuerySet
# from django.http.request import HttpRequest
# from .models import Post,Category,Tag,Comment

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('id','category','tag_list','title','description','image','create_date','update_date','like')

#     def tag_list(self, obj):
#         return ','.join([t.name for t in obj.tags.all()]) ## tag 가 한줄로 보일수 있도록 해줌 (한줄표현식)

#     def get_queryset(self, request):
#         return super().get_queryset(request).prefetch_related('tags') ## 데이터를 미리 꺼내놓음
    
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display=('id','name','description')

# @admin.register(Tag)
# class TagAdmin(admin.ModelAdmin):
#     list_display=('id','name')

# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display=('id','post','short_content','create_date','update_date')


from django.contrib import admin
from blog.models import Post, Category, Tag, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'tag_list', 'title', 'description', 'image', 'create_dt', 'update_dt', 'like')

    def tag_list(self, obj):
        return ','.join([t.name for t in obj.tags.all()])

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'short_content', 'create_dt', 'update_dt')

    


    