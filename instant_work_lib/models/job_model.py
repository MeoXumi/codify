# -*- coding: utf-8 -*-
#
from instant_work_lib.models.category_model import Category
from instant_work_lib.models.zone_model import Zone

# imagine that we have real DB and search index.

jobs = {
	1: {
		"id": 1,
		"price": 3000000,
		"image": "https://www.healthline.com/hlcmsresource/images/topic_centers/1200x628_FACEBOOK_benefits-of-hot-stone-massage.jpg",
		"description": "Có sử dụng thêm dầu dưỡng massage hoặc tinh dầu massage vừa để bôi trơn vừa giúp da dẻ mịn màng, căng bóng hơn. Trên thị trường có khá nhiều loại dầu massage body các bạn có thể lựa chọn theo sở thích như dầu dừa, dầu oliu, dầu quả bơ, dầu jojoba, …hoặc tùy theo nhu cầu của khách hàng nhé.",
		"category_ids": [Category.MASSAGE],
		"zone_id": Zone.P5,
		"lat": 10.781,
		"lng": 106.673,
		"apply_uids": [3, 6, 7, 8, 9],
		"phone": "0876412381",
		"address": "123 Quán Hai Đắc, Đường Lê Văn Sỹ, Phường 1, Tan Binh, Ho Chi Minh City",
		"create_uid": 1
	},
	2: {
		"id": 2,
		"price": 300000,
		"image": "https://cdn.daynauan.info.vn/wp-content/uploads/2019/05/hoc-nau-an-chuyen-nghiep-tai-tphcm.jpg",
		"description": "Người đầu bếp chuyên nghiệp phải nắm rõ kỹ thuật về chế biến món ăn, giữ dao luôn sắc bén, áp dụng đúng quy chuẩn an toàn thực phẩm, cách nêm nếm điều chỉnh gia vị, kỹ năng vận hành quản lí bếp… Tất cả bạn sẽ tìm thấy ở những khóa học chuyên sâu về nghề bếp được giảng dạy bởi các chuyên gia hàng đầu.",
		"category_ids": [Category.NAU_AN],
		"zone_id": Zone.P5,
		"lat": 10.783,
		"lng": 106.676,
		"apply_uids": [4, 5, 8, 10, 11],
		"phone": "0375412581",
		"address": "20 Nam Kỳ Khởi Nghĩa, Quận 1, Ho Chi Minh City",
		"create_uid": 1
	},
	3: {
		"id": 3,
		"price": 300000,
		"image": "https://image-us.eva.vn/upload/2-2019/images/2019-06-30/nhung-cach-nau-an-gay-ung-thu-nhieu-nguoi-viet-dang-lam-hang-ngay-1-1561867340-639-width600height360.jpg",
		"description": "Nhu cầu thưởng thức ẩm thực luôn phát triển không ngừng đòi hỏi người đầu bếp phải sáng tạo và bắp kịp trào lưu nấu ăn hiện đại. Biết lắng nghe để chấp nhận phản hồi từ khách hàng. Hãy học hỏi và tìm kiếm cơ hội làm việc với những người đầu bếp giỏi bởi kiến thức là vô hạn.",
		"category_ids": [Category.NAU_AN],
		"zone_id": Zone.P5,
		"lat": 10.778,
		"lng": 106.674,
		"apply_uids": [3, 4],
		"phone": "0175412521",
		"address": "30 Đường Lê Lợi, Bến Nghé, District 1, Ho Chi Minh City",
		"create_uid": 1
	},
	4: {
		"id": 4,
		"image": "https://cdn.cet.edu.vn/wp-content/uploads/2019/06/noi-niem-chi-co-nguoi-lam-phuc-vu-moi-hieu.jpg",
		"price": 300100,
		"description": "Làm sao để chăm sóc khách hàng thật “ân cần, chu đáo” là điều mà nhân viên phục nào cũng cần phải lưu tâm. Kỹ năng chăm sóc khách hàng thể hiện ở việc giúp khách kéo ghế ngồi vào bàn; giúp khách treo áo khoác lên vị trí thích hợp; hỏi han khách có cần hài lòng về bữa ăn và có yêu cầu thêm gì không…",
		"category_ids": [Category.PHUC_VU],
		"zone_id": Zone.P5,
		"lat": 10.785,
		"lng": 106.670,
		"apply_uids": [4],
		"phone": "0475412521",
		"address": "Cách Mạng Tháng 8, Quận 3, Ho Chi Minh City",
		"create_uid": 1
	},
	5: {
		"id": 5,
		"price": 120000,
		"image": "https://diennuochoangha.com/wp-content/uploads/2015/11/tho-sua-chua-dien-nuoc-tai-bien-hoa.jpg",
		"description": "Sở hữu đội ngũ kỹ thuật viên chuyên sâu; đội ngũ kỹ sư giỏi, tay nghề cao, Phúc Thịnh luôn có mặt nhanh chóng, kịp thời để hỗ trợ khắc phục các sự cố điện nước, mang đến sự hài lòng đến cho quý khách hàng.",
		"category_ids": [Category.SUA_DIEN],
		"zone_id": Zone.P5,
		"lat": 10.787,
		"lng": 106.679,
		"apply_uids": [3, 6, 7],
		"phone": "0671212121",
		"address": "123 Quán Hai Đắc, Đường Lê Văn Sỹ, Phường 1, Tan Binh, Ho Chi Minh City",
		"create_uid": 1
	},
	6: {
		"id": 6,
		"price": 540000,
		"image": "https://vietreview.vn/wp-content/uploads/2020/01/may-cat-co-cam-tay-tot-nhat-danh-gia-boi-vietreview.jpg",
		"description": "Lam co sach se tai nhà, cắt cỏ ngắn, không gây ồn cho hàng xóm.",
		"category_ids": [Category.LAM_CO],
		"zone_id": Zone.P5,
		"lat": 10.775,
		"lng": 106.665,
		"apply_uids": [],
		"phone": "0571211121",
		"address": "123 Quán Hai Đắc, Đường Lê Văn Sỹ, Phường 1, Tan Binh, Ho Chi Minh City",
		"create_uid": 1
	},
	7: {
		"id": 7,
		"price": 30000,
		"image": "https://img.grouponcdn.com/seocms/jyLP59wuLGYsny7TnJNuaqQR6RN/170958613_jpg_crop_jpeg-1080x648",
		"description": "Massage nhẹ nhàng. Bạn nên di chuyển từ vai đến eo và lưng. Bạn cần dùng lực khác nhau lên các bộ phận trên cơ thể, chẳng hạn dùng lực mạnh lên vùng lưng, chân nhưng dùng lực nhẹ hơn cho những vùng như tay, cổ, bụng... Đây là bước đầu tiên đơn giản nhất trong các cách massage cơ thể.",
		"category_ids": [Category.MASSAGE],
		"zone_id": Zone.P5,
		"lat": 10.778,
		"lng": 106.665,
		"apply_uids": [3],
		"phone": "0471211121",
		"address": "30/4 Đường Tôn Đức Thắng, District 1, Ho Chi Minh City",
		"create_uid": 1
	},
	8: {
		"id": 8,
		"price": 310000,
		"image": "https://cdn.huongnghiepaau.com/wp-content/uploads/2019/01/hoc-nau-an-chuyen-nghiep.jpg",
		"description": "ăn uống là cả một nghệ thuật, nó không chỉ nhằm đáp ứng yêu cầu cơ bản của con người mà còn có mối quan hệ mật thiết đến lối sống, truyền thống dân tộc, được thể hiện rất rõ qua những dụng cụ được dùng trong bữa ăn, cách ứng xử với mọi người trong khi ăn. Vì thế việc ăn uống còn minh chứng cho lịch sử và sự hình thành nền văn hoá của Việt Nam. Các món ăn qua từng giai đoạn nói lên được cuộc sống, con người của giai đoạn đó và của vùng đất – nơi đã sản sinh ra mỗi món ăn.",
		"category_ids": [Category.NAU_AN],
		"zone_id": Zone.P5,
		"lat": 10.772,
		"lng": 106.677,
		"apply_uids": [6],
		"phone": "0371211121",
		"address": "123 Quán Hai Đắc, Đường Lê Văn Sỹ, Phường 1, Tan Binh, Ho Chi Minh City",
		"create_uid": 2
	},
	9: {
		"id": 9,
		"price": 300000,
		"image": "https://m.media-amazon.com/images/M/MV5BOTU0ZGVmY2MtMTM1OS00YmNlLWE1NGUtMGYyMjI1MjY1NWUzXkEyXkFqcGdeQWFybm8@._V1_CR0,4,1404,790_AL_UX477_CR0,0,477,268_AL_.jpg",
		"description": "chứa yếu tố bất ngờ, châm biếm, đả kích, nhằm để phê phán xã hội hay đơn giản hơn là để gây cười. Một số dạng hài hước đơn giản như chơi chữ, hài kịch tình huống, nhại... Hài kịch lãng mạn là một thể loại phổ biến, mô tả mối tình lãng mạn đang phát triển trong điều kiện hài hước, tập trung vào những điểm yếu của những người đang yêu.",
		"category_ids": [Category.DIEN_HAI_KICH],
		"zone_id": Zone.P5,
		"lat": 10.78,
		"lng": 106.672,
		"apply_uids": [3],
		"phone": "0271211121",
		"address": "123 Quán Hai Đắc, Đường Lê Văn Sỹ, Phường 1, Tan Binh, Ho Chi Minh City",
		"create_uid": 1
	},
	10: {
		"id": 10,
		"price": 300000,
		"image": "https://static2.yan.vn/YanNews/2167221/201907/bo-anh-tuoi-thanh-xuan-cua-5-co-gai-tre-khien-cong-dong-mang-ngan-ngo-907dff2b.jpg",
		"description": "ngũ nam thanh,nữ tú đẹp trai,đẹp gái khuôn mặt ưa nhìn khi các bạn cần trong công việc hoặc vui chơi giải trí hay những lúc buồn buồn,cô đơn...vv,hiện nay chúng tôi có DỊCH VỤ cho thuê Nam Nữ - Người yêu đi chơi,đồng hành cùng quý khách hàng khi cần đi đâu đó.",
		"category_ids": [Category.DI_CHOI_CHUNG],
		"zone_id": Zone.P5,
		"lat": 10.77,
		"lng": 106.673,
		"apply_uids": [4],
		"phone": "01412143121",
		"address": "123 Quán Hai Đắc, Đường Lê Văn Sỹ, Phường 1, Tan Binh, Ho Chi Minh City",
		"create_uid": 1
	},
	11: {
		"id": 11,
		"price": 120000,
		"image": "https://cnet1.cbsistatic.com/img/tSurRnreKCkRQnRF90hR5xfkung=/756x567/2020/01/13/6e566b3e-faef-4ffd-9909-01acca997b6d/windows-10-cropped-for-promo.png",
		"description": "Có thể cài được ubuntu, macos, window XP, window 11. Cài tại nhà, dễ mến với chủ nhà.",
		"category_ids": [Category.CAI_WIN_DAO],
		"zone_id": Zone.P5,
		"lat": 10.76,
		"lng": 106.679,
		"apply_uids": [3],
		"phone": "06412143111",
		"address": "102 Đường Tôn Đức Thắng, District 1, Ho Chi Minh City",
		"create_uid": 1
	},
	12: {
		"id": 12,
		"price": 540000,
		"image": "https://travltalk.co/wp-content/uploads/2019/05/nhau-2.png",
		"description": "phải biết nhậu. Uống được càng nhiều càng tốt nhưng ngoại hình càng đẹp, càng hấp dẫn thì càng thích",
		"category_ids": [Category.NHAU_CUNG],
		"zone_id": Zone.P5,
		"lat": 10.79,
		"lng": 106.67,
		"apply_uids": [],
		"phone": "01412843111",
		"address": "123 Quán Hai Đắc, Đường Lê Văn Sỹ, Phường 1, Tan Binh, Ho Chi Minh City",
		"create_uid": 2
	},
}