# -*- coding: utf-8 -*-
#
# imagine that we have real DB and search index.

from instant_work_lib.models.category_model import Category
from instant_work_lib.models.zone_model import Zone

class WEEKDAY(object):
	MONDAY = 1
	TUESDAY = 2
	WEDNESDAY = 3
	THURSDAY = 4
	FRIDAY = 5
	SATURDAY = 6
	SUNDAY = 7

class BUOI(object):
	MORNING = 1
	NOON = 2
	EVENING = 3

employs = {
	1: {
		"id": 1,
		"name": "Cuong Nguyen Van",
		"avatar": "https://cdn.24h.com.vn/upload/1-2019/images/2019-02-11/1549854510-667-muon-tron-nghia-vu-quan-su-chang-trai-han-quoc-tuc-toc--toi-thai-lan-chuyen-gioi-4-1549851755-width640height853.jpg",
		"category_ids": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
		"gender": "m",
		"age": 21,
		"price": 720000,
		"zone_id": Zone.P5,
		"lat": 10.781,
		"lng": 106.673,
		"is_active": True,
		"reviews": [
			{
				"rank": 1,
				"comment": "lam do qua",
			},
			{
				"rank": 2,
				"comment": "thiếu trách nhiệm trong công việc.",
			}
		]
	},
	2: {
		"id": 2,
		"name": "Duc Minh Tran",
		"avatar": "https://media.techz.vn/media2019/source/aaaLinh/tran-duc-bo-1.jpg",
		"description": "",
		"category_ids": [Category.SUA_NUOC],
		"gender": "m",
		"age": 23,
		"price": 200000,
		"zone_id": Zone.P5,
		"lat": 10.781,
		"lng": 106.673,
		"is_active": True,
		"week_days": [(WEEKDAY.MONDAY, BUOI.NOON),(WEEKDAY.WEDNESDAY, BUOI.MORNING),(WEEKDAY.FRIDAY, BUOI.MORNING)],
		"reviews": [
			{
				"rank": 1,
				"comment": "vui ve",
			}
		]
	},
	3: {
		"id": 3,
		"name": "Mai Huu Nhan",
		"avatar": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRvXjz5EU3KM38nnG4_3EcEUKFtq_pgTbk7ew&usqp=CAU",
		"category_ids": [Category.MASSAGE],
		"gender": "m",
		"age": 19,
		"price": 120000,
		"zone_id": Zone.P5,
		"lat": 10.781,
		"lng": 106.673,
		"is_active": True,
		"week_days": [(WEEKDAY.MONDAY, BUOI.MORNING),(WEEKDAY.WEDNESDAY, BUOI.MORNING),(WEEKDAY.FRIDAY, BUOI.MORNING)],
		"reviews": [
			{
				"rank": 1,
				"comment": "lam rat tot",
			}
		]
	},
	4: {
		"id": 4,
		"name": "Tran Van Duy",
		"avatar": "https://i.doanhnhansaigon.vn/2019/10/13/vin4447-1570967950_750x0.jpg",
		"category_ids": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
		"gender": "m",
		"age": 30,
		"price": 32000,
		"zone_id": Zone.P5,
		"lat": 10.781,
		"lng": 106.673,
		"is_active": True,
		"week_days": [(WEEKDAY.MONDAY, BUOI.MORNING),(WEEKDAY.WEDNESDAY, BUOI.MORNING),(WEEKDAY.FRIDAY, BUOI.MORNING)],
		"reviews": [],
	},
	5: {
		"id": 5,
		"name": "Tran Duc Bo",
		"avatar": "https://biggroup.vn/wp-content/uploads/2018/11/Doanh-nhan-Vo-Phi-Nhat-Huy-Toi-chia-se-kinh-nghiem-de-cung-moi-nguoi-thanh-cong-trong-BdS-doanh-nhan-1-1528273330-757-width600height544.jpg",
		"category_ids": [Category.NAU_AN],
		"gender": "m",
		"age": 31,
		"price": 30100,
		"zone_id": Zone.P5,
		"lat": 10.781,
		"lng": 106.673,
		"is_active": False,
		"week_days": [(WEEKDAY.WEDNESDAY, BUOI.EVENING), (WEEKDAY.THURSDAY, BUOI.NOON), (WEEKDAY.SUNDAY, BUOI.MORNING)],
		"reviews": [],
	},
	6: {
		"id": 6,
		"name": "Nguyen Thi Hong",
		"avatar": "https://vcdn-ngoisao.vnecdn.net/2019/02/03/2-8472-1549155527.jpg",
		"category_ids": [Category.NAU_AN],
		"gender": "f",
		"age": 25,
		"price": 32000,
		"zone_id": Zone.P5,
		"lat": 10.781,
		"lng": 106.673,
		"is_active": True,
		"week_days": [(WEEKDAY.MONDAY, BUOI.EVENING), (WEEKDAY.THURSDAY, BUOI.NOON), (WEEKDAY.SUNDAY, BUOI.MORNING)],
		"reviews": [],
	},
	7: {
		"id": 7,
		"name": "Tran Van Dan",
		"avatar": "https://images.kienthuc.net.vn/zoom/800/uploaded/trucchinh2/2020_01_16/son16-1/newfolder/anh-thoi-chua-noi-tieng-cua-den-vau-jack-va-son-tung.jpg",
		"category_ids": [Category.BOC_VAC],
		"gender": "m",
		"age": 25,
		"price": 39000,
		"zone_id": Zone.P5,
		"lat": 10.781,
		"lng": 106.673,
		"is_active": True,
		"week_days": [(WEEKDAY.MONDAY, BUOI.EVENING), (WEEKDAY.THURSDAY, BUOI.NOON), (WEEKDAY.SUNDAY, BUOI.MORNING)],
		"reviews": [],
	},
	8: {
		"id": 8,
		"name": "Nguyen Thi Hong Tuyen",
		"avatar": "https://icdn.dantri.com.vn/thumb_w/640/2017/2-doanh-nhan-bui-thanh-huyen-so-huu-phong-cach-sang-tring-trong-trang-suc-kim-cuong-1509334874928.jpg",
		"category_ids": [Category.SUA_CHUA_DO_DIEN_TU],
		"gender": "f",
		"age": 25,
		"price": 31000,
		"zone_id": Zone.P5,
		"lat": 10.781,
		"lng": 106.673,
		"is_active": True,
		"week_days": [(WEEKDAY.MONDAY, BUOI.EVENING), (WEEKDAY.THURSDAY, BUOI.NOON), (WEEKDAY.SUNDAY, BUOI.MORNING)],
		"reviews": [],
	},
	9: {
		"id": 9,
		"name": "Nguyen Thi Hong Tuyen",
		"avatar": "https://vnu.edu.vn/upload/2018/12/23326/image/Hua%20Thanh%20Hoa.jpg",
		"category_ids": [Category.PHUC_VU],
		"gender": "f",
		"age": 27,
		"price": 32000,
		"zone_id": Zone.P5,
		"lat": 10.781,
		"lng": 106.673,
		"is_active": False,
		"week_days": [(WEEKDAY.MONDAY, BUOI.EVENING), (WEEKDAY.THURSDAY, BUOI.NOON), (WEEKDAY.SUNDAY, BUOI.MORNING)],
		"reviews": [],
	},
	10: {
		"id": 10,
		"name": "Nguyen Thanh Mai",
		"avatar": "https://vcdn-vnexpress.vnecdn.net/2019/08/05/nguyen-nhat-minh-4-1565000013-6424-1565001528_1200x0.png?w=0&h=0&q=100&dpr=2&fit=crop&s=aDOXPgd-frOWLErKy3IKXg",
		"category_ids": [Category.CAI_WIN_DAO],
		"gender": "f",
		"age": 21,
		"price": 32000,
		"zone_id": Zone.P5,
		"lat": 10.781,
		"lng": 106.673,
		"is_active": True,
		"week_days": [(WEEKDAY.MONDAY, BUOI.EVENING), (WEEKDAY.THURSDAY, BUOI.NOON), (WEEKDAY.SUNDAY, BUOI.MORNING)],
		"reviews": [],
	},
	11: {
		"id": 11,
		"name": "Phan Thanh Nam",
		"avatar": "https://media.laodong.vn/Storage/NewsPortal/2020/5/14/805324/GS-Phan-Thanh-Nam-33.jpg?w=720&crop=auto&scale=both",
		"category_ids": [Category.SUA_DIEN],
		"gender": "m",
		"age": 21,
		"price": 31000,
		"zone_id": Zone.P5,
		"lat": 10.781,
		"lng": 106.673,
		"is_active": True,
		"week_days": [(WEEKDAY.MONDAY, BUOI.EVENING), (WEEKDAY.THURSDAY, BUOI.NOON), (WEEKDAY.SUNDAY, BUOI.MORNING)],
		"reviews": [],
	},
}