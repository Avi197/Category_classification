import os
import re
import collections
import jsonlines

import file_path

Dantri_category = file_path.Dantri_category_only
Thanhnien_category = file_path.Thanhnien_category_only
Tuoitre_category = file_path.Tuoitre_category_only
Vnexpress_category = file_path.Vnexpress_category_only
Vnn_category = file_path.Vnn_category_only
Vtv_category = file_path.Vtv_category_only
# cate

# filename = os.path.dirname(Dantri_test)
# if not os.path.exists(filename):
#     os.makedirs(filename)


# def count_label():
#     with open(cooking_label_uniq) as label_uniq:
#         with open(cooking_label) as label:
#             with open(cooking_label_count, 'w') as outfile:
#                 for line_label_uniq in label_uniq:
#                     count = 0
#                     for line_label in label:
#                         if line_label_uniq == line_label:
#                             count += 1
#                     outfile.write(f'{count} {line_label_uniq}')


def count_category(file, out):
    out = file.replace('.txt', '(only_category).txt')
    with open(file, encoding='utf-8') as infile:
        with open(out, 'w', encoding='utf-8') as outfile:
            counts = collections.Counter(l.strip() for l in infile)
            for line, count in counts.most_common():
                outfile.write(f'{count} {line}\n')


def unique_category(file, name):
    out = file.replace('.json', name)
    with open(file, encoding='utf-8') as infile:
        with open(out, 'w', encoding='utf-8') as outfile:
            counts = collections.Counter(l.strip() for l in infile)
            for line, counts in counts.most_common():
                outfile.write(f'{line}\n')

# thanhnien_count = "H:/Vietnamese word representations/Category_classification_data/category_title_raw_json/category_only/thanhnien_count.txt"
# tuoitre_count = "H:/Vietnamese word representations/Category_classification_data/category_title_raw_json/category_only/tuoitre_count.txt"
# vnexpress_count = "H:/Vietnamese word representations/Category_classification_data/category_title_raw_json/category_only/vnexpress_count.txt"
# vnn_count = "H:/Vietnamese word representations/Category_classification_data/category_title_raw_json/category_only/vnn_count.txt"
# vtv_count = "H:/Vietnamese word representations/Category_classification_data/category_title_raw_json/category_only/vtv_count.txt"

all_category = "H:/Vietnamese word representations/Category_classification_data/category_title_raw_json/category_only/category.txt"
category_count = "H:/Vietnamese word representations/Category_classification_data/category_title_raw_json/category_only/category_count.txt"
category_uniq = "H:/Vietnamese word representations/Category_classification_data/category_title_raw_json/category_only/category_uniq.txt"

# in category_only/category_only
# dantri = "H:/Vietnamese word representations/Category_classification_data/category_title_raw_json/category_only/category_only/dantri_category_only.txt"
# thanhnien = "H:/Vietnamese word representations/Category_classification_data/category_title_raw_json/category_only/category_only/thanhnien_category_only.txt"
# tuoitre = "H:/Vietnamese word representations/Category_classification_data/category_title_raw_json/category_only/category_only/tuoitre_category_only.txt"
# # vnexpress ="H:/Vietnamese word representations/Category_classification_data/category_title_raw_json/category_only/category_only/vnexpress_category_only.txt"
# vnn = "H:/Vietnamese word representations/Category_classification_data/category_title_raw_json/category_only/category_only/vnn_category_only.txt"
# vtv = "H:/Vietnamese word representations/Category_classification_data/category_title_raw_json/category_only/category_only/vtv_category_only.txt"

# in category_only
dantri = "H:/Vietnamese word representations/Category_classification_data/category_title_raw_json/category_only/dantri_category_only.json"
thanhnien = "H:/Vietnamese word representations/Category_classification_data/category_title_raw_json/category_only/thanhnien_category_only.json"
tuoitre = "H:/Vietnamese word representations/Category_classification_data/category_title_raw_json/category_only/tuoitre_category_only.json"
# vnexpress ="H:/Vietnamese word representations/Category_classification_data/category_title_raw_json/category_only/vnexpress_category_only.json"
vnn = "H:/Vietnamese word representations/Category_classification_data/category_title_raw_json/category_only/vnn_category_only.json"
vtv = "H:/Vietnamese word representations/Category_classification_data/category_title_raw_json/category_only/vtv_category_only.json"

file_list = [dantri, thanhnien, tuoitre, vnn, vtv]

# for f in file_list:
#     unique_category(f, '(only_category).txt')

count_category(all_category, category_count)
