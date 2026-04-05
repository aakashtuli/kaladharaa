import os

target = "https://kaladharaa.com/"
replacement = "/"

count = 0
for root, _, files in os.walk('.'):
    for filename in files:
        if filename.endswith(".html"):
            filepath = os.path.join(root, filename)
            with open(filepath, 'r') as f:
                content = f.read()
            original = content
            # Replace absolute URLs with root-relative paths
            content = content.replace(target, replacement)
            # Also catch ones without the trailing slash just in case
            content = content.replace("https://kaladharaa.com", "")

            if original != content:
                print(f"Fixed absolute URLs in {filepath}")
                with open(filepath, 'w') as f:
                    f.write(content)
                count += 1
print(f"Total files updated: {count}")
