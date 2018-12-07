#!/usr/bin/env python3
#
# Name: Duy Hoang
# Id: dqh23
# Assignment 3
# December 3, 2018	
#
#

import datetime
import re
import operator
import sys
import os
FILEPATH="sample.log"
tmp_filepath="tmp"
class Transaction:
	def __init__(self, trans_type, amount, time):
		self.time = time
		self.trans_type = trans_type
		if trans_type.lower() in ["dw"]:
			self.trans_type = trans_type.upper()
		self.amount = amount
		


	def getAmount(self):
		return float(self.amount)

	def getTransactionType(self):
		return self.trans_type

	def getLogString(self):
		trans_type_str = ""
		if self.trans_type == "D":
			trans_type_str = "deposit"
		else:
			trans_type_str = "withdrawal"
		log = "%s %s $%s" %(self.time, \
									trans_type_str, str(self.amount))
		return log

class Account:
	def __init__(self, num, name):
		self.__num = num
		self.__name = name
		self.__transactions = []
		self.__balance = 0

	def getName(self):
		return self.__name

	def getAccountNumber(self):
		return self.__num

	def addTransaction(self, transaction):
		self.__transactions.append(transaction)
		if transaction.trans_type== "W":
			self.__balance -= transaction.getAmount()
		else:
			self.__balance += transaction.getAmount()

	def getBalance(self):
		return self.__balance

	def getHistory(self):
		formatted_str = ""
		for transaction in self.__transactions:
			formatted_str+= "\t" + transaction.getLogString() + "\n"
		return formatted_str

	def __lt__(self, other):
		if self.__name <= other.__name:
			return True
		return False

	def __str__(self):
		string = "\taccount #:  %s\n\t     name:  %s\n\t  balance:  $%s\n" %(self.__num, self.__name, self.__balance)
		return string




def readInFileAndUpdateAccounts(filepath=FILEPATH):
	acct_num_dict = dict()
	acct_list = list()
	acct_num_reg = re.compile("(\d{4}):")
	acct_name_reg = re.compile(":(\w+\s*\w*):")
	trans_time_reg = re.compile(":(\d{2}\.\d{2}\.\d{2}):")
	trans_type_reg = re.compile(":(\w{1}):")
	trans_amount_reg = re.compile(":(\d+\.*\d*$)")
	f = open(filepath, "r")
	for line in f.readlines():
		if len(line.strip()):
			acct_num = re.search(acct_num_reg, line)[1]
			acct_name = re.search(acct_name_reg, line)[1]
			trans_time = re.search(trans_time_reg, line)[1]
			trans_type = re.search(trans_type_reg, line)[1]
			trans_amount = re.search(trans_amount_reg, line)[1]

			acct_num = int(acct_num)
			if acct_num not in acct_num_dict:
				newAccount = Account(acct_num, acct_name)
				acct_num_dict[acct_num] = newAccount

			newTransaction = Transaction(trans_type, trans_amount, trans_time)
			acct_num_dict[acct_num].addTransaction(newTransaction)

	acct_list = sorted(acct_num_dict.values())
	f.close()
	return (acct_list, acct_num_dict)

def showAccountList(mode):
	if mode == "info":
		print("Info\n----")
	elif mode == "history":
		print("History\n-------")
	elif mode == "transaction":
		print("Transaction\n----------")
	acct_list, acct_num_dict = readInFileAndUpdateAccounts(FILEPATH)
	for order, acct in enumerate(acct_list):
		acct_name = acct.getName()
		acct_num = acct.getAccountNumber()
		returned_line = "%d) %s %s" %(order+1, acct_name, acct_num)
		print(returned_line)
	if mode == "transaction":
		print("c)reate new account")
	print("q)uit")


def runInfoMode():
	while True:
		acct_list, acct_num_dict = readInFileAndUpdateAccounts(FILEPATH)
		showAccountList("info")
		usr_input = input("Enter choice => ")
		if usr_input == "q":
			break
		try:
			usr_input = int(usr_input)
			if (usr_input < len(acct_list) + 1):
				print(acct_list[usr_input-1])
				continue
			else:
				raise ValueError("Input out of range")
		except Exception as e:
			print(e)
			continue

