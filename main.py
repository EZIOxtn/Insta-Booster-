modules = [
    "threading", "time", "requests", "datetime", "os", "base64", "tempfile", 
    "re", "chardet", "typing", "urllib.parse", "prettytable", "concurrent.futures", 
    "httpx", "json", "colorama"
]




# ==============================================================================
# Made with 'LOVE -_-' BY EZIOxtn
# ==============================================================================
#  ███████ ███████ ██  ██████  
#  ██         ███  ██ ██    ██ 
#  █████     ███   ██ ██    ██ 
#  ██       ███    ██ ██    ██ 
#  ███████ ███████ ██  ██████  xtn
# ==============================================================================
# Description: This script provides a command-line interface for setting 
# configuration in a JSON file. It allows users to start a process directly or 
# modify specific configuration parameters. if u use it dont forget to mention me 
# Dont buy it or sell it , its free for every one

#
# ==============================================================================

# soon   / :: accounts DBs ;)







import platform
for module in modules:
    try:
        __import__(module)
    except ImportError:
        try:
            import os
            os.system(f"pip install {module + "--break-system-packages" if platform.system() == 'Linux' else module}")
        except Exception as e:
            print(f"Failed to install module {module}: {e}")
import argparse
import threading
import time
import requests
from datetime import datetime
import os
import base64
import tempfile
import sys
import re
import chardet
from typing import Dict,List
from urllib.parse import quote
from prettytable import PrettyTable
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock
import httpx
import json
from colorama import init, Fore,Back
requests.packages.urllib3.disable_warnings()
from random import randint as rd
import math
mediaID = '3452099268087052040_69025336415'
mediaCode = 'C_oUf6LtvcI'
Raw_id = 'dfgjhdkfjgkjg654'
mediaUsername = 'protechps5'
mediaUserID = '69025336415'
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
X_IG_APP_ID = "93661974..." 
X_FB_LSD = "AVqbxe3J_YA"
fail = 0
succ = 0
import httpx
import json
from urllib.parse import quote
from typing import Dict

app_id = "936619743392459"
client = httpx.Client(
    headers={
        "x-ig-app-id": app_id,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9,ru;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "*/*",
    }
)
def LoadSetConfig(contentTosetJson=None):
    file_path = "Config.json"
    
    if contentTosetJson:
        with open(file_path, "w") as file:
            json.dump(contentTosetJson, file, indent=4)  
        return True
    
    with open(file_path, "r") as file:
        data = json.load(file)
    
    username = data["username"]
    insta_post = data["InstaPost"]
    email = data["email"]
    password = data["password"]

    author_name = data["author"]["name"]
    author_username = data["author"]["username"]
    author_followers = data["author"]["followers"]
    author_following = data["author"]["following"]
    author_private = data["author"]["private"]

    debug = data["debug"]
    
    return data


def get_instagram_graphql_data(url):
    ig_id = get_id(url)
    if not ig_id:
        return json.dumps({"error": "Invalid URL"})
    
    # Prepare the GraphQL endpoint and parameters
    graphql_url = "https://www.instagram.com/api/graphql"
    variables = json.dumps({"shortcode": ig_id})
    params = {
        "variables": variables,
        "doc_id": "10015901848480474",
        "lsd": X_FB_LSD,
    }
    
    headers = {
        "User-Agent": USER_AGENT,
        "Content-Type": "application/x-www-form-urlencoded",
        "X-IG-App-ID": X_IG_APP_ID,
        "X-FB-LSD": X_FB_LSD,
        "X-ASBD-ID": "129477",
        "Sec-Fetch-Site": "same-origin"
    }
    
    response = requests.post(graphql_url, headers=headers, data=params)
    
    if response.status_code != 200:
        return str(json.dumps({"error": f"Failed to fetch data: {response.status_code}"}))
    
    json_data = response.json()
    x = json.dumps(json_data)
    return json_data
    

def get_id(url):
    regex = r"instagram.com\/(?:[A-Za-z0-9_.]+\/)?(p|reels|reel|stories)\/([A-Za-z0-9-_]+)"
    match = re.search(regex, url)
    return match.group(2) if match else None
def getCode(url_or_shortcode):
    if "http" in url_or_shortcode:
        try:
            
            return url_or_shortcode.split("/p/")[-1].split("/")[0]
        except:
            return "Link Error"
        
    else:
        return url_or_shortcode
def scrape_m2(user):
    headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.5',
    'origin': 'https://www.tucktools.com',
    'priority': 'u=1, i',
    'referer': 'https://www.tucktools.com/',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Brave";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
}
    params = {
    'username': user,
}
    try:
        r = requests.get('https://fanhub.pro/tucktools_user', params=params, headers=headers)
        try:
            js = r.json()
            f = extract_fields(js,"U2")
            return f
        except:
            return {}
    except:
        return {}
