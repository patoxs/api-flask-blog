from models.model import Post, PostTaxonomy, Taxonomy
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

class PostModel:
	def __init__(self, **kwargs):
		self.title = kwargs['title']
		self.excerpt = kwargs['excerpt']
		self.content = kwargs['content']
		self.datetime = kwargs['datetime']
		self.status = kwargs['status']
		self.ping = kwargs['ping']
		self.password = kwargs['password']
		self.url = kwargs['url']
		self.modified = kwargs['modified']
		self.parent = kwargs['parent']
		self.post_order = kwargs['post_order']
		self.id_person = kwargs['id_person']

	def save_to_db(self):
		news = Post.select().where(Post.title == self.title).get()
		p = model_to_dict(news)
		if len(p) == 0:
			try:
				p = Post(
					title = self.title,
					excerpt = self.excerpt,
					content = self.content,
					datetime = self.datetime,
					status = self.status,
					ping = self.ping,
					password = self.password,
					url = self.url,
					modified = self.modified,
					parent = self.parent,
					post_order = self.post_order,
					id_person = self.id_person
				)
				p.save()
				return p.id
			except:
				return {"message": "Error ocurred creating the item"}, 500

		else:
			try:
				query = Post.update(
					excerpt = self.excerpt,
					content = self.content,
					status = self.status,
					ping = self.ping,
					password = self.password,
					modified = self.modified,
					parent = self.parent,
					post_order = self.post_order,
					id_person = self.id_person
				).where(Post.title == self.title)
				
				return p['id']
			except:
				return {"message": "Error ocurred update the item"}, 500


			


	@classmethod
	def find_by_url(self, url):
		query = Post.select(
			Post.id,
			Post.title,
			Post.excerpt,
			Post.content,
			Post.url,
			Post.datetime			
			).where(Post.url == url).dicts()
		return query
		#return query._data

	@classmethod
	def return_post_all(self, quantity):
		query = Post.select().join(PostTaxonomy).join(Taxonomy).order_by(Post.title).limit(quantity).dicts()
		return query

	@classmethod
	def return_post_by_taxonomy(self, taxonomy, quantity):
		query = Post.select(
			Post.title,
			Post.excerpt,
			Post.datetime,
			Taxonomy.taxonomy,
			Post.url
			).join(PostTaxonomy).join(Taxonomy).where( Taxonomy.taxonomy == taxonomy ).order_by(Post.title).limit(quantity).dicts()
		return query

	@classmethod
	def find_taxonomy_by_idtaxonomy(self, id_post):
		query = Taxonomy.select(
			Taxonomy.id,
			Taxonomy.taxonomy
			).join(PostTaxonomy).where(PostTaxonomy.id_post == id_post).dicts()
		return query