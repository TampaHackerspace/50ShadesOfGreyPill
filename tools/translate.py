from rapidconnect import RapidConnect
rapid = RapidConnect('openwerx-greypill', 'b6b91fb4-9c29-43ee-8ffe-342f8bca0dcf')

def gtDetectLang (text):
    return rapid.call('GoogleTranslate', 'detectLanguage', { 
	'apiKey': 'AIzaSyBv2QEVIH-ZNORgAJkTTaDmx_f_vMM5RYE',
	'string': text
    })
    

def gtAutoTranslate (text):
    return rapid.call('GoogleTranslate', 'translateAutomatic', { 
	'apiKey': 'AIzaSyBv2QEVIH-ZNORgAJkTTaDmx_f_vMM5RYE',
	'string': text,
	'targetLanguage': 'en'
    })

def gtTranslate (text, lang):
    return rapid.call('GoogleTranslate', 'translate', { 
	'apiKey': 'AIzaSyBv2QEVIH-ZNORgAJkTTaDmx_f_vMM5RYE',
	'string': text,
	'targetLanguage': 'en',
	'sourceLanguage': lang
    })

