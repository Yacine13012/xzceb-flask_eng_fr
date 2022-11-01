''' English to French and French to English Translator '''

import os

import json

from ibm_watson import LanguageTranslatorV3

from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']

url = os.environ['url']

authenticator = IAMAuthenticator('jFdSwZNrx5b7Yg0P-W7aryBwEoN77kZ5iSsX7XWR3jcU')

language_translator = LanguageTranslatorV3(
    version = '2021-09-22',
    authenticator = authenticator )

language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/2ff8c87d-25da-42e3-849e-f0ac5090f3b6')

def english_to_french(englishtext):
    ''' English to French Translator '''
    frenchtext = language_translator.translate(text = englishtext,model_id ='en-fr').get_result()
    return frenchtext['translations'][0]['translation']

def french_to_english(frenchtext):
    ''' French to English Translator '''
    englishtext = language_translator.translate(text = frenchtext,model_id = 'fr-en').get_result()
    return englishtext['translations'][0]['translation']
