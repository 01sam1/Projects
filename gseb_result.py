import requests as re
from bs4 import BeautifulSoup,SoupStrainer
import csv

headers ={
    'User-Agent':r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'Accept-encoding':'gzip, deflate, br, zstd',
    'origin':'https://www.gseb.org'
}
# ------------------------------------
def inputs(data='b5188171',total_seat_digits=7):
    # input details
    flag =1
    # data =input("enter seat no\n")
    first_char =data[0].upper()
    seat_no =data[1:]
    # validate seat no
    # print(ord(first_char)) 
    if 64<ord(first_char)<91 :
        flag =flag<<1     
    if seat_no.isdigit() and len(seat_no)==total_seat_digits:
        flag =flag<<1
    # verdict ----
    # print(flag)
    if flag==4:
        return(first_char,seat_no)
    else:
        return False
def parse2(ele):
    flag =0
    flag2 =0
    m=0
    n=0
    data=[]
    for i in ele:
        w =i.text
        if flag:
            if m==3:
                data.append(w)
                n+=1
            if m==4:
                m=0
                continue
            m+=1
        if n==6:
            flag=0
            # n=100
        if not flag and flag2==1:
            data.append(w[:3])
        if flag2:
            flag2+=1
            # print(flag2)
        if flag2==3:
            w =w.split('\n')
            # print(w)
            O=w[5].strip(" ").split(' ')
            data.append(O.pop())
            data.append(O.pop())
            # flag2=0
            break
        if w=='Subject Wise Grade':
            flag=1
        if not flag and w=='Grand Total':
            flag2 =1
    return data
                
def parse_web(content):
    a =SoupStrainer("table",{'class':'maintbl'})
    parser_ =BeautifulSoup(content,"html.parser",parse_only=a)
    ele =parser_.find_all('td')
    data =parse2(ele)
    # parse name
    name =ele[0].text
    name =name.split(' ')
    data.append(name[2])
    data.append(name[4]+' '+name[6]+' '+name[8])
    return data
# resamble the data stored in list eg:put seat no at first index etc...
def data_arrange(data):
    data_ =[]
    data_.append(data.pop())
    data_.append(data.pop())
    data_+=data
    return data_
def request(url="https://www.gseb.org/Result/SSCResultView",headers=headers,seatNo='b5188171'):
    # with open('gseb_cookie.json') as file:
    #     headers =file.read()
    try:     
        data={'InitialCharacter':'B','SeatNo':"5188171",'__Invariant':'SeatNo','Captcha':'13','hdnCaptcha':"QyydA53vkjHHFn2NWSLSKA==",'__RequestVerificationToken':"CfDJ8JXFi5j4wnBAjF6sjqJpvRSQ_yrqJAmn5PxJdVlc29oZb2YDqClgCgnbX8Aj9Xl8Wnmpy9ZRCGbdEfJa1dWqBpQPDCbptS8UsM8wpegffvuxfGErnx5m0ZM_QEkAw4hvlrddOPkQiS8QD-2JDLmc9HU"}
        seat_data =inputs(seatNo)
        if not seat_data:
            exit(0)
            # raise Exception("invalid seat data")
        data['InitialCharacter'] =seat_data[0]
        data['SeatNo'] =seat_data[1]
        D=re.post(url,headers=headers,data=data)
        # print(D.text)
        if D.status_code==200:
            # print(D.text)
            return parse_web(D.text)
        else:
            raise re.HTTPError('error in making the request')     
    except Exception as e:
        print('error')
        print(e)
        exit(500)
        
def main():
    # create threads
    # append data
    accumulate_data =[]
    counter =5188145
    first_char="B"
    for _ in range(0,50):
        T =counter
        s_n =first_char+str(T)
        data =request(seatNo=s_n)
        data =data_arrange(data)
        accumulate_data.append(data)
        print('d',end=' ')
        
        counter+=1
    with open('result_data.csv','at') as file:
        csv_pointer =csv.writer(file)
        csv_pointer.writerows(accumulate_data)
    print('sucess ....')

main()
# request(headers=headers)
