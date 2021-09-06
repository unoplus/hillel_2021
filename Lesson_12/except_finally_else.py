# Create by Bender

# обращение к несуществующему и существующему файлам по очереди
for file_name in ["some_file_which_not_exists", "file_exists.txt"]:
    try:
        print(f"Read file: '{file_name}'")
        fid = open(file_name, "r")
    except FileNotFoundError as e:
        print(f"There is no such file: {e}")
    else:
        # Execute some actions with files if file exists
        print(f"Done work with file '{file_name}'")
        fid.close()
    finally:
        print("Execute part from finally")
