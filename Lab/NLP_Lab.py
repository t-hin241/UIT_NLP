#Hàm so khớp từ dài nhất--------------------------------------

def tokenizer(text, dict, is_show = False):
    print('Input: ', text, '\n')
    input = text.split(' ')
    words = []
    s = 0
    while True:
        e = len(input)
        while e > s:
            tmp_word = input[s:e]
            is_word = ''
            for item in tmp_word:
                is_word += item + ' '
            is_word = is_word[:-1]
            e -= 1
            if is_word.lower() in dict:
                words.append(is_word)
                break
            if e == s:
                words.append(is_word)
                break
                
        if e >= len(input):
            break
        
        if is_show:
            print('s = ', s)
            print('e = ', e)
            print(words[len(words)-1])
            print('-'*100)
        s = e + 1
        
    output = ''
    for item in words:
        output += item.replace(' ', '_')
        output += ' '
    output = output[:-1]
    
    return output

#Tạo dictionary từ file txt đã xác định từ ghép---------

with open('.\sent_tokened.txt', 'r', encoding='utf8') as f:
    text = f.read()
	#loại bỏ các dấu câu
    text1 = text.replace(".", " ")
    text2 = text1.replace("?"," ")
    text3 = text2.replace("("," ")
    text4 = text3.replace(")"," ")
    text5 = text4.replace(",","")
    sens = text5.split("\n")
    wordlist = []
    count = 0
    for i in range(len(sens)):
        sen = sens[i].split(' ')
        for j in range(len(sen)):
            if sen[j] not in wordlist:
                if '_' in sen[j]:
                    word = sen[j].replace('_', ' ')
                    count += 1				#đếm các từ ghép được thêm vào dict
                    wordlist.append(word)
                else:
                    wordlist.append(sen[j])
    dict = {}
    tmp = 0
    while tmp < len(wordlist):
        dict[wordlist[tmp]] = tmp
        tmp += 1

#In ra tần suất của từ ghép-----------------------------

print('Tan suat tu ghep:', count/len(wordlist))

#Chạy hàm với file txt chứa 40 câu Tiếng Việt-----------

with open('.\sentences.txt', 'r', encoding='utf8') as txt:
    test = txt.read()
    sentences = test.split("\n")
    for sentence in sentences:
        tmp = tokenizer(sentence, dict)
        print(tmp)
        print('\n---------------------------------------')
