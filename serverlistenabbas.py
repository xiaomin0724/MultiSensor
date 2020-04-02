import subprocess
from bottle import run, post, request, response, get, route
import sys

@route('/<path>',method = 'POST')
def process(path):
    print('Hello world!', file=sys.stderr)
    print(request.json, file=sys.stderr)           
    for i in request.json:
       print(request.json[i], file=sys.stderr)
     
    return subprocess.check_output(['python',path+'.py'],shell=True)

run(host='localhost', port=5000, debug=True)