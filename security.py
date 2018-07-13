from werkzeug.security import safe_str_cmp
from resources.auth import ResourceAuth

def authenticate(username,password):
	person = ResourceAuth.find_by_name(username)
	if person and safe_str_cmp(person.password, password):
		return person

def identity(payload):
	person_id = payload['identity']
	return ResourceAuth.find_by_id(person_id)