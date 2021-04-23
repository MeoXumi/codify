from django.contrib.gis.geos import Point, Polygon

from instant_work_lib.models.zone_model import LOCATION_ZONE, RESTRICT_ZONE

map_lat_to_zone = {}
map_lng_to_zone = {}
map_lat_to_restrict_zone = {}
map_lng_to_restrict_zone = {}
POSITION_UP_RATE = 100

def refresh_model():
	for zone_id, coords in LOCATION_ZONE.iteritems():
		min_lat = min([i[1] for i in coords]) * POSITION_UP_RATE
		max_lat = max([i[1] for i in coords]) * POSITION_UP_RATE

		for i in range(int(min_lat), int(max_lat) + 1):
			map_lat_to_zone.setdefault(i, []).append(zone_id)

		min_lng = min([i[0] for i in coords]) * POSITION_UP_RATE
		max_lng = max([i[0] for i in coords]) * POSITION_UP_RATE

		for i in range(int(min_lng), int(max_lng) + 1):
			map_lng_to_zone.setdefault(i, []).append(zone_id)


	for zone_id, coords in RESTRICT_ZONE.iteritems():
		min_lat = min([i[1] for i in coords]) * POSITION_UP_RATE
		max_lat = max([i[1] for i in coords]) * POSITION_UP_RATE

		for i in range(int(min_lat), int(max_lat) + 1):
			map_lat_to_restrict_zone.setdefault(i, []).append(zone_id)

		min_lng = min([i[0] for i in coords]) * POSITION_UP_RATE
		max_lng = max([i[0] for i in coords]) * POSITION_UP_RATE

		for i in range(int(min_lng), int(max_lng) + 1):
			map_lng_to_restrict_zone.setdefault(i, []).append(zone_id)

	print (map_lat_to_zone)
refresh_model()


def get_zone_id_by_lat_lng(lat, lng):
	print ("map_lat_to_zone=", map_lat_to_zone)
	zone_ids = set(map_lat_to_zone.get(int(lat * POSITION_UP_RATE), [])) & set(map_lng_to_zone.get(int(lng * POSITION_UP_RATE), []))
	for zone_id in zone_ids:
		if Polygon(LOCATION_ZONE[zone_id]).contains(Point(x=lng, y=lat)):
			return zone_id
	return None

def is_in_restrict_zone(lat, lng):
	zone_ids = set(map_lat_to_restrict_zone.get(int(lat * POSITION_UP_RATE), [])) & set(map_lng_to_restrict_zone.get(int(lng * POSITION_UP_RATE), []))
	for zone_id in zone_ids:
		if Polygon(LOCATION_ZONE[zone_id]).contains(Point(x=lng, y=lat)):
			return True
	return False
