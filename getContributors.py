import requests
import json
import pandas as pd
from collections import defaultdict

# setup owners , access_token, headers and reposName 
access_token='ACCESS TOKEN' 
headers = {'Authorization':"Token "+access_token}
owners = ["freecodecamp", "flutter", "ansible", "kubernetes", "tensorflow", "definitelytyped", "home-assistant"]

reposName = defaultdict(list)
# Loop through all owners 
for owner in owners:
	# Loop through all pages
	date = "2030-06-07T21:32:36Z" # Dummy date for finding earliest date
	for page_num in range(1,100):
		try:
			# to find all the repos' names from each page
			url=f"https://api.github.com/users/{owner}/repos?page={page_num}" 
			repo=requests.get(url,headers=headers).json()		
			if repo == []: 
				break
			# Loop through all repos in the page
			for rep in repo:
				reposName[owner].append(rep["name"])
				# If this repo was created earlier, update date
				if rep["created_at"] < date:
					date = rep["created_at"]
		except:
			None
	# Print created date
	print(f"{owner}: {date}")

# Adding repos that are only one repo and not a whole owner
reposName["microsoft"].append("vscode")
reposName["facebook"].append("react-native")
reposName["microsoftdocs"].append("azure-docs")

# Loop through all owners
for owner in reposName:
	repos = reposName[owner]
	names = []
	counts = []
	# Loop through all repos
	for repo_name in repos:
		print(f"{owner}/{repo_name}")
		# Loop through all pages
		for page_num in range(1,1000):
			try:
				# to find all the repos' contributors from each page
				url = f"https://api.github.com/repos/{owner}/{repo_name}/contributors?page={page_num}&anon=true"
				contributors = requests.get(url,headers=headers).json()		
				# If empty page, break
				if contributors == []: 
					break
				# If its got "documentation_url" something went wrong
				if "documentation_url" in contributors:
					f = open("error.txt", "a")
					f.write(f"{owner}/{repo_name}\n")
					f.close()
					break
				# Loop through all contributors on the page
				for contributor in contributors:
					try:
						# If not anonymous
						if "login" in contributor:
							names.append(contributor['login'])
							counts.append(contributor['contributions'])
						# If anonymous
						elif "name" in contributor:
							names.append(contributor['name'])
							counts.append(contributor['contributions'])	
					except:
						None

			except:
				# Timed out, usually means empty
				f = open("empty.txt", "a")
				f.write(f"{owner}/{repo_name}\n")
				f.close()
				break

	# Make data structure
	mydata=pd.DataFrame()
	mydata['contributor_name']=names
	mydata['counts']=counts
	
	# Remove duplicates and NaN, and sort by counts
	mydata=mydata.groupby('contributor_name')["counts"].sum().reset_index().sort_values(by='counts',ascending=False)
	mydata=mydata.dropna(axis=0).reset_index().drop(columns='index')

	# save
	mydata.to_csv(f"data/{owner}.csv")