# BMS
BMS means blog-management-system 

In search of a content-management-system that met my needs I don't want to make a compromise. So I decide to build my own blog-management-system that correspondent with my wishes.

I'm using python/flask for my backend and bootstrap for my frontend layout. SQLAlchemy will transform your querys in every database language you want. I'm using Jinja2 as my python template engine. It's pretty cool and very easy to use for generating dynamic content in your html files.

## Goals

### v1.0
- [X] :heavy_check_mark: create blog post
- [X] :heavy_check_mark: CKEditor
- [ ] search engine
- [X] :heavy_check_mark: usermanagement
  * [X] Roles (user, mod, admin)
  * [X] change pw or email
  * [X] email token after registration
- [X] :heavy_check_mark: comments
  * [X] markdown editor
  * [X] moderate comments with enable/disable
- [ ] :soon: categories
- [ ] :soon: user profile 
  * [ ] save favourite posts 
  * [ ] :soon: see your own comments
  * [ ] upload a profile pic
  * [X] see some information about the user
- [ ] automatically generating editor team page

### Future version
- automatically social media administration
- user tracking
- data visualization for editor/admin

## Requirements
- Python version 3.5.2
- You will find a pip freeze in the requirements.txt

## Quick start

### Linux / OSX

Create virtual environment
`$ virtualenv -p python3 .venv`

Activate virtual environment
`$ source .venv/bin/activate`
`(.venv) $`

Install requirements
`(.venv) $ pip install -r requirements.txt`

(Optional) Configure your E-Mail
- Open the config.py file in the root directory and change the "mail" section to your needs
- Set your username `export MAIL_USERNAME=testuser`
- Set your password `export MAIL_PASSWORD=testpassword`

Run server
`python manage.py runserver`

## Template
In this project I'm using the g'old bootstrap css framework. Flask has an extension for bootstrap called 'flask-bootstrap'. I use it for quickforms like on the 'auth/login.html' template.
