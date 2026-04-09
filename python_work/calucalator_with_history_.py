HISTORY_FILE = "history.txt"


def show_history():
    file = open(history_file,'r')
    lines = file.readlines()
    if len(lines) == 0:
      print("no history found!"):
    else:

     for line in reversed(lines):
        print(line.strip())
    file.close()
    
def clear_history():
    file = open(HISTORY_file,'W')
    file.close()
    print('HISTORY cleared.')
    
def save_TO_history(equation,resulth):
 file = open(history_file, 'a')
 file.write(equation + "=" + str(result)+ "\n")
file.close()
          