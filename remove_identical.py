import os
import hashlib


def calculate_sha1(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
        sha1 = hashlib.sha1(data).hexdigest()
    return sha1


def delete_duplicates(directory):
    jpg_count = 0
    duplicate_count = 0
    file_sha1s = {}
    for filename in os.listdir(directory):
        jpg_count += 1
        if filename.endswith('.jpg'):
            file_path = os.path.join(directory, filename)
            sha1 = calculate_sha1(file_path)
            if sha1 in file_sha1s:
                duplicate_count += 1
                print(f'deleting duplicate file: {file_path}')
                os.remove(file_path)
            else:
                file_sha1s[sha1] = file_path
    print(f"total: {jpg_count}\nduplicates: {duplicate_count} ({duplicate_count / jpg_count * 100:.3f}%)")
