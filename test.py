from mongoengine import *

connect('db',host='localhost',port=27017)

class post(Document):
    name=StringField()
    published=BooleanField()

    @queryset_manager
    def retrive(self,queryset):
        return queryset.filter(published=True)
post1 =post(name="monya",published=True)
post1.save()
post1.name='meme'
post1.save()
print post.retrive()