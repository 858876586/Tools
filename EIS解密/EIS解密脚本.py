import os,sys

def Creat_newfile(filename, newfilepath):
    if not os.path.isdir(os.path.dirname(newfilepath)):
        os.makedirs(os.path.dirname(newfilepath))
        
    with open(newfilepath,"wb") as file_in:
        with open(filename, "rb") as file_out:
            file_in.write( file_out.read() )


def list_dir(fdir):
    for lists in os.listdir(fdir):
        path = os.path.join(fdir, lists)
        if os.path.isfile(path):
            file_list.append(path)
        if os.path.isdir(path):
            list_dir(path)


if __name__ == "__main__":
    os.chdir(os.path.dirname(sys.argv[0]))
    
    while True:
        file_list = list()
        
        fdir = input('please input the path or filename:')

        #change to abs path
        if not os.path.isabs(fdir):
            fdir = os.path.abspath(fdir)

        parent_path = os.path.dirname(fdir)
        newpath_pre = os.path.join(parent_path,'__jiemi')

        if os.path.isfile(fdir):
            file_list.append(fdir)
        elif os.path.isdir(fdir):
            list_dir(fdir)
        else:
            print("Please make sure the file exists!")
            continue

        for file in file_list:
            newpath_post = file.split(parent_path)[1]
            newfilepath = newpath_pre + newpath_post
            Creat_newfile(file, newfilepath)
            print(newfilepath + " is OK.")
            



            
