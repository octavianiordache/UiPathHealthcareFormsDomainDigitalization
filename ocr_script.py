import easyocr

def extract_handwritten_text(image_path):
	import easyocr
    reader = easyocr.Reader(['ro']) 
    results = reader.readtext(image_path)
    extracted_text = "\n".join([text[1] for text in results])
    return extracted_text
