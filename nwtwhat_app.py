from Question import Question

question_prompt= [
"If an Ethernet port on a router were assigned an IP address of 21.121.54.71/15, which host address would be able to communicate with it? \n (a) 166.121.177.233 \n (b) 95.199.103.46 \n (c) 21.121.241.69 \n (d) 244.28.220.100 \n (e) 198.58.153.142 \n (f) 79.46.141.190 \n (g) 167.232.175.162\n\n",
"Which of the following services use UDP? 1. DHCP  2. SMTP  3. FTP  4. HTTP \n (a) 3 \n (b) 1 \n (c) All of the above \n (d) 2 \n\n",
"Which of the following is the valid host range for the subnet on which the IP address 120.2.67.128/15 resides \n (a) 120.2.0.1-120.3.255.251 \n (b) 120.2.0.2-120.3.255.254 \n (c) 120.2.0.1-120.3.255.253 \n (d) 120.2.0.1-120.4.0.3\n\n",
"DHCP is used for \n (a) Both IPV6 and IPV4 \n (b) None of the mentioned \n (c) IPv4 \n (d) IPv6 \n\n",
"How long is an IPv4 address?  \n (a) 64 bits \n (b) 128 bits \n (c) 128 bytes \n (d) 32 bits \n\n",
"How long is an IPv4 address?  \n (a) 64 bits \n (b) 128 bits \n (c) 128 bytes \n (d) 32 bits \n\n"

]

questions = [
	Question(question_prompt[0], "c"),
	Question(question_prompt[1], "b"),
	Question(question_prompt[2], "b"),
	Question(question_prompt[3], "a")
	Question(question_prompt[4], "d")
]

def run_test(questions):
	score = 0
	for question in questions:
		answer = input(question.prompt)
		if answer == question.answer:
			score += 1
	print ("You got " + str(score) + "/" + str(len(questions)) + "Correct")

run_test(questions)
