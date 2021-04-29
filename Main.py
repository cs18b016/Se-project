import shlex
from subprocess import Popen, PIPE
import requests

def exe_and_rtn(cmd):
    """
    Execute the external command and get its exitcode, stdout and stderr.
    """
    args = shlex.split(cmd)
    proc = Popen(args, stdout=PIPE, stderr=PIPE)
    out, err = proc.communicate()
    return out, err

def make_rqst(error):
    print("Searching for "+error)
    resp  = requests.get("https://api.stackexchange.com/"+"2.2/search?order=desc&tagged=python&sort=activity&intitle={}&site=stackoverflow".format(error))
    return resp.json()

def fetch_urls(json_dict):
    url_list = []
    count = 0
    for i in json_dict['items']:
        if i["is_answered"]:
            url_list.append(i["link"])
        count+=1
        if count == len(i) or count == 3:
            break
    import webbrowser
    for i in url_list:
        webbrowser.open(i)




if __name__ == "__main__":
    out, err = exe_and_rtn("python test.py")
    error_message = err.decode("utf-8").strip().split("\r\n")[-1]
    print(error_message)
    if error_message:
        filter_out = error_message.split(":")
        print(filter_out)
        print(filter_out[0])
        json1 = make_rqst(filter_out[0])
        json2 = make_rqst(filter_out[1])
        json = make_rqst(error_message)
        fetch_urls(json1)
        fetch_urls(json2)
        fetch_urls(json)
    else:
        print("No errors")
