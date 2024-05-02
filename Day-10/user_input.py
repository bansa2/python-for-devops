import os

def fld_err_lst(fldt):
    try:
        lst = os.listdir(fldt)
        return lst,None
    except FileNotFoundError:
        return None, "Folder not found"
    except PermissionError:
        return None, "Permission denied"



def main():
    try:
        flno = int(input("Please enter no of folder you want to get details "))
        print(flno)

        for i in range(flno):
            fldt = input("Enter folder name")
            print(fldt)

            lst,error_message = fld_err_lst(fldt)
            if lst:
                print("Files in Folder",fldt)
                for i in lst:
                    print(i)
            else:
                print(f"Please enter correct folder name {fldt}: {error_message}")    

    except ValueError:
        print("")

if __name__ == "__main__":
    main()