def scrapePostM2(url_or_shortcode):
    shortcode = ""
    if "http" in url_or_shortcode:
        try:
            shortcode = url_or_shortcode.split("/")[-2]
        except:
            print()
        
    else:
        shortcode = url_or_shortcode
    
    dict = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_")
    

    indexes = [dict.index(char) for char in shortcode]
    #print({"Mediaid":str(from_radix(indexes, 64))})
  
    return {"Mediaid":str(from_radix(indexes, 64)),"++":str(from_radix(indexes, 64))}
    
def from_radix(digits, radix):
   
    return sum(digit * (radix ** index) for index, digit in enumerate(reversed(digits)))

def scrape_user(username: str) -> Dict:
    try:
        result = client.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}")
        
        try:
            data = json.loads(result.content)
            
            return extract_fields(data["data"]["user"],"U")
        except Exception as e:
            #print(e)
            return {"ErrorOccered_X00X": f"Failed to parse data -> the user {username} doesn't exist (api error)"}
    except:
        return {"ErrorOccered_X00X": "Internet Connection Error"}

def scrape_post(url_or_shortcode: str) -> Dict:
    if "http" in url_or_shortcode:
        try:
            shortcode = url_or_shortcode.replace("reel", "p")
        except:
            print()
        shortcode = url_or_shortcode.split("/p/")[-1].split("/")[0]
    else:
        shortcode = url_or_shortcode

    print(f"please wait ...")

    variables = {
        "shortcode": shortcode,
        "has_threaded_comments": True,
    }
    url = "https://www.instagram.com/graphql/query/?query_hash=b3055c01b4b222b8a47dc12b090e4e64&variables="
    try:
        result = httpx.get(
            url=url + quote(json.dumps(variables)),
            headers={"x-ig-app-id": app_id},
            timeout=60
        )
        try:
            #print(result.content)
            data = json.loads(result.content)
            return extract_fields(data["data"]["shortcode_media"], "P")
        except:
            return {"ErrorOccered_X00X": f"Failed to parse data -> the post {url_or_shortcode} doesn't exist"}
    except:
        return {"ErrorOccered_X00X": "Internet Connection Error"}

def extract_fields(posts, typeOfContent=None):
    #print(posts)
    if isinstance(posts, dict):
        if typeOfContent == "P":
            result = [
                posts["owner"]["username"],
                posts["id"],
                posts["shortcode"],
                str(posts["edge_media_preview_comment"]["count"]),
                str(posts["edge_media_preview_like"]["count"])
            ]
            return result
        elif typeOfContent == "U":
            result = [
                posts["biography"],
                str(posts["edge_followed_by"]["count"]),
                str(posts["edge_follow"]["count"]),
                posts["full_name"],
                "public" if not posts["is_private"] else "private",
                posts["id"],
                posts["username"]
            ]
            return result
        elif typeOfContent == "U2":
            result = [
                posts["user_description"],
                str(posts["user_followers"]),
                str(posts["user_following"]),
                posts["user_fullname"],
                "public" if not posts["is_private"] else "private",
                posts["id"],
                posts["username"]
            ]
            return result
        #pprint("this is the media id here ",posts["Mediaid"])
        result = [posts["Mediaid"]]
        return result

