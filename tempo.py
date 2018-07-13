class Student(Resource):

	@jwt_required()
	def get(self, name):
		return {'student': name}

	def post(self, name):
		data = request.get_json()
		item = {'name':name, 'price': data['price']}
		return item, 201