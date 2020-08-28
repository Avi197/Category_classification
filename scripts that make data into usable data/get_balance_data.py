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


# def get_category(file, out):
#     with jsonlines.open(file) as infile:
#         with open(out, 'w', encoding='utf-8') as outfile:
#             count_line = 1
#             for li in list_list:
#                 print('check point 1')
#
#                 count = 1
#                 for obj in infile:
#                     print('check point 2')
#                     category = obj['category']
#                     if count <= max_records:
#                         if category == li:
#                             label = re.sub(r' ', '-', category)
#                             outfile.write(f'__label__{label} ')
#                             outfile.write(f'{obj["title"]} ')
#                             outfile.write('\n')
#                             count += 1


def get_category(file, out):
    with jsonlines.open(file) as infile:
        with open(out, 'w', encoding='utf-8') as outfile:
            count_line = 1
            for obj in infile:
                category = obj['category']
                for li in list_list:
                    count = 1
                    if count <= max_records:
                        if category == li:
                            if len(obj['title']) > 20:
                                label = re.sub(r' ', '-', category)
                                outfile.write(f'__label__{label} ')
                                outfile.write(f'{obj["title"]} ')
                                outfile.write('\n')
                                count += 1
                    # with open(left_over_data, 'w', encoding='utf-8') as left_over:
                    #     if category == li:
                    #         if len(obj['title']) > 20:
                    #             label = re.sub(r' ', '-', category)
                    #             left_over.write(f'__label__{label} ')
                    #             left_over.write(f'{obj["title"]} ')
                    #             left_over.write('\n')


left_over_data = "H:/Vietnamese word representations/Category_classification_data/generalize_category/left_over_data.txt"

# get_category(Dantri_infile, Dantri_out, 'category')
# get_category(Thanhnien_infile, Thanhnien_out, 'cate')
# get_category(Tuoitre_infile, Tuoitre_out, 'cate')
# get_category(Vnn_infile, Vnn_out, 'catename')
file_in = "H:/Vietnamese word representations/Category_classification_data/generalize_category/g_category_json/_g_category.json"
file_out = "H:/Vietnamese word representations/Category_classification_data/generalize_category/_g_category.txt"

get_category(file_in, file_out)

