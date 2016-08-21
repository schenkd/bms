from app import db, models

admin_role = models.Role(name='Administrator')
mod_role = models.Role(name='Moderator')
user_role = models.Role(name='User')

db.session.add_all([admin_role, mod_role, user_role])
db.session.commit()
