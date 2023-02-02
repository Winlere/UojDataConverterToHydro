basepath='./problem/' # path to save problems
skip = True # Skip problem which has downloaded(exists folder)
only_public = True # Only download the public problem(not hidden)
url = 'http://uoj.ac' # Site's url. DO NOT OMIT http
pre = 'U' # Id prefix
extags=['uoj'] # [] # Tags to add
defaulttags= [] #['待标记'] # Default tags for problems has no tags
# template for problem.yaml. 
templ =\
    '''
pid: {pid}
owner: 1
title: "{title}"
tag:
{tags}
nSubmit: 0
nAccept: 0
'''
retry_cnt = 3 # retry times when failed