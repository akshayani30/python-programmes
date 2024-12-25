def check_for_word():
    word="hello"
    with open("ak.txt","r") as f:
        data=f.read()
        if word in data:
            print("found")
        else:
            print("not found")
check_for_word()

def check_for_line():
    word="hello"
    data=True   #true means if data presend in it  if data=" "loop does not work
    line_no=1
    with open("ak.txt","r") as f:  #it opens and readline by line
        while data:
            data=f.readline()
        
            if(word in data):
                print(line_no)
                break
            line_no+=1

    return -1
check_for_line()