def perform_tasks(sessions, sites):
    counter = 0
    dateStart = datetime.now()
    cntloader = 0
    analytics = 0
    followers = 0
    conteur_def = 0
    totfollowers = 0
    newf = 0
    commentlist = []
    commentlist = CommentParcer()
    CmtIndex = 0
    CmtFinalIndex = len(commentlist)
    print(CmtFinalIndex)
    
    while True:
        CLR()
        logo()
        try:
            print("           hits: success " + str(statlogin[0]) + " fail : " + str(statlogin[1]))
        except:
            pass
        print("\n")
        total_tasks = len(sites)
        
        for i, fd in enumerate(range(len(sites))):
            progress = int((i + 1) / total_tasks * 100)
            done = '█' * (progress // 2)
            remaining = '░' * (50 - (progress // 2))
            
            print(f'\r[{done}{remaining}] {progress}% {fd + 1}/{total_tasks}', end='', flush=True)

            cntloader += 1
            if cntloader == 4:
                cntloader = 0

            addF(sessions[fd], sites[fd]["add_follower"])
            addLike(sessions[fd], sites[fd]["send_like"])
            addProfileView(sessions[fd], "https://" + ExtractDom(sites[fd]["login"]) + "/tools/send-view?formType=send")
            addView(sessions[fd], "https://" + ExtractDom(sites[fd]["login"]) + "/tools/send-view-video/{mediaID}?formType=send")
            addPostSave(sessions[fd], "https://" + ExtractDom(sites[fd]["login"]) + "/tools/send-save/{mediaID}?formType=send")
            ## STORY VIEWS SHOULD BE ADDED AS SOON AS POSSIBLE ##################
            if commentlist != []:
                try:
                    addComment(sessions[fd], "https://" + ExtractDom(sites[fd]["login"]) + "/tools/send-comment/{mediaID}?formType=send&clearCommentedIndex=0", commentlist[CmtIndex-1])
                    if CmtIndex != CmtFinalIndex :
                    	CmtIndex = CmtIndex + 1
                    else:
                    	CmtIndex = 0
                except Exception as e:
                    DebuggerLog(str(e))
                    CmtIndex = 0
                    pass
            time.sleep(6)
        ############################################################################"
        counter += 1
        elapsed_time = datetime.now() - dateStart
        resultat_final = ""
        v, l, o = "N/A", "N/A", "N/A"
        name = ""
        res = {}
        if analytics == 0:
            try:
                res = instaconteur_defer(mediaUsername)
                res = json.loads(res)
            except Exception as e:
                res = {}
                print(f"Error fetching user data: {e}")
            
            if res:
                try:
                    followers = int(res.get('user_followers', 0))
                    conteur_def = followers - newf
                    name = res.get("username", "Unknown")
                    resultat_final = f"{name} {str(followers)} {'+' if conteur_def > 0 else ''}{str(conteur_def)} ↑" if conteur_def > 0 else \
                                     f"{name} {str(followers)} {str(conteur_def)} ↕" if conteur_def == 0 else \
                                     f"{name} {str(followers)} {str(conteur_def).replace('-', '')} ↓"
                    newf = followers
                except :
                    pass
            else:
                resultat_final = f"{name} {str(followers)} {str(conteur_def)} ↕"

            try:
                data = get_instagram_graphql_data(f"https://www.instagram.com/reel/{mediaCode}")
                
                

                media_data = data["data"]["xdt_shortcode_media"]
                if media_data:
                    try:
                        
                        v = media_data["video_view_count"]
                    except:
                        pass
                    l = media_data["edge_media_preview_like"]["count"]
                    o = media_data["owner"]["username"]
                else:
                    v, l, o = "N/A", "N/A", "N/A"
                
            except Exception as e:
                
                v, l, o = "N/A", "N/A", "N/A" # it was work !!! : )

            print(f"\nFollowers: {counter} | {resultat_final} | Post by {o}: {v} views, {l} likes | Hits : S {Stat[0]} D {Stat[1]} E {Stat[2]} | {elapsed_time.seconds // 3600}h {elapsed_time.seconds // 60 % 60}m", end='', flush=True) # this print should now !!!

            analytics = 0
        else:
            analytics += 1
        
        time.sleep(30)
def CommentParcer():
    me = True
    file = "comments.txt"
    if IsNotEmptyFile(file) == True:
        me = True
    else :
    	return [] 

    with open(file, 'rb') as f:
        raw_data = f.read()     
        result = chardet.detect(raw_data)
        encoding = result['encoding']
    parcedCmt = []
    try:
        
            with open('comments.txt', 'r', encoding=encoding) as f:
                for l in f:
                    cleaned_line = re.sub(r'\d+', '', l)                         
                    parcedCmt.append(cleaned_line.replace('\n',"").replace(".",""))
                                 
    except Exception as e:
        DebuggerLog(str(e))
        pass    
    return parcedCmt
def IsNotEmptyFile(file):
    return True
    try:
        cnt =""
        with open(file, 'rb') as f:
            raw_data = f.read()
            result = chardet.detect(raw_data)
            encoding = result['encoding']
        with open(file, 'r', encoding=encoding) as f:
            cnt = f.read()
        return False if cnt == "" else (True)
    except:
        return False
         
def instaconteur_defer(user):
    headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.5',
    'origin': 'https://www.tucktools.com',
    'priority': 'u=1, i',
    'referer': 'https://www.tucktools.com/',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Brave";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
}
    params = {
    'username': user,
}
    try:
        r = requests.get('https://fanhub.pro/tucktools_user', params=params, headers=headers)
        try:
            js = r.text
            
            return js
        except:
            return {}
    except:
        return {}
def blocker(file_name ="tempoPY", file_extension ="arm"):
    

    temp_dir = tempfile.gettempdir()
    temp_file_path = os.path.join(temp_dir, f"{file_name}.{file_extension}")

    file_exists = os.path.isfile(temp_file_path)
    with open(temp_file_path, 'wb') as temp_file:
        temp_file.write(b"This is a temporary file.")

    return file_exists
def checkblock(file_name ="tempoPY", file_extension ="arm"):
    temp_dir = tempfile.gettempdir()
    temp_file_path = os.path.join(temp_dir, f"{file_name}.{file_extension}")
    

    file_exists = os.path.isfile(temp_file_path)

    return file_exists
def CLR():
    if os.name == 'nt':  
        os.system('cls')
    else:
        #DB97rFPtq9Q
        os.system('clear')
def deob1(triostat):
   
    rdead = ''.join(chr(ord(char) - 3) for char in triostat)

    revloader = rdead[::-1]

    decoded = base64.b64decode(revloader).decode()

    return decoded
def start():
    global sessions, Stat, mediaID, mediaCode, mediaUsername, mediaUserID, statlogin, hits,Raw_id
    statlogin = [0,0]
    
    CLR()
    logo(True)
    
    if checkblock():
        print("Your are not allowed to use this script anymore") # i dunno why i did this this way but , Who knows !!!
        exit(1)
    Stat = [0, 0, 0, 0, 0, 0]
    protected = str((chr(50) + chr(54) + chr(51) + chr(51) + chr(52) + chr(53) + chr(57) + chr((int(round(math.factorial(5) - (3 ** 3) + (6 * 9) / 3) + (math.sqrt(144) - math.log(1)) + (10 * (16 / 4))))- 106)))
    print("this script is protected with password   \n \n")
    tier = 0
    var1 = ""
    while var1 is not protected:
        break
        var1 = input("script password   :")
        if var1 == protected:
            print("welcome")
            break
        else:
            print("wrong password, Try again", 3 - tier)
            tier += 1
            exit(1)
    if tier == 3 :
        print("Your are not allowed to use this script anymore")
        blocker()
        exit(1)
    CLR()
    time.sleep(3)
    logo()
    Load_Data = {}
    user = "marioxi@pxdmail.net"
    passw = "hamaheda"
    target = "eziox01"   # this is my insta by the way 
    reel = "DB97rFPtq9Q"
    try:
        Load_Data = LoadSetConfig()
        user = Load_Data["email"]
        passw = Load_Data["password"]
        target= Load_Data["username"]
        reel = Load_Data["InstaPost"]
        print(f"login Creds, target user and post set to: \n    [Username/Email]: {user}\n    [Password]: {passw}\n    [Target]: {target}\n    [reel]: {reel}")
    except Exception as e:
        print("No config file found 'Config.json' in the main directory  [exception occured]", e)
        
    
    if len(Load_Data) == 0:
        print("No config file found 'Config.json' in the main directory")
        exit(1)
    print("starting...")
    
    #print(user,passw,target,reel)

    Udata =scrape_user(target)
    #print(Udata)
    errCode = "ErrorOccered_X00X"
    if errCode in Udata :
        #print(Udata[errCode])
        #print("starting method 2 ...")
        Udata = scrape_m2(target)
        if Udata == {}:
            print("Error Type 'Unknown'")
            return
        
    time.sleep(3)
    
    #print(Udata)
    Uname = Udata[len(Udata)-1]
    Uid = Udata[len(Udata)-2]
   #  print(Uname, Uid)
    displayScrape(Udata,"User Data")
    
    #print("scraping post info...")
    Pdata =scrape_post(reel)
    
    if "ErrorOccered_X00X" in Pdata :
        #print(Pdata["ErrorOccered_X00X"])
        #print(f"the instagram post with link cannot be parced due to instagram api restriction \n Switching to Method2 (Only ID)")
        Pdata = scrapePostM2(reel)
        try:
            dataxa = get_instagram_graphql_data(reel)

            media_data = dataxa["data"]["xdt_shortcode_media"]
            if media_data:
                try:
                    
                    v = str(media_data["video_view_count"])
                except:
                    pass
                l = str(media_data["edge_media_preview_like"]["count"])
                o = str(media_data["owner"]["username"])
                print(f"post views : {v}\n likes : {l}\n owner : {o}")
            else:
                ## idunno why its not working ...
                v, l, o = "N/A", "N/A", "N/A"
                print(f"post views : {v}\n likes : {l}\n owner : {o}")
            
        except:
            pass
            
        
    
    Pid = (Pdata[1].replace("id :", "")) if "Mediaid" not in str(Pdata) else Pdata["Mediaid"]
    Pcode = Pdata[2].replace("code :", "") if "Mediaid" not in str(Pdata) else getCode(Pdata["Mediaid"])
    
    #displayScrape(Pdata,"Post Data")
    #checkFaccount(user, passw)
    mediaUsername = Uname  #  username
    mediaUserID = Uid # user ID
    Raw_id = Pid
    mediaID = f"{Pid}_{mediaUserID}"  # media ID
    mediaCode = Pcode  #  media code
    # print(mediaUsername,mediaUserID,mediaID,mediaCode)
    time.sleep(10)
    
    ## WHY OBFUSCATING LINKS IN AN OPEN SOURCE PROJECT ??
    ## ANS : MABE THEY ILL FIND OUT WE ARE USING THEIR API !!? 
    ## PASS THE ARGS --DEBUG true to see the links and api endpoints
    otherl =["@@zOxopO6<Jev<p]3Q[\\p<|O9PKf3UKd", "@;VeyQpOsQJfswZ\\38Zd3IJez<|O9PKf3UKd", "@@zOw<5\\xL[\\3QKfswZ\\3<|O9PKf3UKd", "@;VeyQpOsQJfswZ\\3oJexI5\\xf6g6<|O9PKf3UKd", "y35em8VdmE[duIJgsM[]}<|O9PKf3UKd", "@;VeyQpOxY5]sQJfswZ\\3<|O9PKf3UKd", "@;VeyQpOsQJfswZ\\38Zd3IJez<|O9PKf3UKd", "@@zOw<5\\xXphsQqfog6ev{5ep<|O9PKf3UKd", "|Yp\\wYZey35em8VdmE[duIJgso[\\l<|O9PKf3UKd", "yT[]x8lfk][dmE[duIJgxf6g6<|O9PKf3UKd", "@@zOw<5\\xnJekM6dsQJfswZ\\3<|O9PKf3UKd", "@@zO3Ypexj[esQJfswZ\\3<|O9PKf3UKd", "@;VeyQpO7IZesQJfswZ\\3<|O9PKf3UKd", "@;VeyQpO|o5]sQJfswZ\\3<|O9PKf3UKd", "@;VeyQpOxYphsQJfswZ\\3<|O9PKf3UKd", "@@zOw<5\\xn5\\zo5dkU[dv8Z\\m<|O9PKf3UKd", "@@zOw<5\\xn5\\zo5dkU[d}E[]r<|O9PKf3UKd", "y35em8FfswZ\\3gZdl<|O9PKf3UKd", "yT[]x8|]xo5dsQJfswZ\\3<|O9PKf3UKd", "y35em8V]}Ip\\sQJfswZ\\3<|O9PKf3UKd", "y35em8FfswZ\\3Ipek<|O9PKf3UKd", "@@zOqM6exHJ]y4Z\\3Qqes<|O9PKf3UKd", "@;VeyQpOsQJfswZ\\3M[dl<|O9PKf3UKd", "y35em8V]woJgsQJfswZ\\3<|O9PKf3UKd", "@@zOw<5\\xL[\\3QKfswZ\\3<|O9PKf3UKd", "@;Gfko6fsM[dq<Fgo8pO|Y5gy{Jey]5]s<|O9PKf3UKd", "@;VeyQpO4Q[g3Y6dsQJfswZ\\3<|O9PKf3UKd"]

    sessions = []
    sites  = [
    {
      "login": f"{deob1(otherl[0])}member?",
      "add_follower": f"{deob1(otherl[0])}tools/send-follower/{mediaUserID}?formType=send",
      "send_like": f"{deob1(otherl[0])}tools/send-like/mediaID?formType=send"
    },
    {
      "login": f"{deob1(otherl[1])}member?",
      "add_follower": f"{deob1(otherl[1])}tools/send-follower/{mediaUserID}?formType=send",
      "send_like": f"{deob1(otherl[1])}tools/send-like/{mediaID}?formType=send"
    },
    {
      "login": f"{deob1(otherl[2])}login?",
      "add_follower": f"{deob1(otherl[2])}tools/send-follower/{mediaUserID}?formType=send",
      "send_like": f"{deob1(otherl[2])}tools/send-like/mediaID?formType=send"
    },
    {
      "login": f"{deob1(otherl[3])}login?",
      "add_follower": f"{deob1(otherl[3])}tools/send-follower/{mediaUserID}?formType=send",
      "send_like": f"{deob1(otherl[3])}tools/send-like/mediaID?formType=send"
    },
    {
      "login": f"{deob1(otherl[4])}member?",
      "add_follower": f"{deob1(otherl[4])}tools/send-follower/{mediaUserID}?formType=send",
      "send_like": f"{deob1(otherl[4])}tools/send-like/mediaID?formType=send"
    },
    {
      "login": f"{deob1(otherl[5])}login?",
      "add_follower": f"{deob1(otherl[5])}tools/send-follower/{mediaUserID}?formType=send",
      "send_like": f"{deob1(otherl[5])}tools/send-like/mediaID?formType=send"
    },
    {
      "login": f"{deob1(otherl[6])}member?",
      "add_follower": f"{deob1(otherl[6])}tools/send-follower/{mediaUserID}?formType=send",
      "send_like": f"{deob1(otherl[6])}tools/send-like/mediaID?formType=send"
    },
    {
      "login": f"{deob1(otherl[7])}member?",
      "add_follower": f"{deob1(otherl[7])}tools/send-follower/{mediaUserID}?formType=send",
      "send_like": f"{deob1(otherl[7])}tools/send-like/mediaID?formType=send"
    },
    {
      "login": f"{deob1(otherl[8])}login?",
      "add_follower": "https://bayitakipci.com/tools/send-follower/{mediaUserID}?formType=send",
      "send_like": "https://bayitakipci.com/tools/send-like/mediaID?formType=send"
    },
    {
      "login": f"{deob1(otherl[9])}login?",
      "add_follower": f"{deob1(otherl[9])}tools/send-follower/{mediaUserID}?formType=send",
      "send_like": f"{deob1(otherl[9])}tools/send-like/mediaID?formType=send"
    },
    {
      "login": f"{deob1(otherl[10])}login?",
      "add_follower": f"{deob1(otherl[10])}tools/send-follower/{mediaUserID}?formType=send",
      "send_like": f"{deob1(otherl[10])}tools/send-like/mediaID?formType=send"
    },
    {
      "login": f"{deob1(otherl[11])}login?",
      "add_follower": f"{deob1(otherl[11])}tools/send-follower/{mediaUserID}?formType=send",
      "send_like": f"{deob1(otherl[11])}tools/send-like/mediaID?formType=send"
    },
    {
      "login": f"{deob1(otherl[12])}login?",
      "add_follower": f"{deob1(otherl[12])}tools/send-follower/{mediaUserID}?formType=send",
      "send_like": f"{deob1(otherl[12])}tools/send-like/mediaID?formType=send"
    },
    {
      "login": f"{deob1(otherl[13])}login?",
      "add_follower": f"{deob1(otherl[13])}tools/send-follower/{mediaUserID}?formType=send",
      "send_like": f"{deob1(otherl[13])}tools/send-like/mediaID?formType=send"
    },
    {
      "login": f"{deob1(otherl[14])}login?",
      "add_follower": f"{deob1(otherl[14])}tools/send-follower/{mediaUserID}?formType=send",
      "send_like": f"{deob1(otherl[14])}tools/send-like/mediaID?formType=send"
    },
    {
      "login": f"{deob1(otherl[15])}login?",
      "add_follower": f"{deob1(otherl[15])}tools/send-follower/{mediaUserID}?formType=send",
      "send_like": f"{deob1(otherl[15])}tools/send-like/mediaID?formType=send"
    },
    {
      "login": f"{deob1(otherl[16])}member?",
      "add_follower": f"{deob1(otherl[16])}tools/send-follower/{mediaUserID}?formType=send",
      "send_like": f"{deob1(otherl[16])}tools/send-like/mediaID?formType=send"
    },
    {
      "login": f"{deob1(otherl[17])}member?",
      "add_follower": f"{deob1(otherl[17])}tools/send-follower/{mediaUserID}?formType=send",
      "send_like": f"{deob1(otherl[17])}tools/send-like/mediaID?formType=send"
    },
    {
      "login": f"{deob1(otherl[18])}login?",
      "add_follower": f"{deob1(otherl[18])}tools/send-follower/{mediaUserID}?formType=send",
      "send_like": f"{deob1(otherl[18])}tools/send-like/mediaID?formType=send"
    },
    {
      "login": f"{deob1(otherl[19])}login?",
      "add_follower": f"{deob1(otherl[19])}tools/send-follower/{mediaUserID}?formType=send",
      "send_like": f"{deob1(otherl[19])}tools/send-like/mediaID?formType=send"
    },
    {
      "login": f"{deob1(otherl[20])}login?",
      "add_follower": f"{deob1(otherl[20])}tools/send-follower/{mediaUserID}?formType=send",
      "send_like": f"{deob1(otherl[20])}tools/send-like/mediaID?formType=send"
    },
    {
      "login": f"{deob1(otherl[21])}login?",
      "add_follower": f"{deob1(otherl[21])}tools/send-follower/{mediaUserID}?formType=send",
      "send_like": f"{deob1(otherl[21])}tools/send-like/mediaID?formType=send"
    },
    {
      "login": f"{deob1(otherl[22])}member?",
      "add_follower": f"{deob1(otherl[22])}tools/send-follower/{mediaUserID}?formType=send",
      "send_like": f"{deob1(otherl[22])}tools/send-like/mediaID?formType=send"
    },
    {
      "login": f"{deob1(otherl[23])}login?",
      "add_follower": f"{deob1(otherl[23])}tools/send-follower/{mediaUserID}?formType=send",
      "send_like": f"{deob1(otherl[23])}tools/send-like/mediaID?formType=send"
    },
    {
      "login": f"{deob1(otherl[24])}login?",
      "add_follower": f"{deob1(otherl[24])}tools/send-follower/{mediaUserID}?formType=send",
      "send_like": f"{deob1(otherl[24])}tools/send-like/mediaID?formType=send"
    },
    {
      "login": f"{deob1(otherl[25])}girisyap?",
      "add_follower": "https://igfollower.net/tools/send-follower/{mediaUserID}?formType=send",
      "send_like": "https://igfollower.net/tools/send-like/mediaID?formType=send"
    },
    {
      "login": f"{deob1(otherl[26])}member?",
      "add_follower": f"{deob1(otherl[26])}tools/send-follower/{mediaUserID}?formType=send",
      "send_like": f"{deob1(otherl[26])}tools/send-like/mediaID?formType=send"
    },
    {
      "login": f"https://mixtakip.com/login?",
      "add_follower": f"https://mixtakip.com/tools/send-follower/{mediaUserID}?formType=send",
      "send_like": f"https://mixtakip.com/tools/send-like/mediaID?formType=send"
    },
    {
      "login": f"https://begenivar.com/login?member?",
      "add_follower": f"https://begenivar.com/tools/send-follower/{mediaUserID}?formType=send",
      "send_like": f"https://begenivar.com/tools/send-like/mediaID?formType=send"
    }
  ]


    
    step = 0
    CLR()
    logo()
    
    
    print("Please wait...")
    total_sites = len(sites)
    threads = []
    for i in sites:
        step += 1
        session = requests.Session()
        sessions.append(session)
        print(i['login'])
        login(session, user, passw, i['login'] )
        print(f'\rloading[{step}/{len(sites)}] success :{statlogin[0]} fail :{statlogin[1]}     ', end='', flush=True)
    if statlogin[1] == len(sites) :
        print("\n look like te fake account was banned, wrong, in challenge or doesnt exist, try to check it manually")
        return
    time.sleep(3)
    
    print("\n")
    print("booster started ... \n ")
    print("liker started ... \n ")
    print("followers started ... \n")
    time.sleep(5)
    args = (sessions, sites)
    threading.Thread(target=KeepSession, args=args, daemon=True).start()
    
    threading.Thread(target=perform_tasks, args=args, daemon=True).start()
    

    while True:
        time.sleep(1)
def login_task(i):
    session = requests.Session()
    login(session, user, passw, i['login'])
    sessions.append(session)
    step += 1
    print(f'loading[{step}/{len(sites)}] success :{statlogin[0]} fail :{statlogin[1]}      ', end='', flush=True)
       
def checkFaccount(user, passw):
    s = requests.Session()
    js = {"username": user,
          "password": passw}
    
    try:
        
        x = s.post("https://takipcigir.com/login?", json = js)
        x = x.text
        if "şifreni" in x:
            print("mot de passe erroné")
            exit(1)
        elif "code_verification" in x :
            di = text.json()
            res = di["allData"][""]
    except:
        print("Internet connection error")
        exit(1)
def login_task_thread(site, user, passw):
    session = requests.Session()
    try:
        login(session, user, passw, site['login'])
        sessions.append(session)
           
    except Exception as e:
        x = 5  
    return site['login']


def displayScrape(json_data, val):
   
    table = PrettyTable()
    table.field_names = [val]

    for value in json_data:
        table.add_row([value])

    print(table)
def ExtractDom(url):
    parts = url.split('/')
    if len(parts) > 2:
        domain = '/'.join(parts[2:-1])
        return domain
    else:
        return None
def KeepSession(sessions, sites):
    while True:
        for i, site in enumerate(sites):
            try:
                sessions[i].get("https://" + ExtractDom(site['login']) + "/ajax/keep-session")
            except Exception as e:
                try:
                    sessions[i].get("https://" + ExtractDom(site['login']) + "/ajax/keep-session", verify = False)
                except Exception as e:
                    pass
                    
                    # print(e)
            time.sleep(4)

def addLike(session, site):
    data = {
        'adet': '80',
        'mediaID': mediaID,
        'mediaCode': mediaCode,
        'mediaUsername': mediaUsername,
        'mediaUserID': mediaUserID
    }
    
    try:
        #print(site)
        response = session.post(site, json=data, timeout=30)
        process_response(response, Stat, success_idx=4)
    except requests.exceptions.Timeout:
        #print("(*)")
        pass
    except Exception as e:
        DebuggerLog(str(e))
        try:
            f = session.post(site, json= data, timeout=10, verify= False)
            process_response(f, Stat, success_idx=4)
            DebuggerLog("ssl error bypassed")
        except:
            pass
            
    

def addF(session, site):
    data = {'adet': '80', 'userID': mediaUserID, 'userName': mediaUsername}
    try:
        response = session.post(site, json=data, timeout=10)
        process_response(response, Stat, success_idx=0)
    except requests.exceptions.Timeout:
        pass
    except Exception as e:
        DebuggerLog(str(e))
        try:
            f = session.post(site, json= data, timeout=10, verify = False)
            process_response(f, Stat,success_idx=4)
        except:
            pass
            # print()
def addView(session, site):
    data = {
        'adet': '80',
        'mediaID': mediaID,
        'mediaCode': mediaCode
    }
    
    try:
        #print(site)
        response = session.post(site, json=data, timeout=30)
        process_response(response, Stat, success_idx=4)
    except requests.exceptions.Timeout:
        #print("(*)")
        pass
    except Exception as e:
        DebuggerLog(str(e))
        try:
            f = session.post(site, json= data, timeout=10, verify= False)
            DebuggerLog("ssl error bypassed")
        except:
            pass
def addProfileView(session, site):
    data = {
        'adet': '80',
        'userID': mediaID,
        'userName': mediaUsername
    }
    
    try:
        #print(site)
        response = session.post(site, json=data, timeout=30)
        process_response(response, Stat, success_idx=4)
    except requests.exceptions.Timeout:
        #print("(*)")
        pass
    except Exception as e:
        DebuggerLog(str(e))
        try:
            f = session.post(site, json= data, timeout=10, verify= False)
            DebuggerLog("ssl error bypassed")
        except:
            pass
def addPostSave(session, site):
    data = {
        'adet': '80',
        'mediaID': mediaID,
        'mediaCode': mediaCode
    }
    
    try:
        #print(site)
        response = session.post(site, json=data, timeout=30)
        process_response(response, Stat, success_idx=4)
    except requests.exceptions.Timeout:
        #print("(*)")
        pass
    except Exception as e:
        DebuggerLog(str(e))
        try:
            f = session.post(site, json= data, timeout=10, verify= False)
            DebuggerLog("ssl error bypassed")
        except:
            pass
def addComment(session, site, comment):
    
    data = {
  "yorum": [comment],
  "mediaID": mediaID,
  "mediaCode": mediaCode
}
    
    try:
        #print(site)
        response = session.post(site, json=data, timeout=30)
        process_response(response, Stat, success_idx=4)
    except requests.exceptions.Timeout:
        #print("(*)")
        pass
    except Exception as e:
        DebuggerLog(str(e))
        try:
            f = session.post(site, json= data, timeout=10, verify= False)
            DebuggerLog("ssl error bypassed")
        except:
            pass

def DebuggerLog(string):
    checker = LoadSetConfig()
    if checker["debug"]:
        if string.strip().startswith("<!DOCTYPE html>") or string.strip().startswith("<html") or "html" in string:
            print("html output error not a valid response (Json)")
        else:
            print(string)
        
def process_response(response, stats, success_idx):
    ctn = response.text
   
    
    try:
        data = response.json()  
        DebuggerLog( str(data))
    except :
        DebuggerLog("Invalid JSON response")
    if "success" in ctn:
        Stat[success_idx] += 1
    elif "duplic" in ctn:
        Stat[1] += 1 
    elif  "nocreditleft" in ctn:
        Stat[2] += 1
    else:
        Stat[5] += 1

def login(session, user, passwd, site):
    data = {"username": user, "password": passwd}
    try:
        response = session.post(site, json=data, timeout=30)
        DebuggerLog(response.text)
        if "success" in response.text and "html" not in response.text:
            statlogin[0] +=1
        else:
            statlogin[1] += 1
    except requests.exceptions.Timeout:
        statlogin[1] += 1
    except Exception as err:
        try:

            res = session.post(site, json= json, timeout=30, verify=False) # timeout=(5, 5)
            ctn = res.content.decode('utf-8')
            if "success" in ctn :

                statlogin[0] +=1
            else:
                
                statlogin[1] += 1
        except:
            statlogin[1] += 1
def logo(dispAuth = False):
    init(autoreset=True)
    PGname =  (
       Fore.YELLOW + "══════════════════════════╗\n" +
        Fore.YELLOW + "        InstaBoost             \n" +
        Fore.YELLOW + "    Your Instagram Growth     \n" +
        Fore.YELLOW + "       unofficial API [29 sites]   \n" +
        Fore.YELLOW + "══════════════════════════\n"

        +
        f"{Fore.RED}  IIIIIIIII \n"
        f"{Fore.YELLOW}Instagram Followers Booster\n"
        f"{Fore.BLUE}Powered by EZIOxtn\n"
    )
    S_L_print(PGname)
    if dispAuth == True:
        lines = [
    "O Z I R I S",
    "github.com/EZIOxtn",
    "eziotn.000.pe",
    "t.me/s/ozirisXta",
    ""
]
        for line in lines:
            S_print(line)
            
        
def S_print(text, width=45):
    padding = (width - len(text)) // 2
    spaces = " " * max(padding, 0) 
    print(spaces + text)
    time.sleep(0.2)
def S_L_print(text, width=52):
    lines = text.split('\n')
    
    for line in lines:
        padding = (width - len(line)) // 2
        spaces = " " * max(padding, 0)
        print(spaces + line)

def setConfig(filename = "Config.json", username=None, insta_post=None, email=None, password=None, debug=None):
    
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            config = json.load(file)
    else:
        config = {}

    if username is not None:
        config["username"] = username
    if insta_post is not None:
        config["InstaPost"] = insta_post
    if email is not None:
        config["email"] = email
    if password is not None:
        config["password"] = password
    if debug is not None:
        config["debug"] = debug

    with open(filename, 'w') as file:
        json.dump(config, file, indent=4)

def main():
    logo()
    parser = argparse.ArgumentParser(description="Insta Booster EZIOxtn")
    parser.add_argument('--start', action='store_true', help="Start the process directly without modifying the JSON file.")
    parser.add_argument('--username', help="Set the username.")
    parser.add_argument('--insta_post', help="Set the Instagram post URL.")
    parser.add_argument('--email', help="Set the email.")
    parser.add_argument('--password', help="Set the password.")
    parser.add_argument('--debug', action='store_true', help="Set the debug mode to true.")

    args = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    if args.start:
        print("Starting the process directly. no mods to the config file")
        try:
    
            start()
        except KeyboardInterrupt:
            print(Fore.RED + "\n script stopped , good bye")
            exit(1)

    if not any([args.username, args.insta_post, args.email, args.password, args.debug]):
        print("No arguments provided. Use --help for more information.")
        parser.print_help()
        return

    setConfig( args.username, args.insta_post, args.email, args.password, args.debug)
    print(f"Configuration updated in {args.filename}")
    try:
    
        start()
    except KeyboardInterrupt:
        print(Fore.RED + "\n script stopped , good bye")
        exit(1)
if __name__ == "__main__":
    main()