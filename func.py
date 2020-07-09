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


def is_bad(obj, key=None):
    title = obj['title']
    title = title.strip()
    if key is not None:
        return title in key


