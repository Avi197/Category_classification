import jsonlines
import file_path

Dantri_infile = file_path.Dantri
Thanhnien_infile = file_path.Thanhnien
Tuoitre_infile = file_path.Tuoitre
Vnexpress_infile = file_path.Vnexpress
Vnn_infile = file_path.Vnn
Vtv_infile = file_path.Vtv

Dantri_category = file_path.Dantri_g_category
# category
# title
Thanhnien_category = file_path.Thanhnien_g_category
# cate
Tuoitre_category = file_path.Tuoitre_g_category
# cate
Vnexpress_category = file_path.Vnexpress_g_category
# cate
Vnn_category = file_path.Vnn_g_category
# catename
Vtv_category = file_path.Vtv_g_category
# cate
list_list = [['thế giới', 'thế giới đó đây'], ['thời sự', 'trong nước'],
             ['thể thao', 'bóng đá trong nước', 'bóng đá quốc tế', 'bóng đá việt nam', 'tin chuyển nhượng',
              'các môn khác', 'ngoại hạng anh'], ['sức khỏe', 'sức khoẻ 24h', 'ung thư', 'tình yêu - giới tính'],
             ['kinh tế', 'kinh doanh', 'tài chính - kinh doanh', 'thị trường', 'tài chính', 'đầu tư', 'doanh nhân'],
             ['văn hóa - giải trí', 'giải trí', 'thế giới sao', 'thời trang', 'game', 'nhạc', 'phim', 'văn hóa'],
             ['xã hội', 'chính trị', 'pháp luật', 'ký sự pháp đình', 'hồ sơ vụ án', 'an toàn giao thông'],
             ['nhịp sống trẻ', 'giới trẻ', 'gương mặt trẻ'],
             ['giáo dục', 'giáo dục - khuyến học', 'tuyển sinh', 'góc phụ huynh'],
             ['đời sống', 'gia đình', 'tấm lòng nhân ái', 'chuyện lạ', 'tấm lòng việt'],
             ['công nghệ', 'sức mạnh số', 'khoa học - công nghệ', 'khoa học', 'tin công nghệ', 'sản phẩm'],
             ['ô tô - xe máy', 'xe'], ['cần biết', 'bạn cần biết'], ['bạn đọc', 'góc khán giả'],
             ['du lịch', 'khám phá'], ['truyền hình'], ['việc làm'], ['chuyển động 24h'],
             ['bất động sản', 'nhà đất', 'dự án']]


def get_category(file, out, category_field_name_of_each_news):
    with jsonlines.open(file) as infile:
        with jsonlines.open(out, 'w') as outfile:
            for obj in infile:
                new_obj = {}
                category = obj[f'{category_field_name_of_each_news}']
                category = category.lower()
                if any(category in sl for sl in list_list):
                    for li in list_list:
                        if category in li:
                            category = li[0]
                            new_obj['category'] = category
                            new_obj['title'] = obj['title'].replace('\u2028', '').strip()
                            outfile.write(new_obj)


get_category(Dantri_infile, Dantri_category, 'category')
get_category(Thanhnien_infile, Thanhnien_category, 'cate')
get_category(Tuoitre_infile, Tuoitre_category, 'cate')
get_category(Vnn_infile, Vnn_category, 'catename')
get_category(Vtv_infile, Vtv_category, 'cate')

