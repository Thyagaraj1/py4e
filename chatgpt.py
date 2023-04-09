friends = ["John", "Jane", "Jim", "Joan"]

def happy_new_year(friends_list):
    message = "Happy New Year to "
    for friend in friends_list:
        message += friend + ", "
    message = message[:-2] + "!"
    return message

print(happy_new_year(friends))
