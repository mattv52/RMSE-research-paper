import pandas as pd

# Setup owners
owners = ["freecodecamp", "microsoft", "flutter", "ansible", "kubernetes", "facebook", "tensorflow", "definitelytyped", "home-assistant"]

# Loop through owners
for owner in owners:
	# Load data
	df = pd.read_csv(f'data/{owner}.csv')

	# Get total contributors and contributions
	contributors = df.count()["contributor_name"]
	contributions = df.sum()["counts"]

	# Set up some variables
	top10 = 0
	count = 0
	percent = [0, 0, 0, 0, 0, 0, 0, 0, 0]
	con = [0, 0, 0, 0, 0]

	# Loop through all contributors
	for x in df.index:
		# Add each contributors count
		count += df.loc[x, "counts"]
		
		# If this is 10th contributor (0-9) set top10
		if x == 9:
			top10 = count
		
		# If it hasnt been set and count/contributions is 10% set it, etc..
		if percent[0] == 0 and count/contributions > 0.1:
			percent[0] = x+1
		if percent[1] == 0 and count/contributions > 0.2:
			percent[1] = x+1
		if percent[2] == 0 and count/contributions > 0.3:
			percent[2] = x+1
		if percent[3] == 0 and count/contributions > 0.4:
			percent[3] = x+1
		if percent[4] == 0 and count/contributions > 0.5:
			percent[4] = x+1
		if percent[5] == 0 and count/contributions > 0.6:
			percent[5] = x+1
		if percent[6] == 0 and count/contributions > 0.7:
			percent[6] = x+1
		if percent[7] == 0 and count/contributions > 0.8:
			percent[7] = x+1
		if percent[8] == 0 and count/contributions > 0.9:
			percent[8] = x+1

		# If contributor has 1 or less contributions, add to con. etc..
		if df.loc[x, "counts"] <= 1:
			con[0] += 1
		if df.loc[x, "counts"] <= 2:
			con[1] += 1
		if df.loc[x, "counts"] <= 3:
			con[2] += 1
		if df.loc[x, "counts"] <= 5:
			con[3] += 1
		if df.loc[x, "counts"] <= 10:
			con[4] += 1


	# Print out all Information formatted
	print(f"{owner} & {percent[0]} & {percent[1]} & {percent[2]} & {percent[3]} & {percent[4]} & {percent[5]} & {percent[6]} & {percent[7]} & {percent[8]} \\\\")
	print(f"\tTotal contributors: {contributors}")
	print(f"\tTotal contributions: {contributions}")
	print(f"\tPercentage of contributions by top 10: {(top10/contributions)*100:.2f}")
	print(f"\tNumber of contributors to reach:")
	print(f"\t\t10%: {percent[0]}")
	print(f"\t\t20%: {percent[1]}")
	print(f"\t\t30%: {percent[2]}")
	print(f"\t\t40%: {percent[3]}")
	print(f"\t\t50%: {percent[4]}")
	print(f"\t\t60%: {percent[5]}")
	print(f"\t\t70%: {percent[6]}")
	print(f"\t\t80%: {percent[7]}")
	print(f"\t\t90%: {percent[8]}")
	print(f"\tPercentage of contributors with x or less contributions:")
	print(f"\t\t1: {con[0]/contributors*100:.2f}")
	print(f"\t\t2: {con[1]/contributors*100:.2f}")
	print(f"\t\t3: {con[2]/contributors*100:.2f}")
	print(f"\t\t5: {con[3]/contributors*100:.2f}")
	print(f"\t\t10: {con[4]/contributors*100:.2f}")
	print("\n")

	# Used to generate the top 10 contributor tables
	# print(f"\\begin{{table}}[h]\n\t\\caption{{Top 10 Contributors for {owner}}}\n\t\\label{{tab:{owner}}}\n\t\\begin{{tabular}}{{lc}}")
	# print("\t\t\\toprule\n\t\tContributor &  Contributions\\\\\n\t\t\\midrule")
	# for i in range(0, 10):
	# 	con = df.loc[i, "contributor_name"]
	# 	count = df.loc[i, "counts"]
	# 	print(f"\t\t{con} & {count} \\\\")
	# print(f"\t\t\\midrule\n\t\tTotal from top 10 & {top10} \\\\\n\t\tTotal contributions & {contributions} \\\\")
	# print("\t\t\\bottomrule\n\t\\end{tabular}\n\\end{table}\n")
