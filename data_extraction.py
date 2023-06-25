from pdf2image import convert_from_path
import pytesseract,re
import cv2

print("----------------------------------Patient_Information_file----------------------------------------------")
# pd_2.pdf file.
pd = r"/home/ankushp/Desktop/Data_Extraction/pd_2.pdf"
pd_pages = convert_from_path(pd, 350)
j = 1

pd_images_list=[]
for page in pd_pages:
    image_name = "pd_" + str(j) + ".jpg"
    page.save(image_name, "JPEG")
    pd_images_list.append(image_name)
    j= j+1

i=0
while i < len(pd_images_list):

    if i==0:
        img = cv2.imread(f'{pd_images_list[i]}')
        img = cv2.resize(img, (900, 800))
        img= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cv2.imshow("Output", img)
        cv2.waitKey(15)
        texts = pytesseract.image_to_string(img)

        m = (re.findall(r"(\bPatient Information\s.*\n.\w+\s\w+)", texts))
        words = ['Birth', 'Date']
        words_format = r'\b(?:{})\b'.format('|'.join(words))
        remove_words = lambda y: re.sub(words_format, ' ', y)
        m = list(map(remove_words,m))

        n = (re.findall(r"(\bBirth Date.*\n.*\n)", texts))
        words = ['Jerry', 'Lucas ']
        words_format = r'\b(?:{})\b'.format('|'.join(words))
        remove_words = lambda y: re.sub(words_format,"", y)
        n = list(map(remove_words,n))

        if m and n:
            print(m[0])
            print(n[0])

    else:
        img = cv2.imread(f'{pd_images_list[i]}')
        img = cv2.resize(img, (900, 800))
        img= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cv2.imshow("Output", img)
        cv2.waitKey(15)
        texts = pytesseract.image_to_string(img)
        m = re.findall(r"\bPolicy Number:\s\d+", texts)
        n = re.findall(r"\bExpiry Date:\s\d+.\s\w+.\s\d+", texts)
        if m and n:
            print(m[0])
            print(n[0])
    i+=1

print("\n----------------------------------Prescription_file----------------------------------------------")
#pre_2.pdf file

pre = r"/home/ankushp/Desktop/Data_Extraction/pre_2.pdf"
pre_pages = convert_from_path(pre)

for page in pre_pages:
    image_name = "pre_" + str(2) + ".jpg"
    page.save(image_name, "JPEG")
img = cv2.imread(f'{image_name}')
img = cv2.resize(img, (900, 855))
img= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow("Output", img)
cv2.waitKey(20)
custom_config = r'--oem 3 --psm 6'
texts = pytesseract.image_to_string(img,config=custom_config)
m = re.findall(r"\bName:\s.\w+", texts)
n = re.findall(r"\bDate:\s.*\n", texts)
if m and n:
    print(m[0])
    print(n[0])
