import pandas as pd

# Setup owners and extra to clear
owners = ["freecodecamp", "flutter", "ansible", "kubernetes", "tensorflow", "definitelytyped", "home-assistant", "microsoft", "facebook"]
extra = ["skia-flutter-autoroll", "engine-flutter-autoroll", "Kubernetes Submit Queue", "tensorflower-gardener", "Copybara-Service", "tfx-copybara", "A. Unique TensorFlower"]

# Loop through owners
for owner in owners:
	# Read data and drop extra column
	df = pd.read_csv(f'data/{owner}.csv')	
	df.drop(inplace = True, columns = 'Unnamed: 0')

	# Loop through all contributors
	for x in df.index:
		# If name has -bot, [bot] or -robot, drop it
		if "-bot" in df.loc[x, "contributor_name"] or "[bot]" in df.loc[x, "contributor_name"] or "-robot" in df.loc[x, "contributor_name"]:
			df.drop(x, inplace = True)
		# If name is in the list of extra ones to clear, drop it
		if df.loc[x, "contributor_name"] in extra:
			df.drop(x, inplace = True)
	
	# Reset the index and drop extra index column
	df=df.reset_index()
	df.drop(inplace = True,columns = 'index')

	# Save data
	df.to_csv(f"data/{owner}.csv")