import file_path
import jsonlines
from langdetect import detect
import re
import os.path


"""
some records have 1 tag, which is also in bad_tag_list
some records have tag that is a link
"""

Vnn_infile = file_path.Vnn

vnn_bad_tags = ['vnn', 'vietnamnet', 'vietnamnetvn', 'vietnamnetvn doc bao', 'vietnamnet.vn',
                'tin nong', 'tin moi', 'doc bao']
vnn_english = 'news'
vnn_bad_title = ['Những hình ảnh ấn tượng trong tuần', 'Bản tin thời sự VTV', 'http://']

"""
Vnn has english titles, which we don't need
some tags are irrelevant to the title, e.g: vnn, vietnamnetvn doc bao,.... which is just to mark
the news source (???) 
some title are just 1 general text but with lots of usable tags, remove them
"""


"""
remove english news
remove all bad tags in bad_tags list
remove bad title
check if len(tags)>0

"""


# return true if tag is the same as title
def is_dup(obj, key=''):
    title = obj['title']
    tag = obj['tags'][0]
    title = title.strip()
    tag = tag.strip()
    if tag == title:
        return True
    elif tag != title:
        title = f'{title}{key}'
        if tag == title:
            return True
        else:
            return False


# check if title is in bad_title list
def check_bad_title(obj, bad_title_list=None):
    title = obj['title']
    title = title.strip()
    if bad_title_list is not None:
        count = 0
        for bad_title in bad_title_list:
            if bad_title in title:
                count += 1
        return count > 0


# return True if no english keyword in tags found
def check_english(tags, english_keys):
    for tag in tags:
        count = 0
        if english_keys not in tag:
            count += 1
        if count == 0:
            return True
# ???????????
# don't know why it work lol
# if not check_english(tags, english_keys):
#     dump


# clean up data
# write to file_data
# get only tags and title from raw json
# also get rid of some bad tags
# this one is for vnn only
# Vnn has some tags that are irrelevant
# e.g: vnn, vietnamnet, ...
# NOTE
# you can use outfile.write(new_obj) to reduce the size of output file, as it move all "idObject"
def get_data_vnn(infile, bad_tag_list, bad_title_list, english_keys=''):
    count_line = 1

    if 'json' in infile:
        file_name = infile.replace('.json', '')
    else:
        file_name = infile
    with jsonlines.open(infile) as file:
        with jsonlines.open(f'{file_name}_data(write_new_obj)', 'w') as outfile:
            for obj in file:
                new_obj = {}
                tags = obj['category']
                title = obj['title']
                new_obj['tags'] = []
                # check if news is not english news
                if not is_dup(obj):
                    if not check_english(tags, english_keys):
                        # check if news in previous list is not english news (again)
                        if detect(title) == 'vi':
                            for tag in tags:
                                # check for news with unusable tags
                                if tag not in bad_tag_list:
                                    new_obj['tags'].append(tag)
                            new_obj['title'] = obj.get('title')
                            if len(new_obj['tags']) == 1:
                                if 'http://' not in new_obj['tags'][0]:
                                    if not check_bad_title(new_obj, bad_title_list):
                                        outfile.write(new_obj)
                            elif len(new_obj['tags']) > 1:
                                if not check_bad_title(new_obj, bad_title_list):
                                    outfile.write(new_obj)
                print(f'done line {count_line}')
                count_line += 1
            print(f'wrote to {file_name}_data')


get_data_vnn(Vnn_infile, bad_tag_list=vnn_bad_tags, bad_title_list=vnn_bad_title, english_keys=vnn_english)
