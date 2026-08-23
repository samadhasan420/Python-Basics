print("\n----- Username Analyzer -----")

UserName = input("\nPlease enter your username: ")
Length = len(UserName)

print("\nusername:", UserName)
print("\nLength:", Length)
print("First character:", UserName[0])
print("Last character:", UserName[-1])
print("First 3 character:", UserName[:3])
print("Last 3 character:", UserName[-3:])