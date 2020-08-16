# Category_classification
 Vietnamese news classification based on their category

 

group similar category from different news, change category to general category<br/>
all category in list become category[0]
```
[['thế giới', 'thế giới đó đây'],
['thời sự', 'trong nước'],
['thể thao', 'bóng đá trong nước', 'bóng đá quốc tế', 'bóng đá việt nam', 'tin chuyển nhượng', 'các môn khác', 'ngoại hạng anh'],
['sức khỏe', 'sức khoẻ 24h', 'ung thư', 'tình yêu - giới tính'],
['kinh tế', 'kinh doanh', 'tài chính - kinh doanh', 'thị trường', 'tài chính', 'đầu tư', 'doanh nhân'],
['văn hóa - giải trí', 'giải trí', 'thế giới sao', 'thời trang', 'game', 'nhạc', 'phim', 'văn hóa'],
['xã hội', 'chính trị', 'pháp luật', 'ký sự pháp đình', 'hồ sơ vụ án', 'an toàn giao thông'],
['nhịp sống trẻ', 'giới trẻ', 'gương mặt trẻ'],
['giáo dục', 'giáo dục - khuyến học', 'tuyển sinh', 'góc phụ huynh'],
['đời sống', 'gia đình', 'tấm lòng nhân ái', 'chuyện lạ', 'tấm lòng việt'],
['công nghệ', 'sức mạnh số', 'khoa học - công nghệ', 'khoa học', 'tin công nghệ', 'sản phẩm'],
['ô tô - xe máy', 'xe'], ['cần biết', 'bạn cần biết'],
['bạn đọc', 'góc khán giả'],
['du lịch', 'khám phá'],
['truyền hình'],
['việc làm'],
['chuyển động 24h'],
['bất động sản', 'nhà đất', 'dự án']]
```


## selected category
```
159153 thế giới
156206 văn hóa - giải trí
155818 xã hội
154270 thời sự
143004 thể thao
122129 kinh tế
102888 sức khỏe
99273 giáo dục
81008 công nghệ
78659 đời sống
69820 nhịp sống trẻ
```
use under sampling for imbalance data problem, maximum number of record is 100000 or 100k
