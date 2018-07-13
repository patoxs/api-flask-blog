from modelos.person import PersonModel

class ResourceAuth:
	
	@classmethod
	def find_by_name(self, name):
		return PersonModel.find_by_name(name)

	@classmethod
	def find_by_id(self, id):
		return PersonModel.find_by_id(id)
		
