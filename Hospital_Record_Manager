# Assignment - 2
# Name - Priyanshu
# Roll No - 2020106

import json


'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- DO NOT modify/delete the given functions. 

- DO NOT import any python libraries, except for the ones already included.

- DO NOT create any global variables in this module.

- DO NOT add print statements anywhere in this module.

- Make sure to return value as specified in the function description.

- Remove the pass statement from the functions when you implement them.
'''


def read_data_from_file(file_path="data.json"):
	'''
	**** DO NOT modify this function ****
	Description: Reads the data.json file, and converts it into a dictionary.

	Parameters: 
	- file_path (STRING): The path to the file (with .json extension) which contains the initial database. You can pass the file_path parameter as "data.json".

	Returns:
	- A dictionary containing the data read from the file
	'''
	
	with open(file_path, 'r') as data:
		records = json.load(data)

	return records


def filter_by_first_name(records, first_name):
	'''
	Description: Searches the records to find all persons with the given first name (case-insensitive)

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- first_name (STRING): The first name

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given first name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''
	result=[]
	for i in records:
		if i['first_name'].lower()==first_name.lower():
			result.append(i['id'])
	return result



def filter_by_last_name(records, last_name):
	'''
	Description: Searches the records to find all persons with the given last name (case-insensitive)

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- last_name (STRING): The last name

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given last name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''

	a=[]
	for i in records:
		if i['last_name'].lower()==last_name.lower():
			a.append(i['id'])
	return a


def filter_by_full_name(records, full_name):
	'''
	Description: Searches the records to find all persons with the given full name (case-insensitive)

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- full_name (STRING): The full name (a single string with 2 space-separated words, the first name and the last name respectively)

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given full name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''
	b=[]
	c=full_name.split()
	first_name=c[0]
	last_name=c[1]
	for i in records:
		if i['first_name'].lower()==first_name.lower() and i['last_name'].lower()==last_name.lower():
			b.append(i['id'])
	return b


