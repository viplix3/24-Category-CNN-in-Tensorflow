""" Downloading the Testing data """
import time
import os
import pandas as pd  # For manipulating CSV files
import urllib.request
from IPython.display import clear_output
from termcolor import colored


testcsv = pd.read_csv('myntra_test.csv')


start = time.time()
for i in range(testcsv.shape[0]):
    link = testcsv.iloc[i]['Link_to_the_image']
    name = str(i)+'.jpg'
    full_name = os.path.join('Test', name)
    if not os.path.exists(full_name):
        try:
            clear_output(wait=True)
            urllib.request.urlretrieve(link, full_name)
            print(colored(name+' downloaded', 'green'))
        except:
            clear_output(wait=True)
            print(colored('Link Missing', color='red'))
    else:
        clear_output(wait=True)
        print(name, ' has already been downloaded')
end = time.time()
print('Time taken to download the testing data: ', end-start)
