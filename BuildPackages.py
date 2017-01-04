"""
Builds .sublime-package files from the contents of the "Source" folder.

Developed for Python 3.x
"""

import os, zipfile, sys

ROOT = ""
if len(sys.argv) > 1:
	ROOT = sys.argv[1]
else:
	ROOT = os.getcwd()

PACKGE_PREFIX = "The Subliming of Isaac"
PACKAGE_EXTENSION = ".sublime-package"

def main():
	print("Building .sublime-package files...")
	global ROOT
	license_file = os.path.join(ROOT, "LICENSE.md")
	if not os.path.isfile(license_file):
		print("Could not find 'LICENSE.md' in '%s'." % ROOT)
		return
	license_relative_path = os.path.relpath(license_file, os.path.split(license_file)[0])
	readme_file = os.path.join(ROOT, "README.md")
	if not os.path.isfile(readme_file):
		print("Could not find 'README.md' in '%s'." % ROOT)
		return
	readme_relative_path = os.path.relpath(readme_file, os.path.split(readme_file)[0])
	pkg = os.path.join(ROOT, "Packages")
	if not os.path.isdir(pkg):
		os.makedirs(pkg)
	src = os.path.join(ROOT, "Source")
	if not os.path.isdir(src):
		print("There is no 'Source' folder in '%s'." % ROOT)
		return
	if os.path.isdir(src):
		core_files = []
		for root, dirs, files in os.walk(src):
			for file in files:
				core_files.append(os.path.join(root, file))
		with zipfile.ZipFile(os.path.join(pkg, PACKGE_PREFIX+PACKAGE_EXTENSION), "w") as core_zip:
			core_zip.write(license_file, license_relative_path)
			core_zip.write(readme_file, readme_relative_path)
			for file in core_files:
				core_zip.write(file, os.path.relpath(file, os.path.split(file)[0]))
	print("Finished...")
main()