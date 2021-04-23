from instant_work_lib.models.employ_model import employs

# imagine that we have real DB and search index.

def get_employees_by_zone_id(zone_id):
	return [employ for employ in employs.values() if employ['zone_id'] == zone_id]
