hashtable = [[] for _ in range(10)]
def display_hash(hashtable):
    for i in range(len(hashtable)):
        print (i,end="")
        for j in hashtable[i]:
            print("__>",end=" ")
            print (j,end=" ")
        print()
def hashing (keyvalue):
    return keyvalue%len(hashtable)
def insert(hashtable, keyvalue,value):
    hash_key=hashing(keyvalue)
    hashtable[hash_key].append(value)
insert(hashtable,10,'Apple')
insert(hashtable,25,'mango')
insert(hashtable,20,'kiwi')
insert(hashtable,9,'chickoo')
insert(hashtable,21,'lime')
insert(hashtable,21,'cherry')
display_hash(hashtable)
                              
