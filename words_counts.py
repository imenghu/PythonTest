def ReadFile():
    '''读取文件名称并判断英文的字符个数'''
    with open(r'files\\wordcounts.txt', 'rt', encoding='utf-8') as f:
        words = f.readlines()
    count = 0
    for wordline in words:
        # for word in wordline.strip().split(" "):
        #     print(word)
        #     count+=1

        temp = wordline.strip().split(" ")
        print(temp)
        count += len(temp)

    print(count)


if __name__ == '__main__':
    ReadFile()


#
# def word_counts(inputfile):
# 	"""
# 	"""
# 	if os.path.isfile(inputfile) != True:
# 		print "inputfile not exists"
# 		sys.exit()
# 	word_count = 0
# 	words = open(inputfile, "r").readlines()
# 	for word in words:
# 		print ("word: %s" %word)
# 		temp = word.strip().split(' ')
# 		word_count += len(temp)
# 	print ("word count:", word_count)
