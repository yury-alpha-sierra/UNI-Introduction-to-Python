
import datetime as dt

now = dt.datetime.now()
file_name = now.strftime("%Y-%m-%d-%H-%M-%S")
file_name = 'invoice ' + file_name + '.txt'
with open(str(file_name), 'w') as invoice_file:
    pass
