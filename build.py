# SSG with Python
import os

# List of Pages to rebuild
PAGES =  ['index.html', 'archive.html', 'sponsor.html', 'team.html']

print("Regenerating Pages...")

# Change Directory to src
os.chdir("src")

# Iterate over the pages and write the reusable components
for page in PAGES:
    print(f"Working on {page}")
    with open('header.html', 'r') as header, \
        open('navbar.html', 'r') as navbar, \
        open(page, 'r') as content, \
        open('footer.html', 'r') as footer, \
        open(f"../{page}", "w") as output:
        output.write(header.read())
        output.write(navbar.read())
        output.write(content.read())
        output.write(footer.read())

# Change Directory
os.chdir("../")

# Success
print("All Done!")

