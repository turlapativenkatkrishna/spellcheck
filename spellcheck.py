import sys
import os
import json
import difflib 
import pickle
import spell

pkl_file_path="dictwords.pkl"

def load_pickle_file(pkl_file_path):
    try:
	with open(pkl_file_path, 'rb') as the_file:
		dict_words_list=pickle.load(the_file)
	return dict_words_list
    except Exception as e:
	print str(e)
	print "Exiting spellcheck"
	sys.exit()



def spellcheck(sorted_ip_str, dict_words_list):
	misspelledwords=0
	for word in sorted_ip_str:
		if word not in dict_words_list:
			return word
			misspelledwords+=1
	if misspelledwords==0:
		print "found 0 misspelled words"
		return None
	

def main():
	miss_spelled_words=[]
	input_line=sys.argv[1]
	dict_words_list=load_pickle_file(pkl_file_path)	
	ip_words=input_line.strip().split(' ')
 	uniq_ip_words=set(ip_words)
	sorted_uniq_ip_words=sorted(list(uniq_ip_words))
	miss_spelled_words.append(spellcheck(sorted_uniq_ip_words, dict_words_list))	
	for word in miss_spelled_words:
		print "misspelled word found: " + word + " " + ", possible correct word: " + str(spell.correction(word))
		#print word


if __name__=="__main__":
	main()
