import pandas as pd
import os

directory = "/Users/user/Downloads/Jalpaiguri-Siliguri M Corp"
files = os.listdir(directory)
print(len(files))

for f in files:
	if f.endswith('.xls'):
		full_path = os.path.join(directory, f)
		dfs = pd.read_html(full_path)
		# print(dfs)
		for dff in dfs:
			if "Name" in dff.columns:
				# print("The first name is", dff["Name"])
				if "MANTU GHOSH" in dff["Name"].values:
					print("Yes")
					print(full_path)
				else: print("No")
				
			else: print("No")

	

# import os

# # unpacking the tuple
# file_name, file_extension = os.path.splitext("RCCount_Beneficiary.xls")

# print(file_name)
# print(file_extension)

