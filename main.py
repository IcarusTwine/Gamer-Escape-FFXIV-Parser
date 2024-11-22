from Utils.github import sync_github_folder

sync_github_folder("xivapi", "ffxiv-datamining-patches", "patchlist.json", "patchlist.json", "master", None)
sync_github_folder("xivapi", "ffxiv-datamining", "csv", "./csv", "master", None)
sync_github_folder("xivapi", "ffxiv-datamining-patches", "patchdata", "./patchdata", "master", None)