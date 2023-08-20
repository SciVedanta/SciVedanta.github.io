import glob

x = []
words = []
for i in glob.glob("*/Video*.md"):
    x.append(i)
    f = open(i, "r")
    lines = f.read().splitlines()
    f.close()
    for j in lines:
        for k in j.split():
            words.append(k)
print(words[0:10])
print("Number of videos:", len(x))
print("Number of words:", len(words))
