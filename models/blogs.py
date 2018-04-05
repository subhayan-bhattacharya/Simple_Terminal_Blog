'''
Created on Jul 6, 2017

@author: bhatsubh
'''
from database import Database
import uuid
import datetime


class Blog:
    def __init__(self,author,title,description,detail,tags,id=None):
        self.author = author
        self.title = title
        self.desc = description
        self.detail = detail
        self.tags = tags.split(',')
        self.date = str(datetime.datetime.utcnow())
        self.id = uuid.uuid4().hex if id is None else id
        
    @staticmethod
    def create_blog(author,title,desc,detail,tags):
        blog = Blog(author=author,title=title,description=desc,detail=detail,tags=tags)
        get_json = Blog.create_json(author=blog.author, title=blog.title, desc=blog.desc, detail=blog.detail, tags=blog.tags, id=blog.id,date=blog.date)
        Database.insert(collection="blogs", data=get_json)
        
    @classmethod
    def create_json(cls,author,title,desc,detail,tags,id,date):
        return{
            'id' : id,
            'author' : author,
            'title' : title,
            'desc' : desc,
            'details' : detail,
            'tags' : tags,
            'date' : date
            }
    @staticmethod
    def display_blogs():
        blogs = Database.find(collection="blogs", query={})
        if len(blogs) > 0:
            for blog in blogs:
                print ("=======================")
                print ("Blog author:",blog['author'])
                print ("Blog title:",blog['title'])
                print ("Blog id:",blog['id'])
                print ("=======================")
            return True
        else:
            print ("No blogs to display as of now!")
            return False
        
            
    @staticmethod
    def display_blog_detail(blog_id):
        blog = Database.find_one(collection="blogs", query={'id' : blog_id})
        if blog is not None:
            print ("=======================")
            print ("Blog detail:",blog['details'])
            print ("Blog author:",blog['author'])
            return True
        else:
            return False
        
    @staticmethod
    def post_comment_toblog(id,comment,user):
        comment_json = Blog._get_comment_json(comment=comment,user=user)
        update_query = {'$push' : {'comments' : comment_json }}
        blog_filter = {'id' : id}
        Database.update(collection="blogs",filter=blog_filter,query=update_query)
        
    @classmethod
    def _get_comment_json(cls,comment,user):
        return {
            'commenter' : user.username,
            'email' : user.email,
            'comment' : comment
            }
        
    