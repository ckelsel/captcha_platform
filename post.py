# importing the requests library 
import requests 
import argparse
import base64


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,                                                                                                                                                                                                             
            help="path to input image")   
args = vars(ap.parse_args())

# defining the api-endpoint  
API_ENDPOINT = "http://192.168.31.210:19952/captcha/v1"

image = open(args["input"], "rb")
image_data = base64.b64encode(image.read())
base64_string = image_data.decode()
image.close()

# sending post request and saving response as response object 
r = requests.post(API_ENDPOINT, json={'image': base64_string})


# extracting response text  
pastebin_url = r.text 
print("The pastebin URL is:%s"%pastebin_url)
