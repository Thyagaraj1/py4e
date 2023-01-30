#C:\>python
#Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license" for more information.
#>>> help(str.isupper)
#Help on method_descriptor:

#isupper(self, /)
    #Return True if the string is an uppercase string, False otherwise.

    #A string is uppercase if all cased characters in the string are uppercase and
    #there is at least one cased character in the string.

#
def remove_upper(string):
    result=""
    for char in string:
        if not char.isupper():
            result+=char
        return result
string='How you Doing At the Mine'
Output=remove_upper(string)
