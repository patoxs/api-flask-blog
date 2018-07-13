from playhouse.shortcuts import model_to_dict, dict_to_model

def user():
	user = model_to_dict(current_identity)
	return user