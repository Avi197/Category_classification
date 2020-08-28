import jsonlines
import re
import file_path

Dantri_infile = file_path.Dantri_g_category
Thanhnien_infile = file_path.Thanhnien_g_category
Tuoitre_infile = file_path.Tuoitre_g_category
Vnexpress_infile = file_path.Vnexpress_g_category
Vnn_infile = file_path.Vnn_g_category
Vtv_infile = file_path.Vtv_g_category


Dantri_out = file_path.Dantri_g_category_text
Thanhnien_out = file_path.Thanhnien_g_category_text
Tuoitre_out = file_path.Tuoitre_g_category_text
Vnexpress_out = file_path.Vnexpress_g_category_text
Vnn_out = file_path.Vnn_g_category_text
Vtv_out = file_path.Vtv_g_category_text


list_list = ['thế giới', 'văn hóa - giải trí', 'xã hội', 'thời sự', 'thể thao', 'kinh tế', 'sức khỏe', 'giáo dục',
             'công nghệ', 'đời sống', 'nhịp sống trẻ']

max_records = 100000


def get_category(file):
    with jsonlines.open(file) as infile:
        for obj in infile:
            category = obj['category']
            # with open(f'{location}{category}', 'a', encoding='utf-8') as outfile:
            for li in list_list:
                if category == li:
                    outfile = open(f'{location}{category}', 'a', encoding='utf-8')
                    if len(obj['title']) > 20:
                        label = re.sub(r' ', '-', category)
                        outfile.write(f'__label__{label} ')
                        outfile.write(f'{obj["title"]} ')
                        outfile.write('\n')


location = "H:/Vietnamese word representations/Category_classification_data/generalize_category/individual_category/"
file_in = "H:/Vietnamese word representations/Category_classification_data/generalize_category/g_category_json/_g_category.json"
file_out = "H:/Vietnamese word representations/Category_classification_data/generalize_category/_g_category.txt"

get_category(file_in)

