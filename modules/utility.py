from gluon import current
from gluon.html import *

def get_all_wh():
	db = current.db
	records = db().select(db.wh.ALL)
	return records