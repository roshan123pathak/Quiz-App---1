import time
import random

users = []
quiz_results = []

questions = [
    # DBMS Questions
    {"question": "What does DBMS stand for?", "options": ["Data Base Management System", "Database Management Source", "Data Block Management System", "Data Base Multiple Systems"], "correct": "Data Base Management System"},
    {"question": "Which of the following is a key feature of DBMS?", "options": ["Data Redundancy Control", "Data Storage Management", "Data Integrity", "All of the above"], "correct": "All of the above"},
    {"question": "Which command is used to retrieve data from a database?", "options": ["GET", "SELECT", "FETCH", "QUERY"], "correct": "SELECT"},
    {"question": "Which of the following is NOT a type of DBMS model?", "options": ["Hierarchical Model", "Relational Model", "Object-Oriented Model", "Linear Model"], "correct": "Linear Model"},
    {"question": "What is a primary key in a database?", "options": ["A unique identifier for each record in a table", "A key used to encrypt data", "A key used for indexing", "A key to group similar records"], "correct": "A unique identifier for each record in a table"},
    
    # Cybersecurity Questions
    {"question": "What does the term 'Phishing' refer to?", "options": ["The act of hacking into a computer system", "The use of fraudulent emails to steal sensitive information", "A type of virus that destroys files", "A technique for encrypting passwords"], "correct": "The use of fraudulent emails to steal sensitive information"},
    {"question": "Which of the following is a common method for protecting sensitive data?", "options": ["Encryption", "Password hashing", "Two-factor authentication", "All of the above"], "correct": "All of the above"},
    {"question": "What does the acronym 'DDoS' stand for?", "options": ["Distributed Denial of Service", "Digital Data Online System", "Data Distribution Over Server", "Direct Denial of Service"], "correct": "Distributed Denial of Service"},
    {"question": "Which of the following is a tool used for penetration testing?", "options": ["Wireshark", "Nmap", "Metasploit", "All of the above"], "correct": "All of the above"},
    {"question": "What is the purpose of a firewall in cybersecurity?", "options": ["To detect malware", "To monitor network traffic", "To prevent unauthorized access to a network", "To encrypt sensitive data"], "correct": "To prevent unauthorized access to a network"},
    
    # Network Security Questions
    {"question": "Which of the following is a network security protocol?", "options": ["HTTP", "HTTPS", "FTP", "SNMP"], "correct": "HTTPS"},
    {"question": "What does VPN stand for in network security?", "options": ["Virtual Private Network", "Virtual Protected Network", "Virtual Public Network", "Verified Protection Network"], "correct": "Virtual Private Network"},
    {"question": "Which of the following is a common attack method in network security?", "options": ["Man-in-the-Middle (MITM) attack", "Phishing", "SQL Injection", "All of the above"], "correct": "All of the above"},
    {"question": "What is the purpose of an Intrusion Detection System (IDS)?", "options": ["To monitor and detect malicious network activity", "To prevent unauthorized access to a network", "To block all network traffic", "To provide network access control"], "correct": "To monitor and detect malicious network activity"},
    {"question": "Which protocol is commonly used for securing email communication?", "options": ["HTTP", "POP3", "SMTP", "S/MIME"], "correct": "S/MIME"}
]

def create_account():
    print("\n--- Create Account ---")
    username = input("Choose a username: ")
    password = input("Create a password: ")

    users.append({"username": username, "password": password})
    print("Account created successfully!")

def log_in():
    print("\n--- Log In ---")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    for user in users:
        if user["username"] == username and user["password"] == password:
            print("Login successful!")
            return username
    
    print("Incorrect username or password!")
    return None

def load_quiz_questions():
    random.shuffle(questions) 
    return questions[:5] 

def take_quiz(username):
    print("\n--- Start Quiz ---")
    questions = load_quiz_questions()
    correct_answers = 0
    total_questions = len(questions)
    start_time = time.time()

    for i, q in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {q['question']}")
        for j, option in enumerate(q['options'], start=1):
            print(f"{j}. {option}")
        
        answer = input("Select your answer (1-4): ")
        if q['options'][int(answer) - 1] == q['correct']:
            correct_answers += 1
    
    end_time = time.time()
    time_taken = round(end_time - start_time, 2)
    score = f"{correct_answers}/{total_questions}"

    quiz_results.append({"username": username, "score": score, "time_taken": time_taken})
    
    print(f"\nQuiz complete! Your score: {score}")
    print(f"Time taken: {time_taken} seconds")

def view_results(username):
    print("\n--- Your Results ---")
    found = False
    for result in quiz_results:
        if result["username"] == username:
            print(f"Score: {result['score']}, Time: {result['time_taken']} seconds")
            found = True
    if not found:
        print("No results available!")

def main():
    while True:
        print("\n--- Main Menu ---")
        print("1. Create Account")
        print("2. Log In")
        print("3. Take Quiz")
        print("4. View Results")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            create_account()
        elif choice == '2':
            username = log_in()
            if username:
                while True:
                    print("\n1. Take Quiz")
                    print("2. View Results")
                    print("3. Log Out")
                    sub_choice = input("Select an option: ")
                    if sub_choice == '1':
                        take_quiz(username)
                    elif sub_choice == '2':
                        view_results(username)
                    elif sub_choice == '3':
                        break
                    else:
                        print("Invalid option!")
        elif choice == '5':
            print("Exiting application...")
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
