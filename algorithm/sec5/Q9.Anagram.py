#[#Q9.Anagram(아나그램)]

def word_counts(inputs, dictionary):
    for x in inputs:
        if x in dictionary:
            dictionary[x] += 1
        else:
            dictionary[x] = 1
    return dictionary

for i in range(2):
    word_dict = dict()
    globals()["w{}".format(i+1)] = word_counts(input(), word_dict)
    
if w1==w2:
    print("YES")
else:
    print("NO")
    