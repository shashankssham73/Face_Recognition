import os
path = '/face recognition/xyz/new'
files = os.listdir(path)
i = 163

for filea in files:
    os.rename(os.path.join(path, filea), os.path.join(path, 'User.2.'+str(i)+'.jpg'))
    i = i+1
