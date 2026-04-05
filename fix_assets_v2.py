import os

replacements = [
    ("https://kaladharaa.com/", "/"),
    ("https:\\/\\/kaladharaa.com\\/", "\\/"),
    ("https://kaladharaa.com", ""),
    ("https:\\/\\/kaladharaa.com", "")
]

count = 0
for root, _, files in os.walk('.'):
    for filename in files:
        if filename.endswith(".html"):
            filepath = os.path.join(root, filename)
            with open(filepath, 'r') as f:
                content = f.read()
            original = content
            
            for target, rep in replacements:
                content = content.replace(target, rep)

            if original != content:
                print(f"Fixed URLs in {filepath}")
                with open(filepath, 'w') as f:
                    f.write(content)
                count += 1
print(f"Total files updated: {count}")