def filter_by_age_range(records, min_age, max_age):
	'''
	Description: Searches the records to find all persons whose age lies in the given age range [min_age, max_age]

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- min_age (INTEGER): The minimum age (inclusive)
	- max_age (INTEGER): The maximum age (inclusive)

	Note: 0 < min_age <= max_age

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given full name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''
	temp_list=[]
	for i in records:

		if i["age"]>=min_age and i["age"]<=max_age:

			temp_list.append(i['id'])
	return temp_list


def count_by_gender(records):
	'''
	Description: Counts the number of males and females

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)

	Returns:
	- A dictionary with the following two key-value pairs:
		KEY        VALUE
		"male"     No of males (INTEGER)
		"female"   No of females (INTEGER)
	'''
	count_male=0
	count_female=0

	for i in records:
		if i['gender']=='male':
			count_male+=1
		elif i['gender']=='female':
			count_female+=1
	dic = {"male": count_male, "female": count_female}
	return dic


def filter_by_address(records, address):
	'''
	Description: Filters the person records whose address matches the given address. 

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- address (DICTIONARY): The keys are a subset of { "house_no", "block", "town", "city", "state", "pincode" } (case-insensitive)
		Some examples are:
			Case 1: {} 
				=> All records match this case
			
			Case 2:
				=> All records where the block is "AD" and the city is "Delhi" (the remaining address fields can be anything)
			
			Case 3: { "house_no": 24, "block": "ABC", "town": "Vaishali", "city": "Ghaziabad", "state": "Uttar Pradesh", "pincode": 110020 }

	Returns:
	- A LIST of DICTIONARIES with the following two key-value pairs:
		KEY            VALUE
		"first_name"   first name (STRING)
		"last_name"    last name (STRING)
	'''
	result=[]


	if len(address)==0:	# for case 1
		for i in range(len(records)):
			result.append({'first_name': records[i]['first_name'], 'last_name': records[i]['last_name']})
	else:
		for i in range(len(records)):
			flag=True
			for k in address:
				if str(records[i]['address'][k]).lower() == str(address[k]).lower():
					flag=False
				else:
					flag=True
					break
			if flag==False:
				result.append({'first_name': records[i]['first_name'], 'last_name': records[i]['last_name']})
	return result


def find_alumni(records, institute_name):
	'''
	Description: Find all the alumni of the given institute name (case-insensitive). 
	
	Note: A person is an alumnus of an institute only if the value of the "ongoing" field for that particular institute is False.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- institute_name (STRING): Name of the institute (case-insensitive)

	Returns:
	- A LIST of DICTIONARIES with the following three key-value pairs:
		KEY            VALUE
		"first_name"   first name (STRING)
		"last_name"    last name (STRING)
		"percentage"   percentage (FLOAT)
	'''
	result = []
	for i in records:
		temp = i['education']
		for j in temp:
			if institute_name.lower() == j['institute'].lower() and (j['ongoing'] == False):
				result.append({'first_name':i['first_name'], 'last_name':i['last_name'], 'percentage':j['percentage']})

	return result


def find_topper_of_each_institute(records):
	'''
	Description: Find topper of each institute

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)

	Returns:
	- A DICTIONARY with the institute name (STRING) as the keys and the ID (INTEGER) of the topper of that institute.

	Note: If there are `N` distinct institutes in records, the dictionary will contain `N` key-value pairs. The ongoing status does NOT matter. It is guaranteed that each institute will have exactly one topper.
	'''
	my_dic={}
	temp_dic={}
	for i in records:
		temp=i['education']
		for j in temp:
			temp1=j['ongoing']
			if temp1==False:
				temp2=j['institute']
				if temp2 not in temp_dic:
					temp3 = j['percentage']
					temp_dic[temp2]=temp3
					my_dic[temp2]=i['id']
				else:
					temp4= temp_dic[temp2]
					if j['percentage'] > temp4:
						temp_dic[temp2] = j['percentage']
						my_dic[temp2] = i['id']
	return my_dic


def find_blood_donors(records, receiver_person_id):
	'''
	Description: Find all donors who can donate blood to the person with the given receiver ID.

		Note:
		- Possible blood groups are "A", "B", "AB" and "O".

		Rules:
		BLOOD GROUP      CAN DONATE TO
		A                A, AB
		B                B, AB
		AB               AB
		O                A, B, AB, O

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- receiver_person_id (INTEGER): The ID of the donee
		Note: It is guaranteed that exactly one person in records will have the ID as receiver_person_id

	Returns:
	- A DICTIONARY with keys as the IDs of potential donors and values as a list of strings, denoting the contact numbers of the donor
	'''
	my_dic={}


	for i in range(len(records)):
		if i!=receiver_person_id:
			if records[receiver_person_id]['blood_group']=="A":
				if records[i]['blood_group']=="A" or records[i]['blood_group']=="O":
					my_dic[records[i]['id']]=records[i]['contacts']
			elif records[receiver_person_id]['blood_group']=="B":
				if records[i]['blood_group']=="B" or records[i]['blood_group']=="O":
					my_dic[records[i]['id']]=records[i]['contacts']
			elif records[receiver_person_id]['blood_group']=="AB":
				if records[i]['blood_group']=="A" or records[i]['blood_group']=="B" or records[i]['blood_group']=="O" or records[i]['blood_group']=="AB":
					my_dic[records[i]['id']]=records[i]['contacts']
			elif records[receiver_person_id]['blood_group'] == "O":
				if records[i]['blood_group'] == "O":
					my_dic[records[i]['id']] = records[i]['contacts']
	return my_dic

def get_common_friends(records, list_of_ids):
	'''
	Description: Find the common friends of all the people with the given IDs

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- list_of_ids (LIST): A list of IDs (INTEGER) of all the people whose common friends are to be found

	Returns:
	- A LIST of INTEGERS containing the IDs of all the common friends of the specified list of people
	'''
	temp_list1=[]
	temp_list2=[]
	result=[]
	for i in range(len(records)):
		for j in range(len(list_of_ids)):
			if records[i]['id']==list_of_ids[j]:
				temp_list1.extend(records[i]['friend_ids'])
	temp_list2=[]
	for k in temp_list1:
		if k not in temp_list2:
			temp_list2.append(k)
	for l in temp_list2:
		counter=temp_list1.count(l)
		if counter==len(list_of_ids):
			result.append(l)
	return result


def is_related(records, person_id_1, person_id_2):
	'''
	**** BONUS QUESTION ****
	Description: Check if 2 persons are friends

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id_1 (INTEGER): first person ID
	- person_id_2 (INTEGER): second person ID

	Returns:
	- A BOOLEAN denoting if the persons are friends of each other, directly or indirectly (if A knows B, B knows C and C knows D, then A knows B, C and D).
	'''
	temp_list=[]

	for i in range(len(records)):		#stores all the id's of friend of person 1 in a temporary list
		if person_id_1 == records[i]['id']:
			temp_list=records[i]['friend_ids']
	for j in range(len(records)):		#stores all the id's of friend's of all the people who are in temporary list
		for k in temp_list:
			if k==records[j]['id']:
				temp_list.extend(records[j]['friend_ids'])

	if person_id_2 in temp_list:		#checks if person 2 is friend of person 1 directly or indirectly
		flag=True
	else:
		flag = False
	return flag

def delete_by_id(records, person_id):
	'''
	Description: Given a person ID, this function deletes them from the records. Note that the given person can also be a friend of any other person(s), so also delete the given person ID from other persons friend list. If the person ID is not available in the records, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	
	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	'''
	if  person_id<len(records):
		for i in range(len(records)):
			if (person_id in records[i]["friend_ids"]):
				records[i]["friend_ids"].remove(person_id)
		for j in records:
			if (j["id"] == person_id):
				records.remove(j)
	return records
def add_friend(records, person_id, friend_id):
	'''
	Description: Given a person ID and a friend ID, this function makes them friends of each other. If any of the IDs are not available, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	- friend_id (INTEGER): The friend id
	
	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	'''
	if person_id<len(records):
		if friend_id<len(records):
			if person_id not in records[friend_id]['friend_ids']:
				records[friend_id]['friend_ids'].append(person_id)
				records[friend_id]['friend_ids'].sort()
				records[person_id]['friend_ids'].append(friend_id)
				records[person_id]['friend_ids'].sort()


	return records

def remove_friend(records, person_id, friend_id):
	'''
	Description: Given a person ID and a friend ID, this function removes them as friends of each other. If any of the IDs are not available, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	- friend_id (INTEGER): The friend id
	
	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	'''
	if person_id<len(records):
		if friend_id<len(records):
			if person_id in records[friend_id]['friend_ids']:
				records[friend_id]['friend_ids'].remove(person_id)
				records[friend_id]['friend_ids'].sort()
				records[person_id]['friend_ids'].remove(friend_id)
				records[person_id]['friend_ids'].sort()
	return records

def add_education(records, person_id, institute_name, ongoing, percentage):
	'''
	Description: Adds an education record for the person with the given person ID. The education record constitutes of insitute name, the person's percentage and if that education is currently ongoing or not. Please look at the format of an education field from the PDF. If the person ID is not available in the records, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	- institute_name (STRING): The institute name (case-insensitive)
	- ongoing (BOOLEAN): The ongoing value representing if the education is currently ongoing or not
	- percentage (FLOAT): The person's score in percentage

	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	'''
	if person_id<len(records):
		for i in range(len(records)):
			if records[i]['id'] == person_id:
				my_dic={}
				my_dic['institute'] = institute_name
				my_dic['ongoing'] = ongoing
				if ongoing == False:
					my_dic['percentage'] = percentage
				records[i]['education'].append(my_dic)
	return records


