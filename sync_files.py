from Utils.github import sync_github_folder


def sync_files():
	sync_github_folder("xivapi", "ffxiv-datamining-patches", "patchlist.json", "patchlist.json", "master", None)
	sync_github_folder("xivapi", "ffxiv-datamining", "csv", "./csv", "master", None)
	sync_github_folder("xivapi", "ffxiv-datamining-patches", "patchdata", "./patchdata", "master", None)


if __name__ == "__main__":
	sync_files()