def runHistoryMode():
	while True:
		acct_list, acct_num_dict = readInFileAndUpdateAccounts(FILEPATH)
		showAccountList("history")
		usr_input = input("Enter choice => ")
		if usr_input == "q":
			break
		try:
			usr_input = int(usr_input)
			if (usr_input < len(acct_list) + 1):
				print(acct_list[usr_input-1].getHistory())
				continue
			elif usr_input == "q":
				break
			else:
				raise ValueError("Input out of range")
		except Exception as e:
			print(e)
			continue

def promptValidAmount(prompt):
	while True:
		amount = input(prompt)
		try:
			amount = float(amount)
			return amount
		except Exception as e:
			print(e)
			continue

def promptValidTransType(prompt):
	while True:
		trans_type = input(prompt)
		if (trans_type in "wdWD") and (len(trans_type) == 1):
			return trans_type.upper()
		continue

def promptValidAccountNumber(prompt):
	_, acct_num_dict = readInFileAndUpdateAccounts(FILEPATH)
	while True:
		acct_num = input(prompt)
		if len(acct_num) != 4:
			print("Required length: 4 digits")
			continue
		try:
			acct_num = int(acct_num)
			if acct_num in acct_num_dict:
				print("Account number already exists")
				continue
			return acct_num
		except Exception as e:
			print(e)
			continue

def runTransactionMode():
	formatted_time = datetime.datetime.today().strftime("%y.%m.%d")

	while True:
		tmp = open(tmp_filepath, "a");
		acct_list, acct_num_dict = readInFileAndUpdateAccounts(FILEPATH)
		showAccountList("transaction")
		usr_input = input("Enter choice => ")
		if usr_input == "q":
			tmp.close()
			with open("tmp", "r") as tmp, open(FILEPATH, "a") as f:
				line = tmp.readline()
				f.write("\n")
				while line:
					f.write(line)
					line = tmp.readline()
			os.remove(tmp_filepath)
			break
		elif usr_input == "c":
			new_acct_name = input("Enter account holder's name: ")
			new_acct_num = promptValidAccountNumber("Enter account number: ")
			transaction_amount = promptValidAmount("Enter the amount of first deposit: ")

			log = "%s:%s:%s:%s:%d" %(new_acct_num, new_acct_name,
											formatted_time, "D", transaction_amount)
			tmp.write(log)
			tmp.write("\n")
			tmp.close()
			print("Account created successful!")
			with open("tmp", "r") as tmp, open(FILEPATH, "a") as f:
				f.write("\n")
				line = tmp.readline()
				while line:
					f.write(line)
					line = tmp.readline()
			os.remove(tmp_filepath)
			continue

		try:
			usr_input = int(usr_input)
			if (usr_input < len(acct_list) + 1):
				account = acct_list[usr_input-1]

				trans_type = promptValidTransType("Transaction type (w/d):")
				amount = promptValidAmount("Amount:")
				if (trans_type == "W") and (amount > account.getBalance()):
					print("Transaction failed. Not enough money in account")
					continue

				newTransaction = Transaction(trans_type, amount, formatted_time)
				account.addTransaction(newTransaction)
				log = "%s:%s:%s:%s:%d" %(account.getAccountNumber(), account.getName(),
											formatted_time, trans_type, amount)
				print("Transaction successful!")
				tmp.write(log)
				tmp.write("\n")
				tmp.close()
				continue
			else:
				raise ValueError("Input out of range")
		except Exception as e:
			print(e)
			continue

def showUsage():
	usage= "-i -- Account info\n-h -- History\n-t -- Insert transaction\n-? -- Show usage msg \n"
	print(usage)
if __name__ == "__main__":
	print("DEBUGGING")
	readInFileAndUpdateAccounts()
	if not os.environ.get("ACCT_LIST"):
		print("No environment variable 'ACCT_LIST' provided")
		exit(-1)
	if len(sys.argv) < 2:
		print("Not enough arguments")
	else:
		if sys.argv[1] == "-i":
			runInfoMode()
		elif sys.argv[1] == "-h":
			runHistoryMode()
		elif sys.argv[1] == "-t":
			runTransactionMode()
		elif sys.argv[1] == "-?":
			showUsage()

