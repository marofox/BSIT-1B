programming_language = ['java','c#','C++','Python','Perl','Go Lang','Javascript']

print(programming_language[-1])

#index                     0     1    2       3       4        5           6  

#keys:    value, keys: value}

proglang_dictionary = {'medjo mahirap':'Java','ok lang':'C#','extremely hard':'c++',\
'ok lang din':'Python','pang matanda':'Perl','bago lang':'go lang',\
'pang web':'JavaScript'}

print(proglang_dictionary['pang matanda'])

#adding item to a dictionary 

proglang_dictionary['pang beginner'] = ['html']

print(proglang_dictionary)

proglang_dictionary.pop('pang matanda')

#proglang_dictionary.pop('keys')