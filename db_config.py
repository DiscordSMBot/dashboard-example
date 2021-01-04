from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'freedbtech_lucastohmeh'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Luckeycr7'
app.config['MYSQL_DATABASE_DB'] = 'freedbtech_simplebots'
app.config['MYSQL_DATABASE_HOST'] = 'freedb.tech'
mysql.init_app(app)