from functions.get_files_info import get_files_info


print ('Result for current directory:')
result = get_files_info("calculator", ".")
print("  " + result.replace("\n", "\n  "))

print ("Result for '/bin' directory:")
result = get_files_info("calculator", "/bin")
print("  " + result.replace("\n", "\n  "))
print ("Result for '../' directory:")
result = get_files_info("calculator", "../")
print("  " + result.replace("\n", "\n  "))
print ("Result for 'pkg' directory:")
result = get_files_info("calculator", "pkg")
print("  " + result.replace("\n", "\n  "))
