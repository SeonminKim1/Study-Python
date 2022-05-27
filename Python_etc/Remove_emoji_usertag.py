# user_tag, emoji 삭제
import re

if '인스타그램' in f_name:
    # EMOJI, UserTag
    pattern_user_tag = re.compile("@[a-z0-9_.]*") 
    pattern_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
    data_n['댓글'] = data_n['댓글'].replace(pattern_user_tag, '')
    data_n['댓글'] = data_n['댓글'].replace(pattern_EMOJI, '')
    
elif 'Youtube' in f_name:
    pass