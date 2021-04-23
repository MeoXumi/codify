from instant_work_lib.models.employ_model import employs
from instant_work_lib.models.job_model import jobs

# imagine that we have real DB and search index.

def gen_job(job):
	job['apply_eployees'] = [employs[apply_uid] for apply_uid in job['apply_uids']]
	return job

def get_jobs_by_create_uid(create_uid):
	return [gen_job(job) for job in jobs.values() if create_uid == job['create_uid']]

def get_jobs_by_zone_id(zone_id):
	return [gen_job(job) for job in jobs.values() if zone_id == job['zone_id']]

def set_apply_job(uid, job_id):
	apply_uids = set(jobs[job_id]['apply_uids'])
	apply_uids.add(uid)

	jobs[job_id]['apply_uids'] = list(apply_uids)

def create_job(price, description, category_ids, address, zone_id, create_uid, lat, lng, **ignore_kwargs):
	id = len(jobs)
	jobs[id] = {
		"id": id,
		"price": price,
		"description": description,
		"category_ids": category_ids,
		"apply_uids": [],
		"address": address,
		"zone_id": zone_id,
		"create_uid": create_uid,
		"lat": lat,
		"lng": lng,
	}
