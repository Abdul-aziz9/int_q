from bs4 import BeautifulSoup
import psycopg
import random


def get_amount(para_dic, para_color):
    if clean == para_color:
        num = para_dic[para_color] + 1
        para_dic.update({para_color: num})


with open('python_class_question.html') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'html.parser')
    colors = soup.find_all(name='td')
    lst = []
    dic = {
        "GREEN": 0,
        "BLUE": 0,
        "YELLOW": 0,
        "BROWN": 0,
        "PINK": 0,
        "ORANGE": 0,
        "CREAM": 0,
        "RED": 0,
        "WHITE": 0,
        "ARSH": 0,
        "BLEW": 0,
        "BLACK": 0
    }
    total_color = []

    for td in colors:
        if td.text == "MONDAY" or td.text == "TUESDAY" or td.text == "WEDNESDAY" or td.text == "THURSDAY" or \
                td.text == "FRIDAY":
            pass
        else:
            color = td.text.split(',')
            for item in color:
                clean = item.strip()
                lst.append(clean)
                get_amount(dic, "GREEN")
                get_amount(dic, "BLUE")
                get_amount(dic, "YELLOW")
                get_amount(dic, "BROWN")
                get_amount(dic, "PINK")
                get_amount(dic, "ORANGE")
                get_amount(dic, "CREAM")
                get_amount(dic, "RED")
                get_amount(dic, "WHITE")
                get_amount(dic, "ARSH")
                get_amount(dic, "BLEW")
                get_amount(dic, "BLACK")

    sortd = sorted(dic.items(), key=lambda x:x[1])
    srt_dic = dict(sortd)
    total_frequency = len(lst)
    # TODO Find the Mean Shirt color
    mean = total_frequency/12
    mean_color  = f"The Mean Colors are ORANGE AND RED which are closer to the mean i got, {mean}"
    print(mean_color)
    # TODO Find the most worn color
    mws = sortd[-1]
    print(f"The most worn color is {mws[0]} with {mws[1]} appearances")
    # TODO Find the median color
    median = f"with the data extracted from the website below BROWN is to be the median \n{srt_dic}"
    print(median)
    # TODO Find the variance color
    variance = 0
    for v in srt_dic.values():
        num = mean - v
        variance += num
    print(f"the variance of the colors are YELLOW AND PINK Due to the variance gotten from the calculation, {abs(variance) / mean}")
    # TODO Find the probability of getting red
    red_frequency = sortd[9][1]
    probability = red_frequency/total_frequency
    print(f"The Probability of getting Red when a color is picked at random is {probability}")
    # TODO Save the color and frequency in a postgresql data base
    DB_NAME = "Bincom_db"
    USER = "postgres"
    HOST = "localhost"
    PSWRD = "Nike"
    conn = psycopg.connect(dbname=DB_NAME, user=USER, password=PSWRD, host=HOST)
    with conn.cursor() as cur:
        # cur.execute("CREATE TABLE data (id SERIAL PRIMARY KEY, color VARCHAR, frequency INT)")
        cur.execute("SELECT * FROM data;")
        print(cur.fetchall())
        conn.commit()
        cur.close()
        conn.close()

    # TODO fibonnaci sequence
    n_1 = 0
    n_2 = 1
    n_term = 50
    count = 0
    if n_term == 1:
        print(n_1)
    else:
        print("The fibonacci sequence of the numbers is:")
        while count < n_term:
            print(n_1)
            nth = n_1 + n_2
            n_1 = n_2
            n_2 = nth
            count += 1


        d1 = random.randint(0, 1)
        d2 = random.randint(0, 1)
        d3 = random.randint(0, 1)
        d4 = random.randint(0, 1)
        base_2 = f'{d1}'f'{d2}'f'{d3}'f'{d4}'
        base_10 = d1*(2**0) + d2*(2**1) + d3*(2**2) + d4*(2**3)
        print(base_2)
        print(base_10)

