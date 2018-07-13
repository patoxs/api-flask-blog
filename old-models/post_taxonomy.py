from models.model import PostTaxonomy
from peewee import *

class PostTaxonomyModel:
	def __init__(self, **kwargs):
		self.id_post = kwargs['id_post']
		self.id_taxonomy = kwargs['id_taxonomy']

	def save_to_db(self):
		print(PostTaxonomy.insert(
				id_post = self.id_post,
				id_taxonomy = self.id_taxonomy
			))
		try:

			t = PostTaxonomy.insert(
				id_post = self.id_post,
				id_taxonomy = self.id_taxonomy
			).execute()
			print(t)

			return {
				"message": "Create the taxonomy-post",
				"taxonomy": t.id_post
				}, 201
		except:
			return {"message": "Error ocurred creating the taxonomy-post"}, 500


		

