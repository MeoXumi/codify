import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from instant_work_lib.managers import zone_manager
from instant_work_lib.managers.employ_manager import get_employees_by_zone_id
from instant_work_lib.managers.job_manager import create_job, get_jobs_by_create_uid, get_jobs_by_zone_id, set_apply_job
from instant_work_lib.managers.zone_manager import get_zone_id_by_lat_lng, is_in_restrict_zone
from instant_work_lib.models.employ_model import employs

@csrf_exempt
def get_employee(request):
	data = json.loads(request.body)
	return HttpResponse(json.dumps(employs[data['uid']]))

@csrf_exempt
def get_employees(request):
	data = json.loads(request.body)
	lat = data['lat']
	lng = data['lng']

	zone_id = zone_manager.get_zone_id_by_lat_lng(lat, lng)
	if not zone_id:
		return HttpResponse(json.dumps({"employees": []}))

	employees = get_employees_by_zone_id(zone_id)
	results = []
	for employee in employees:
		if is_in_restrict_zone(employee['lat'], employee['lng']):
			continue
		if not(set(data['category_ids']) & set(employee['category_ids'])):
			continue
		if 'gender' in data and employee['gender'] != data['gender']:
			continue
		if 'min_price' in data and employee['price'] > data['min_price']:
			continue
		if 'max_price' in data and employee['price'] < data['min_price']:
			continue
		results.append(employee)

	return HttpResponse(json.dumps(results))


@csrf_exempt
def get_onwer_jobs(request):
	data = json.loads(request.body)
	uid = data['uid']
	jobs = get_jobs_by_create_uid(uid)
	return HttpResponse(json.dumps(jobs))


@csrf_exempt
def get_jobs(request):
	data = json.loads(request.body)
	uid = data['uid']
	user = employs[uid]

	jobs = get_jobs_by_zone_id(user['zone_id'])
	jobs = [job for job in jobs if set(job['category_ids']) & set(user['category_ids'])]
	jobs = [job for job in jobs if job['create_uid'] != uid]
	return HttpResponse(json.dumps(jobs))


@csrf_exempt
def apply_job(request):
	data = json.loads(request.body)
	set_apply_job(data['uid'], data['job_id'])
	return HttpResponse(json.dumps({}))


@csrf_exempt
def submit_job(request):
	data = json.loads(request.body)
	employ = employs[data['create_uid']]
	create_job(zone_id=employ['zone_id'], **data)
	return HttpResponse(json.dumps({}))
