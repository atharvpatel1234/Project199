import socket 
from threading import Thread 
import random 

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip_address= '127.0.0.1'
port= 8000

server.bind((ip_address,port))
server.listen()

list_of_clients=[]

question=[
    ' Which crop is sown in the most important area in India?\n A.Rice \n B.Wheat \n C.Sugarcane \n D.Maize'

    ' Eritrea, which became the 182nd member of the United Nations in 1993, is on the continent of \n A.Asia\n B.Africa\n C.Europe\n D.Australia'

    ' Which of the subsequent personalities gave The Laws of Heredity?\n A.Robert Hook \n B.G.J. Mendel \n C.Darwin \n D.Harvey'

    ' Which of the subsequent national parks is not listed during a UNESCO World Heritage site?\nA.Kaziranga \n B.Keoladeo \n C.Sundarbans \n D.Kanha'

    ' The Capital of Ukraine is...?\n A.Delhi \n B.Colombo \n C.Kyiv \n D.Brussel'

    ' When did the planet Trade Organization inherit existence?\n A.1992 \n B.1993 \n C.1994 \n D.1995'

    ' Panchayati Raj belongs to...\n A.Residual list \n B.Concurrent list \n C.State list \n D.Union list'

    ' The symbol Au stands for what element?\n A.Gold \n B.Silver \n C.Copper \n D.Tin'

    ' Where is the headquarters of the World Economic Forum?\n A.India \n B.Switzerland \n C.USA \n D.Russia'

    ' What is the currency of India?\n A.Dollar \n B.Rupees \n C.Iraqi Dinar \n D.Ngultrum '

]

answers=[
    'A','B','B','D','C','D','C','A','B','B'
]

def clientthread(conn,):
    score=0
    conn.send("Welcome to this quiz game!".encode('utf-8'))
    conn.send("You will receive a question.The answer to that of question should be one of a,b,c,d")
    conn.send("Good luck!\n\n\n\n".encode('utf-8'))
    
    def get_random_question_answers(conn):
         random_index=random.randint(0,len(question)-1)
         random_questions=question(random_index)
         random_answer=answers(random_index)
         conn.send(random_questions.encode('utf-8'))
         return random_questions, random_answer, random_index

    index,question,answers= get_random_question_answers(conn)
    while True:
        try:
            message = conn.recv(2048).decode('utf-8')
            if message:
                if message.lower() == answers:
                    score+=1
                    conn.send("Bravo! Your Score is{score}\n\n".encode('utf-8'))
                else:
                    conn.send("Incorrect Answer! Better luck Next Time \n\n".encode('utf-8'))
                    remove_question(index)
                    index,question,answers= get_random_question_answers(conn)  
            else:
                remove(conn)    
        except:
            continue                

def broadcast(message,connection):
    for client in list_of_clients:
        if(client!=connection):
            try:
                client.send(message.encode('utf-8'))
            except:
                remove(client)

def remove_question(index):
    question.pop(index)
    answers.pop(index)

def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)
while True:
    conn = server.accept()
    list_of_clients.append(conn)
    


