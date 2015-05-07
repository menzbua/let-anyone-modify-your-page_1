# Import Librarys

import urllib
import os

from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.datastore.datastore_query import Cursor

import webapp2
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

# Defining HTML Templates

class Handler(webapp2.RequestHandler):

  def render(self, template, **kw):
    self.write(self.render_str(template,**kw))

  def render_str(self, template, **params):
    template = jinja_env.get_template(template)
    return template.render(params)

  def write(self, *a, **kw):
    self.response.write(*a, **kw)

# Defining Comments Wall

DEFAULT_WALL = 'Comments'

def wall_key(wall_name=DEFAULT_WALL):
    return ndb.Key('Wall', wall_name)

# Defining Post Variables

class Author(ndb.Model):
    identity = ndb.StringProperty(indexed=True)
    name = ndb.StringProperty(indexed=False)
    email = ndb.StringProperty(indexed=False)

class Post(ndb.Model):
    author = ndb.StructuredProperty(Author)
    content = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)

# Defining Main Page

class MainPage(Handler):
    def get(self):
        wall_name = self.request.get('wall_name',DEFAULT_WALL)
        if wall_name == DEFAULT_WALL.lower(): wall_name = DEFAULT_WALL

        posts_to_fetch = 10
        
        cursor_url = self.request.get('continue_posts')

        arguments = {'wall_name': wall_name}

        posts_query = Post.query(ancestor = wall_key(wall_name)).order(-Post.date)

        posts, cursor, more = posts_query.fetch_page(posts_to_fetch, start_cursor =
            Cursor(urlsafe=cursor_url))
        
        if more:
            arguments['continue_posts'] = cursor.urlsafe()

        arguments['posts'] = posts

        user = 'Anonymous'
        arguments['user_name'] = user
        
        self.render('posts.html', **arguments)

# Defining Post your Comment

class PostWall(webapp2.RequestHandler):
    def post(self):

        wall_name = self.request.get('wall_name',DEFAULT_WALL)
        post = Post(parent=wall_key(wall_name))

        content = self.request.get('content')

        if type(content) != unicode:
            post.content = unicode(self.request.get('content'),'utf-8')
        else:
            post.content = self.request.get('content')

        post.put()

        query_params = {'wall_name': wall_name}
        self.redirect('/?' + urllib.urlencode(query_params))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', PostWall),
], debug=True)