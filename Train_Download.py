""" Downloading the Training data """
start = time.time()
for i in range(traincsv.shape[0]):
    link = traincsv.iloc[i]['Link_to_the_image']
    name = (traincsv.iloc[i]['Sub_category'])
    full_name = name+'_'+str(i)+'.jpg'
    img_name = full_name
    full_name = os.path.join(train_dir, img_name)
    if not os.path.exists(full_name):
        try:
            clear_output(wait=True)
            urllib.request.urlretrieve(link, full_name)
            print(colored(img_name+' downloaded', 'green'))
        except:
            clear_output(wait=True)
            print(colored('Link Missing', color='red'))
    else:
        clear_output(wait=True)
        print(img_name,' has already been downloaded')
end = time.time()
print('Time taken to download the training data: ', end-start)