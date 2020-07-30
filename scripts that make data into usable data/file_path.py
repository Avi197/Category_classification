
import os


# raw data
Vnn = 'H:/Vietnamese word representations/Category_classification_data/category_title_raw_json/vnn_category_raw.json'
Vnexpress = 'H:/Vietnamese word representations/Category_classification_data/category_title_raw_json/vnexpress_category_raw.json'
Thanhnien = 'H:/Vietnamese word representations/Category_classification_data/category_title_raw_json/thanhnien_category_raw.json'
Dantri = 'H:/Vietnamese word representations/Category_classification_data/category_title_raw_json/dantri_category_raw.json'
Tuoitre = 'H:/Vietnamese word representations/Category_classification_data/category_title_raw_json/tuoitre_category_raw.json'
Vtv = 'H:/Vietnamese word representations/Category_classification_data/category_title_raw_json/vtv_category_raw.json'


# clean up data
Dantri_category = 'H:/Vietnamese word representations/Category_classification_data/formatted_data/dantri_category.json'
Thanhnien_category = 'H:/Vietnamese word representations/Category_classification_data/formatted_data/thanhnien_category.json'
Tuoitre_category = 'H:/Vietnamese word representations/Category_classification_data/formatted_data/tuoitre_category.json'
Vnexpress_category = 'H:/Vietnamese word representations/Category_classification_data/formatted_data/vnexpress_category.json'
Vnn_category = 'H:/Vietnamese word representations/Category_classification_data/formatted_data/vnn_category.json'
Vtv_category = 'H:/Vietnamese word representations/Category_classification_data/formatted_data/vtv_category.json'


Vnn_category_only = 'H:/Vietnamese word representations/Category_classification_data/category_title_raw_json/category_only/vnn_category_only.json'
Vnexpress_category_only = 'H:/Vietnamese word representations/Category_classification_data/category_title_raw_json/category_only/vnexpress_category_only.json'
Thanhnien_category_only = 'H:/Vietnamese word representations/Category_classification_data/category_title_raw_json/category_only/thanhnien_category_only.json'
Dantri_category_only = 'H:/Vietnamese word representations/Category_classification_data/category_title_raw_json/category_only/dantri_category_only.json'
Tuoitre_category_only = 'H:/Vietnamese word representations/Category_classification_data/category_title_raw_json/category_only/tuoitre_category_only.json'
Vtv_category_only = 'H:/Vietnamese word representations/Category_classification_data/category_title_raw_json/category_only/vtv_category_only.json'

# test data
Dantri_test = 'H:/Vietnamese word representations/Category_classification_data/formatted_data/dantri_test.json'
Thanhnien_test = 'H:/Vietnamese word representations/Category_classification_data/formatted_data/thanhnien_test.json'
Tuoitre_test = 'H:/Vietnamese word representations/Category_classification_data/formatted_data/tuoitre_test.json'
Vnexpress_test = 'H:/Vietnamese word representations/Category_classification_data/formatted_data/vnexpress_test.json'
Vnn_test = 'H:/Vietnamese word representations/Category_classification_data/formatted_data/vnn_test.json'
Vtv_test = 'H:/Vietnamese word representations/Category_classification_data/formatted_data/vtv_test.json'

# not tokenized
Dantri_not_token = 'H:/Vietnamese word representations/Category_classification_data/formatted_data/dantri_not_token.json'
Thanhnien_not_token = 'H:/Vietnamese word representations/Category_classification_data/formatted_data/thanhnien_not_token.json'
Tuoitre_not_token = 'H:/Vietnamese word representations/Category_classification_data/formatted_data/tuoitre_not_token.json'
Vnexpress_not_token = 'H:/Vietnamese word representations/Category_classification_data/formatted_data/vnexpress_not_token.json'
Vnn_not_token = 'H:/Vietnamese word representations/Category_classification_data/formatted_data/vnn_not_token.json'
Vtv_not_token = 'H:/Vietnamese word representations/Category_classification_data/formatted_data/vtv_not_token.json'

# text data
# ---------
# windows
# Dantri_text = 'H:/Vietnamese word representations/Word_vector_data/text data/Dantri/dantri_data'
# Thanhnien_text = 'H:/Vietnamese word representations/Word_vector_data/text data/Thanhnien/thanhnien_data'
# Tuoitre_text = 'H:/Vietnamese word representations/Word_vector_data/text data/Tuoitre/tuoitre_data'
# Vnexpress_text = 'H:/Vietnamese word representations/Word_vector_data/text data/Vnexpress/vnexpress_data'
# Vnn_text = 'H:/Vietnamese word representations/Word_vector_data/text data/Vnn/vnn_data'
# Vtv_text = 'H:/Vietnamese word representations/Word_vector_data/text data/Vtv/vtv_data'
# ubuntu
Dantri_text = '/home/pham/NLU/text data/Dantri/dantri_data.json'
Thanhnien_text = '/home/pham/NLU/text data/Thanhnien/thanhnien_data.json'
Tuoitre_text = '/home/pham/NLU/text data/Tuoitre/tuoitre_data.json'
Vnexpress_text = '/home/pham/NLU/text data/Vnexpress/vnexpress_data.json'
Vnn_text = '/home/pham/NLU/text data/Vnn/vnn_data.json'
Vtv_text = '/home/pham/NLU/text data/Vtv/vtv_data.json'
# ---------


# tokenized data
# ---------
# windows
# Dantri_tokenized = 'H:/Vietnamese word representations/Word_vector_data/text data/Dantri/dantri_tokenized'
# Thanhnien_tokenized = 'H:/Vietnamese word representations/Word_vector_data/text data/Thanhnien/thanhnien_tokenized'
# Tuoitre_tokenized = 'H:/Vietnamese word representations/Word_vector_data/text data/Tuoitre/tuoitre_tokenized'
# Vnexpress_tokenized = 'H:/Vietnamese word representations/Word_vector_data/text data/Vnexpress/vnexpress_tokenized'
# Vnn_tokenized = 'H:/Vietnamese word representations/Word_vector_data/text data/Vnn/vnn_tokenized'
# Vtv_tokenized = 'H:/Vietnamese word representations/Word_vector_data/text data/Vtv/vtv_tokenized'
# ubuntu
Dantri_tokenized = '/home/pham/NLU/text data/Dantri/dantri_tokenized.txt'
Thanhnien_tokenized = '/home/pham/NLU/text data/Thanhnien/thanhnien_tokenized.txt'
Tuoitre_tokenized = '/home/pham/NLU/text data/Tuoitre/tuoitre_tokenized.txt'
Vnexpress_tokenized = '/home/pham/NLU/text data/Vnexpress/vnexpress_tokenized.txt'
Vnn_tokenized = '/home/pham/NLU/text data/Vnn/vnn_tokenized.txt'
Vtv_tokenized = '/home/pham/NLU/text data/Vtv/vtv_tokenized.txt'
# ---------

Data_not_tokenized = '"H:/Vietnamese word representations/Category_classification_data/newfile.txt"'