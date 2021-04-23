# imagine that we have real DB and search index.

class Category(object):
	VIEC_NHA = 1
	BOC_VAC = 2
	SUA_NUOC = 3
	SUA_DIEN = 4
	PHUC_VU = 5
	NAU_AN = 6
	MASSAGE = 7
	LAM_CO = 8
	CAI_WIN_DAO = 9
	NHAU_CUNG = 10
	DIEN_HAI_KICH = 11
	SUA_CHUA_DO_DIEN_TU = 12
	DI_CHOI_CHUNG = 13

	IMAGE_MAP = {
		VIEC_NHA: "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/women-are-doing-housework-preparing-food-royalty-free-illustration-1573648745.jpg?crop=0.774xw:0.491xh;0.226xw,0.272xh&resize=1200:*",
		BOC_VAC: "https://bocxepgiaretphcm.net/wp-content/uploads/2016/05/dich-vu-boc-xep-binh-duong.jpg",
		SUA_NUOC: "https://suadiennuoc24gio.com/wp-content/uploads/2015/10/tho-sua-ong-nuoc-gia-re-quan-11.jpeg",
		SUA_DIEN: "https://lh3.googleusercontent.com/proxy/-FXMv_tdUHxQMrSXV0NFLFoA9icXk6-PTQma_qRAb1ILNLjvPGjcM3EmUoY1NfKTeD2qXWwp5nxPNGrgPixvBhjX29ELzO7OcPL2RJUZvs_ETqpd8bcDrGiOik4O_hRVWLL9l-0dNVmA6b7KkDkkXRcIZdkt2GhfzdG0p8LeVvCTeqw",
		PHUC_VU: "https://hotelcareers.vn/Uploads/images/kien-thuc-nganh-khach-san/ban-mo-ta-cong-viec-phuc-vu-ban-2.jpg",
		NAU_AN: "https://baodansinh.mediacdn.vn/zoom/480_300/Images/2018/06/18/hoc-nghe-nau-an-trinh-do-so-cap-co-viec-lam-ngay1529299588.jpg",
		MASSAGE: "https://ik.imagekit.io/tvlk/xpe-asset/dsIfD0QxFcgaDmB6sQchobk5CmBu9PzsWhwFXGFxJ179jzSxIGG5kZNhhHY-p7nw/xxt/experience/image/b24-diploma-in-massage-therapist-2-jpg-1200x720-FIT-bef285519a21ac41e1825ada9308cdb3.jpeg?_src=imagekit&tr=q-60,c-at_max,w-720,h-512",
		LAM_CO: "https://www.ketnoitieudung.vn/data/ck/images/top-10-san-pham-may-cat-co-cam-tay-gia-dinh-ban-chay-2018-1.png",
		CAI_WIN_DAO: "https://i3g4v6w8.stackpathcdn.com/wp-content/uploads/2019/01/create-partition-install-windows-10-835x574.jpg",
		NHAU_CUNG: "https://znews-photo.zadn.vn/w660/Uploaded/izhqv/2020_01_22/1577107820_6132_only_15768030311431296595185.jpg",
		DIEN_HAI_KICH: "https://tttd.ex-cdn.com/files/f1/2018/06/14/tim_duyen_chfc.jpg",
		SUA_CHUA_DO_DIEN_TU: "https://aeondelight-vietnam.com.vn/wp-content/uploads/2019/03/sua-chua-thiet-bi-dien-tu.jpg",
		DI_CHOI_CHUNG: "https://we25.vn/media2018/Img_News/2019/07/22/bo-anh-tuoi-thanh-xuan-cua-5-co-gai-tre-khien-cong-dong-mang-ngan-ngo-31ab24ff_20190722151800.jpg",
	}

