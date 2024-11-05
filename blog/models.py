# from django.db import models


# #게시글 
# class Post(models.Model):
#     #FK(Foregin Key 외래키)
    
#     category = models.ForeignKey('Category', blank=True, null=True, on_delete=models.SET_NULL) ## 1대 관계에서 다 쪽에 부여해주는 속성 (FK,NT,BT,SN)
#     ## 'Category' class Category 가 밑에 있어서 불러올수가 없음 문자열로 지정하여 순서와 상관없이 불러올수 있도록 함
#     tags = models.ManyToManyField('Tag', blank=True)

#     title = models.CharField('TITLE', max_length=50) ## titme(변수이름)= models.CharField('TITLE', max_length=50)()
#     description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple one-line text.') ##blank=True (빈칸 허용) help_text='simple one-line text'(설명을 간략하게 추가)
#     image = models.ImageField('IMAGE', upload_to='blog/%Y/%m/', blank=True,null=True) ## upload_to='blog/%Y/%m/'(이미지 저장 위치)
#     content = models.TextField('CONTENT')## (NN)
#     create_date = models.DateTimeField('CREATE DT', auto_now_add=True) # auto_now_add=True 게시글 작성시 값(시간) 하나를 넣음(DT,NN,ANA)
#     update_date = models.DateTimeField('UPDATE DT', auto_now=True) # auto_now=True 게시물 업데이트 시 지금 시간으로 계속해서 업데이트(DT,NN,AN)
#     like = models.PositiveIntegerField('LIKE', default=0) ##(int)


#     def __str__(self):
#         return self.title #객체를 생성하면 해당 타이틀을 지정해줌
# # 게시글의 종류를 지정
# class Category(models.Model):
#     name = models.CharField(max_length=100, unique=True) ## unique=True(pk 로 가지고 있는 id 값이 다르더라도 같은 이름이 들어올수 없음)
#     description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple one-line text.')

#     def __str__(self):
#         return self.name
    
# # 게시글의 태그(해시태그)
# class Tag(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name
# # 댓글
# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True) 
#     content = models.TextField('CONTENT')
#     create_date = models.DateTimeField('CREATE DT', auto_now_add=True)
#     update_date = models.DateTimeField('UPDATE DE',auto_now=True)

#     @property
#     def short_content(self):
#         return self.content [:10]
    
#     def __str__(self):
#         return self.short_content
# # Create your models here.



from django.db import models

class Post(models.Model):
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)
    tags = models.ManyToManyField('Tag', blank=True)
    
    title = models.CharField('TITLE', max_length=50)
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple one-line text.')
    image = models.ImageField('IMAGE', upload_to='blog/%Y/%m/', blank=True, null=True)
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DT', auto_now_add=True)
    update_dt = models.DateTimeField('UPDATE DT', auto_now=True)
    like = models.PositiveSmallIntegerField('LIKE', default=0)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple one-line text.')

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DT', auto_now_add=True)
    update_dt = models.DateTimeField('UPDATE DT', auto_now=True)

    @property
    def short_content(self):
        return self.content[:10]

    def __str__(self):
        return self.short_content
