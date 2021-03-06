import tkinter as tk
import tkinter.filedialog as fl
import PyPDF2
import pprint
import os,errno
    
def removearticles(text):
    articles = {'a': '', 'an':'', 'and':'', 'the':'','his': '','her': '','this': '' \
                , 'all':'', 'its':'', 'one':'', 'now':'', 'also':'', 'had':'' \
                , 'him':'', 'to':'', 'only':'', 'has':'', 'they':'', 'are':'' \
                , 'our':'', 'be':'', 'we':'', 'by':'', 'of':'', 'other':'' \
                , 'into':'', 'from':'','in':'', 'that':'', 'can':'', 'you':'' \
                , 'is':'', 'for':'','as':'', 'with':'', 'or':'','have':'' \
                ,'it':'', 'on':'','your':'', 'many':'', 'their':'','not':'' \
                ,'through':'', 'which':'','get':'', 'but':'', 'some':'' \
                ,'them':'','may':'', 'out':'','more':'', 'what':'', 'these':'' \
                ,'very':'','do':'', 'if':'','there':'', 'about':'', 'often':'' \
                ,'up':'','how':'', 'such':'','at':'', 'so':'', 'like':''}
    rest = []
    words = {}
    for word in text.split():
        if word not in articles:
            words.setdefault(word, 0)
            words[word] = words[word] + 1
    file2 = open("D:\\pdf_dict.txt", 'w')
    #sorteddict = sorted(words, key=words.get)
    for word in sorted(words, key=words.get,reverse=True):
        file2.write(str(word) + ': ' + str(words[word]) + "\n")
    file2.close()
    
    for word in words.keys():
        rest.append(word)
    return ' '.join(e for e in rest if e.isalpha())

def remspclchar(text):
    temp = text
    temp = temp.replace(',','')
    temp = temp.replace('.','')
    temp = temp.replace('(','')
    temp = temp.replace(')','')
    temp = temp.replace('-','')
    return temp
  
def unique_file(input_filename, output_filename):
    pdf = PyPDF2.PdfFileReader(open(input_filename, "rb"))
    file_contents = ''
    for page in pdf.pages:
        file_contents_page = page.extractText().encode("ascii", "ignore").decode("utf-8")
        file_contents =  file_contents + file_contents_page.lower()
    #input_file.close()
    file1 = open("D:\\pdf_org.txt", 'w')
    file1.write(str(file_contents) + "\n")
    file1.close()
    
    file_contents = remspclchar(file_contents)
    file_contents = removearticles(file_contents)
    
    word_list = file_contents.split()    
    file = open(output_filename, 'w')
    unique_words = set(word_list)
    for word in unique_words:
        file.write(str(word) + "\n")
    file.close()


root = tk.Tk()
root.withdraw()
try:
    input_filename = fl.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("pdf files","*.pdf"),("pdf files","*.PDF")))
except FileNotFoundError:
    print("Wrong file or file path")


output_filename = "D:\\pdf_res.txt"
unique_file(input_filename, output_filename)
print ('done')
