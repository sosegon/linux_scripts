'''
    File name: fix_osm_sim_errors.py

    Author: Sebastian Velasquez

    Date created: 2016/07/16

    Date last modified: 2016/07/16

    Python Version: 2.7

    License. The MIT License | https://opensource.org/licenses/MIT

    Description: The purpose of this script is to fix the errors occurred during the
    simulation of osm files

    Usage: In a linux terminal, go to the location of the script
    and type the following: 

    python fix_osm_sim_errors.py /home/user_name/errors.txt /home/user_name/model.osm

    In the command line of windows, type like the following:

    python fix_osm_sim_errors.py "C:\Users\user_name\errors.txt" "C:\Users\user_name\model.osm"
    
    The first argument is the file with the errors and warnings in the model.
    The second argument is the osm file 
    
    The script reads the errors from the corresponding file, finds the source of them
    in the osm file and deletes the entities that are causing such errros.
'''
import sys;

def process_errors_file(errors_file_name, source_file_name):
	errors_array = []

	#collect the errors form errors file
	f = open(errors_file_name, 'r')

	for line in f.readlines():
		if "** Severe  **" in line:
			errors_array.append(line[60:].strip()+",")	

	f.close()
	
	#find the lines where the entities with error start
	indexes_of_entities_to_delete = []
	f = open(source_file_name, 'r')
	counter = 1
	source_lines = f.readlines()
	for line in source_lines:
		if is_line_entity_error(line, errors_array):
			new_index = counter - 2; # entity starts 2 linew before where its name is defined
			indexes_of_entities_to_delete.append(new_index)
		
		counter+=1
			
	indexes_of_entities_to_delete.sort()
	for index in indexes_of_entities_to_delete:
		print "line to delete: " + str(index)
	
	#get the lines without the errors
	no_errors_array = []
	counter = 1
	avoiding = False
	for line in source_lines:
		#if counter in indexes_of_entities_to_delete:
			#print "avoid line: " + str(counter)
		if avoiding is True:
			if "OS:" in line and counter not in indexes_of_entities_to_delete:
				avoiding = False
				no_errors_array.append(line)
				#print "NOT avoiding line: -> " + str(counter)
			#else:
				#print "avoiding line: -> " + str(counter)
		else:
			if counter in indexes_of_entities_to_delete:
				avoiding = True
				#print "avoiding line: -> " + str(counter)
			else:
				no_errors_array.append(line)
				#print "NOT avoiding line: -> " + str(counter)
		
		counter+=1

	#print len(no_errors_array)
	#counter = 1
	# for line in no_errors_array:
		# print str(counter) + ": "+ line
		# counter+=1
	
	f.close()
	
	#create file
	
	#f = open("fixed_" + source_file_name, 'w+');
	f = open(source_file_name, 'w+');
	
	for line in no_errors_array:
		f.write(line)
			

def is_line_entity_error(line, array_of_errors):
	for error in array_of_errors:
		if error in line:
			#if surface_error_in_subsurface_line(error, line):
				#return False;
			return True
			
	return False
	
def surface_error_in_subsurface_line(error, line):
	if "Sub" in line and "Sub" not in error: #subsurface error
		return True
	return False

process_errors_file(sys.argv[1], sys.argv[2])