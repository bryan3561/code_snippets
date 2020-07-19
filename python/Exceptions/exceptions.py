"""
try: The code with the exception that you want to catch
except: This code is executed only if an exception was raised in the try block
else: This code is executed only if no exceptions were raised in the try block
finally: This code always executes after the other blocks
raise("Exception"): It's used for raising your own errors
"""

try:
    f = open('curruptfile.txt')
    # if f.name == 'currupt_file.txt':
    #     raise Exception("message")
except IOError as e:
    print('First!')
except Exception as e:
    print('Second')
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")

print('End of program')
