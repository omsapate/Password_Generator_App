import random
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = "jbi239tnbv4iu90984bcjjnehs67gjcbbs"

def Generate_Password(n):

    lower = "qwertyuiopasdfghjklzxcvbnm"
    upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
    symbols = "!@#$%^&*()?:"
    numbers = "1234567890"
    # lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
    # 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
    # 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']

    # upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
    # 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
    # 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
    
    # numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    # symbols = ['@', '#', '$', '%', '=', ':', '?', '>',
    # '*', '<','!']

    strict_four_char = random.sample(lower,1) + random.sample(upper,1) + random.sample(numbers,1) + random.sample(symbols,1)

    remain_char = random.sample(lower,n//2) + random.sample(upper,n//2) + random.sample(symbols,n//2) + random.sample(numbers,n//2)

    temp_pass = strict_four_char + random.sample(remain_char, n-4)
    random.shuffle(temp_pass)
    
    password = "".join(temp_pass)

    return password

@app.route("/", methods=['POST', 'GET'])
def index():
    # count = int(input("Enter number"))
    # password = Password(count)
    if request.method == "POST":
        pass_length = int(request.form['pass_length'])
        #print(type(pass_length))
        
        password = Generate_Password(pass_length)
        # print(password)
        return render_template("index.html", pass_generate = password, prev_length = str(pass_length))
    else:
        return render_template('index.html')
    


if __name__ == '__main__':
    app.run()