from app import db
from models import User

#inser data
# db.session.add(User('admin', 'admin@admin.com', 'admin'))
db.session.add(User('adriana', 'adriana@adriana.com', 'adriana'))



#commit changes
db.session.commit()
