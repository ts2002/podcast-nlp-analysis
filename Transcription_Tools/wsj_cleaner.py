import re
import glob
import os

files = glob.glob("wsj/finished_trans/*")

# Taking out transcript names
pattern = r'\b[A-Z][a-z]+\s[A-Z][a-z]+:'
for file_path in files:
    with open(file_path, 'r') as file:
        content = file.read()

    modified = re.sub(pattern, '', content)
    print(modified)

    modified = modified.replace("\n", "")
    modified = modified.replace("\r", "")
    with open(file_path, 'w') as file:
        file.write(modified)

days = range(1,25)

for day in days:
    day_str = ''
    if len(str(day)) == 1:
        day_str = '0' + str(day)
    else:
        day_str = str(day)
    MORNING_PATH = 'wsj/finished_trans_raw/03_' + day_str + '_AM.txt'
    NIGHT_PATH = 'wsj/finished_trans_raw/03_' + day_str + '_PM.txt'
    NEW_PATH = 'wsj/finished_trans/3_' + str(day) + ".txt"
    print(MORNING_PATH)
    if os.path.isfile(MORNING_PATH) and os.path.isfile(NIGHT_PATH):
        print('')
        with open(MORNING_PATH, 'r') as file:
            content_morning = file.read()
        with open(NIGHT_PATH, 'r') as file:
            content_evening = file.read()
        

        content_all = content_morning + ' ' + content_evening
        
        if (not os.path.isfile(NEW_PATH)):
            with open(NEW_PATH, 'x') as file:
                file.write(content_all)
    else:
        WK_PATH = 'wsj/finished_trans_raw/03_' + day_str + '_WK.txt'
        with open(WK_PATH, 'r') as file:
            content_all = file.read()
            
        if (not os.path.isfile(NEW_PATH)):
            with open(NEW_PATH, 'x') as file:
                file.write(content_all)
        else:
            with open(NEW_PATH, 'w') as file:
                file.write(content_all)



