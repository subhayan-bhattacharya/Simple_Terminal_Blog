'''
Created on Jul 6, 2017

@author: bhatsubh
'''
from models import authors
from models import blogs
import getpass
from database import Database
import hashlib
from models.blogs import Blog

class Menu:
    def __init__(self):
        pass
    
    @staticmethod
    def run_menu():
        have_an_account = input("Do you have an account(Y|N)!")
        if have_an_account == "Y":
            username = input("Please provide your username:")
            password = getpass.getpass("Please provide your password:")
            user = authors.Author.check_user(username=username,password=Menu.hash_pass(password))
            if user is None:
                print ("Could not login to account of user {}".format(username))
                check_account_creation = input("Do you want to create an account (Y|N)???")
                if check_account_creation == "Y":
                    Menu._prompt_for_account()
                else:
                    print ("Thank you for using the blog!")
            else:
                Menu._print_welcome_message(user)
        elif have_an_account == "N":
            Menu._prompt_for_account()
        else:
            print ("Kindly select the options Y or N only !!")
                            
    @classmethod
    def _print_welcome_message(cls,user):
        print ("Welcome {}".format(user.username))
        read_or_write = input("Do you want to read or write (R|W) blogs?")
        if read_or_write == "R":
            if blogs.Blog.display_blogs():
                blog_id = input("Please enter the id of the blog that you want to read more about:")
                if not blogs.Blog.display_blog_detail(blog_id=blog_id):
                    print ("Id entered is wrong!")
                else:
                    to_comment = input("Do you want to comment something in this blog (Y|N)")
                    if to_comment == "Y":
                        comment = input("Please enter your comment:\n")
                        blogs.Blog.post_comment_toblog(id=blog_id,comment=comment,user=user)
                    else:
                        print ("Thank you for blogging!")
        elif read_or_write == "W":
            blogname = input("Please enter the name of the blog:")
            blogdesc = input("Please enter the blog description:")
            blogbody = input("Please enter the blog body:\n")
            blogtags = input("Please enter the tags associated with this blog separated by commas(,): ")
            blogs.Blog.create_blog(author=user.username, title=blogname, desc=blogdesc, detail=blogbody, tags=blogtags)
        else:
            print ("Thank you for blogging!")
        
    @classmethod
    def _prompt_for_account(cls):
        user = None
        while user is None:
            username = input("Please enter your username:")
            if authors.Author.check_username(username=username):
                print ("Username {} already exists ...please choose a different one !")
            else:
                password = getpass.getpass("Please enter your password:")
                email = input("Please enter your email address:")
                user = authors.Author.create_user(username=username, email=email, password=Menu.hash_pass(password))
        Menu._print_welcome_message(user)
                
    @classmethod
    def hash_pass(cls,password):
        hash_password = hashlib.sha1(password.encode('utf-8')).digest()
        hash_password = hashlib.sha1(hash_password).hexdigest()
        hash_password = '*' + hash_password.upper()
        return hash_password
    
    
    