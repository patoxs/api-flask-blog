from peewee import *
from models.model import Taxonomy
from playhouse.shortcuts import model_to_dict, dict_to_model

class TaxonomyModel:
	def __init__(self, **kwargs):
		self.description = kwargs['description']
		self.parent = kwargs['parent']
		self.status = kwargs['status']
		self.taxonomy = kwargs['taxonomy']

	def save_to_db(self):
		response = Taxonomy.select().where(Taxonomy.taxonomy == self.taxonomy)
		
		if response.count() > 0:
			return {"message": "Error taxonomy already exists"}, 500
		else:

			try:
				Taxonomy.create(
					description = self.description,
					parent = self.parent,
					status = self.status,
					taxonomy = self.taxonomy
				)
				return {
					"message": "Create the taxonomy"
					}, 201
			except:
				return {"message": "Error ocurred creating the taxonomy"}, 500

	@classmethod
	def return_id_taxonomy(self, taxonomy):
		tax = Taxonomy.select().where(Taxonomy.taxonomy == taxonomy).get()
		t = model_to_dict(tax)
		return t['id']
		

