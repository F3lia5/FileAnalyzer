#!/usr/bin/env python3
import os

print("------------------------------------------")
print(f"Current working directory: {os.getcwd()}")

files = [f for f in os.listdir() if os.path.isfile(f)]
file_count = len(files)
print(f"Number of files: {file_count}")

file_extensions = [os.path.splitext(file)[1] for file in files]
extension_list = list(set(file_extensions))

print("\n")
print("File extensions:")
for extension in extension_list:
    print(f"({extension}), ", end="")
print("\n")

print("------------------------------------------")
for i in range(file_count):
    print(f"{i + 1}. {files[i]} ({file_extensions[i]})")
