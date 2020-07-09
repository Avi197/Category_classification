import jsonlines
import os
import file_path
import time
import re
from vncorenlp import VnCoreNLP


Dantri_infile = file_path.Dantri
Dantri_category = file_path.Dantri_category

filename = os.path.dirname(Dantri_category)
if not os.path.exists(filename):
    os.makedirs(filename)


# with VnCoreNLP(address='http://127.0.0.1', port=9000) as vncorenlp:
#     with jsonlines.open(data + '.json') as file:
#         with open(output, 'w', encoding='utf-8') as out:
#             for obj in file:
#                 if obj['tags'][0]:
#                     for tag in obj['tags']:
#                         tag = tag.strip()
#                         for _ in range(5):
#                             try:
#                                 tag = vncorenlp.tokenize(tag)
#                                 break
#                             except:
#                                 print("retry")
#                                 time.sleep(5)
#                         if len(tag) > 1:
#                             print("NOPE")
#                             for t in tag:
#                                 label = ' '.join(t)
#                         else:
#                             label = ' '.join(tag[0])
#                             label = re.sub(r' ', '-', label)
#                         # out.write('__label__%s ' % label)
#                         out.write(f'__label__{label} ')
#                     for _ in range(5):
#                         try:
#                             word_seg = vncorenlp.tokenize(obj['title'])
#                             break
#                         except:
#                             print('retry')
#                             time.sleep(5)
#                     if len(word_seg) > 1:
#                         print("NOPE-2")
#                         for sent in word_seg:
#                             seg = ' '.join(sent)
#                             out.write(seg + ' ')
#                     else:
#                         seg = ' '.join(word_seg[0])
#                         out.write(f'{seg} ')
#                     out.write('\n')
#                 print('done line {0}'.format(count))
#                 count += 1


def get_data_dantri(infile):
    count_line = 1
    with VnCoreNLP(address='http://127.0.0.1', port=9000) as vncorenlp:
        with jsonlines.open(infile) as infile:
            with jsonlines.open(Dantri_category, 'w') as outfile:
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
                    seg = ' '.join(word_seg)
                    outfile.write(f'{seg} ')
                    outfile.write('\n')
                    print('done line {0}'.format(count_line))
                    count_line += 1
                print(f'wrote to {Dantri_category}')


get_data_dantri(Dantri_infile)
