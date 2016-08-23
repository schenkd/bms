# bms
bms means blog-management-system 

In search of a content-management-system that met my needs I don't want to make a compromise. So I decide to build my own blog-management-system that correspondent with my wishes.

I'm using python/flask for my backend and bootstrap for my frontend layout. SQLAlchemy will transform your querys in every database language you want. I'm using Jinja2 as my python template engine. It's pretty cool and very easy to use for generating dynamic content in your html files.

## goals

### v1.0
- :soon: create blog post
- markdown editor with pic upload
- search engine
-  :heavy_check_mark: usermanagement (user, editor, admin)
- comments
- categories
- :soon: user profile (save posts, see comments, upload pic etc.)
- automatically generating editor team page

### future version
- automatically social media administration
- user tracking
- data visualization for editor/admin

## requirements
You will find a pip freeze in the requirements.txt

## Template
In this project I'm using the g'old bootstrap css framework. Flask has an extinsion for bootstrap called 'flask-bootstrap'. I use it for quickforms like on the 'auth/login.html' template.
