
import json
import os
from pprint import pprint
# pth = r'/Users/ironieser/Documents/shanghaitech/project/llm4video/videochat_instruct_11k.json'
# # video_pth = file_js[data_index]['video']
# # Q = file_js[data_index]['QA'][QA_index]['q']
# # A = file_js[data_index]['QA'][QA_index]['a']
# pth2 = r'/Users/ironieser/Documents/shanghaitech/project/llm4video/csv_qa.json'


# with open(pth2) as f:
#     file = f.read()
# pprint(file)
# file_js = json.loads(file)
# pprint(file_js)

import json
# file =  [{ "video_0":'the path of video 0 ',
#             "video_1":'the path of video 1 ',
#             "QA":[
#                 {'q':'the question 1',
#                  'a':'the answer 1',
#                     },
#                 {'q':'the question 2',
#                  'a':'the answer 2',  },
#                 ] },
#         { "video_0":'the path of video 0',
#             "video_1": None,
#             "QA":[
#                 {'q':'the question 1',
#                  'a':'the answer 1',
#                     },
#                 {'q':'the question 2',
#                  'a':'the answer 2',
#                     },
#                 ]
#            }
#         ] 
pth2 = r'/Users/ironieser/Documents/shanghaitech/project/llm4video/instruction_demo.json'

with open(pth2) as f:
    file = f.read()
file_js = json.loads(file)
print(file_js)