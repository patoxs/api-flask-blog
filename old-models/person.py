from models.model import Person
from peewee import *

class PersonModel:
	def __init__(self, **kwargs):
		self.email = kwargs['email']
		self.id_person_type = kwargs['id_person_type']
		self.image = kwargs['image']
		self.key_activate = kwargs['key_activate']
		self.login = kwargs['login']
		self.nicename = kwargs['nicename']
		self.password = kwargs['password']
		self.status = kwargs['status']

	def save_to_db(self):
		response = Person.select().where(Person.email == self.email)
		
		if response.count() > 0:

			try:
				query = Person.update(
					image = self.image,
					key_activate = self.key_activate,
					login = self.login,
					nicename = self.nicename,
					password = self.password,
					status = self.status
				).where(Person.email == self.email)
				query.execute()
				return {"message": "Update the person"}, 201
			except:
				return {"message": "Error ocurred update the person"}, 500

		else:

			try:
				Person.create(
					email = self.email,
					id_person_type = self.id_person_type,
					image = self.image,
					key_activate = self.key_activate,
					login = self.login,
					nicename = self.nicename,
					password = self.password,
					status = self.status
				)
				return {
					"message": "Create the person",
					"path": self.nicename
					}, 201
			except:
				return {"message": "Error ocurred creating the person"}, 500


		

