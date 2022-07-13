from polls.models import Blog
from django.db import connection
import redis
rd = redis.Redis(host = '0.0.0.0', port = 6379, db = 0)

class BlogAdapter(object):

    def add_blog(self, id, user_id, title, image_url, description):
        Blog.objects.update_or_create(id = id, user_id=user_id, title= title, image_url = image_url, description=description, defaults = {"id": id})
        return True 
    def update_blog(self, id, user_id, title, image_url, description):
        Blog.objects.filter(id = id).update(user_id=user_id, title=title, image_url=image_url, description=description)

    def get_blog(self):
        response = Blog.objects.all()
        print(response)
        return response
    def recommend_blog(self):
        query = """ 
        select id, 
        user_id, 
        title, 
        image_url, 
        description 
        from blog
        where id != 0
        and id != 1
        order by title
        """
        with connection.cursor() as cursor:
            cursor.execute(query)
            row = cursor.fetchall()
        response = []
        for (id, user_id, title, image_url, description) in row:
            data = {'user_id': user_id, 'title': title, 'image_url': image_url, 'description': description}
            response.append(data)
        return response



