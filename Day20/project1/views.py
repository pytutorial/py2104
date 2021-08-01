from django.shortcuts import HttpResponse

#127.0.0.1:8000 
def index(request):
    return HttpResponse('Hello')

#127.0.0.1:8000/page-2
def page2(request):
    return HttpResponse('Page-2')

texts = [
    'Đất nền tại các tỉnh phía Bắc bắt đầu được quan tâm từ cuối 2016, tuy nhiên, đến đầu năm 2018 thì thị trường thực sự phát triển mạnh mẽ. Thời điểm này xuất hiện hiện tượng sốt đất tại một số các tỉnh như Thái Nguyên, Bắc Giang, Bắc Ninh, Hưng Yên, Vĩnh Phúc, Quảng Ninh,...',
    'Phiên giao dịch hôm nay 25/7, giá USD được các ngân hàng điều chỉnh giảm mạnh sau 2 ngày tăng liên tục; tuy nhiên, giá trên thị trường chợ đen vẫn neo ở mức cao.',
    'Trong số 12 dự án yếu kém của ngành công thương, nhà máy giấy Phương Nam bán 3 lần chưa được, tổ chức đấu giá nhiều lần nhưng không ai tham gia. Trong khi đó, nhà máy xơ sợi Đình Vũ đã có lãi và đủ điều kiện để “vinh dự” đưa ra khỏi danh sách yếu kém.',
    'Việc sở hữu ngôi nhà thứ hai đang là xu hướng “cực thịnh” trong giới doanh nhân và người thành đạt. Bên cạnh việc sở hữu riêng cho mình một chốn nghỉ dưỡng thảnh thơi, cao cấp sau những bộn bề công việc, ngôi nhà thứ hai còn là món đầu tư khôn ngoan, mang lại giá trị lâu dài.',
    'Chào năm học mới, đồng hành cùng các du học sinh và các bậc phụ huynh, Maritime Bank triển khai chương trình “Chuyển tiền quốc tế, điện phí 0 đồng”* miễn điện phí cho các giao dịch chuyển tiền tại quầy qua SWIFT(Hiệp hội viễn thông tài chính liên Ngân hàng quốc tế) từ nay đến hết 29/9/2018.',
    'Từ tháng 5, phân khúc đất nền đang có dấu hiệu chững lại sau cơn “sốt” kéo dài gần 1 năm qua. Trong khi đó, giá căn hộ tại thị trường TPHCM vẫn tăng đều đặn mỗi năm.',
    'Masan Group đạt doanh thu thuần 9.184 tỷ đồng trong quý II/2018, tăng trưởng 11% so với quý I với 8.274 tỷ đồng. Trong đó, lĩnh vực thực phẩm -đồ uống, chế biến sâu khoáng sản và đóng góp của Techcombank đều đạt đăng trưởng hai chữ số.',
    'Đội cứu nạn gồm 10 bác sỹ, y sỹ, y tá với đầy đủ thuốc men và thiết bị của Hoàng Anh Gia Lai cùng 50 tấn gạo, 100.000 gói mì tôm, 5 tấn cá khô, 2.000 bộ quần áo, 100 túi bảo quản tử thi sẽ được vận chuyển sang Lào vào chiều nay.'
]