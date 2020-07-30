import jsonlines
import os
import file_path
import time
import re
from vncorenlp import VnCoreNLP
from unidecode import unidecode

Dantri_infile = file_path.Dantri
Thanhnien_infile = file_path.Thanhnien
Tuoitre_infile = file_path.Tuoitre
Vnexpress_infile = file_path.Vnexpress
Vnn_infile = file_path.Vnn
Vtv_infile = file_path.Vtv

Dantri_not_token = file_path.Dantri_not_token
Thanhnien_not_token = file_path.Thanhnien_not_token
Tuoitre_not_token = file_path.Tuoitre_not_token
Vnexpress_not_token = file_path.Vnexpress_not_token
Vnn_not_token = file_path.Vnn_not_token
Vtv_not_token = file_path.Vtv_not_token
# cate

file_list = [Dantri_not_token, Thanhnien_not_token, Tuoitre_not_token, Vnexpress_not_token, Vnn_not_token,
             Vtv_not_token]
for f in file_list:
    filename = os.path.dirname(f)
    if not os.path.exists(filename):
        os.makedirs(filename)


def get_data_tokenized(file, out):
    count_line = 1
    with VnCoreNLP(address='http://127.0.0.1', port=9000) as vncorenlp:
        with jsonlines.open(file) as infile:
            with open(out, 'w') as outfile:
                for obj in infile:
                    category = obj['category']
                    category = category.strip()
                    for _ in range(5):
                        try:
                            tag = vncorenlp.tokenize(tag)
                            break
                        except:
                            print("retry")
                            time.sleep(5)
                    label = ' '.join(category)
                    label = re.sub(r' ', '-', label)
                    outfile.write(f'__label__{label} ')
                    for _ in range(5):
                        try:
                            word_seg = vncorenlp.tokenize(obj['title'])
                            break
                        except:
                            print('retry')
                            time.sleep(5)
                    if len(word_seg) > 1:
                        lis = []
                        for l in word_seg:
                            li = ' '.join(l)
                            lis.append(li)
                    seg = ' '.join(lis)
                    outfile.write(f'{seg} ')
                    outfile.write('\n')
                    print('done line {0}'.format(count_line))
                    count_line += 1
                print(f'wrote to {out}')


# if category == ''
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
             ['bất động sản', 'nhà đất', 'dự án'], ['tiêu dùng']]


# nhớ thêm bỏ tiếng anh cho vnn
def get_data_not_tokenized(file, out, category_field_name_of_each_news):
    count_line = 1
    with jsonlines.open(file) as infile:
        with open(out, 'w', encoding='utf-8') as outfile:
            for obj in infile:
                category = obj[f'{category_field_name_of_each_news}']

                category = category.lower()

                # check for category and convert to general category

                # if any(category in sl for sl in list_list):
                for l in list_list:
                    if category in l:
                        category = l[0]
                # category = unidecode(category)

                label = re.sub(r' ', '-', category)
                outfile.write(f'__label__{label} ')
                # seg = ' '.join(obj['title'])
                outfile.write(f'{obj["title"]} ')
                outfile.write('\n')
                print('done line {0}'.format(count_line))
                count_line += 1
            print(f'wrote to {out}')


# get_data_dantri(Dantri_infile)

# get_data_not_tokenized(Dantri_infile, Dantri_not_token, 'category')
# get_data_not_tokenized(Thanhnien_infile, Thanhnien_not_token, 'cate')
# get_data_not_tokenized(Tuoitre_infile, Tuoitre_not_token, 'cate')
# get_data_not_tokenized(Vnn_infile, Vnn_not_token, 'catename')
get_data_not_tokenized(Vtv_infile, Vtv_not_token, 'cate')

# vnn has category as a list
# get_data_not_tokenized(Vnexpress_infile, Vnexpress_not_token, 'cate')

# Dantri - category
# Thanhnien - cate
# Tuoitre - cate
# Vnexpress - cate
# Vnn - catename
# Vtv - cate
