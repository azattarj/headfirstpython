import time
today = time.strftime("%A")
condition = 'Headache'
if today == 'Saturday':
    print('Party!!')
elif today == 'Sunday':
    if condition == 'Headache':
        print('Recover, then rest.')
    else:
        print('Rest')
else:
    print('Work, work, work.')
