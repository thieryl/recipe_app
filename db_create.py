# instance/db_create.py

from project import db
from project.models import Recipe, User

# Create the database and the database tables
db.drop_all()
db.create_all()

# insert recipe data
recipe1 = Recipe('Slow-Cooker Tacos',
                 'Delicious ground beef that has been simmering in taco seasoning and sauce.  Perfect with hard-shelled tortillas!')
recipe2 = Recipe('Hamburgers', 'Classic dish elivated with pretzel buns.')
recipe3 = Recipe('Mediterranean Chicken',
                 'Grilled chicken served with pitas, hummus, and sauted vegetables.')
recipe4 = Recipe('Mauritian Chicken',
                 'Grilled chicken served with pitas, hummus, and sauted vegetables.')
db.session.add(recipe1)
db.session.add(recipe2)
db.session.add(recipe3)
db.session.add(recipe4)
# commit the changes
db.session.commit()


user2 = User('thiery.louison@gmails.com', '123456')
db.session.add(user2)
db.session.commit()
