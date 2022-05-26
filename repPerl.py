# perl tast
# --*-- encoding: utf-8
import re


def per():
    line = "Cats are smarter than dogs";

    matchObj = re.match(r'dogs', line, re.M | re.I)
    if matchObj:
        print("match --> matchObj.group() : ", matchObj.group())
    else:
        print("No match!!")

    matchObj = re.search(r'dogs', line, re.M | re.I)
    if matchObj:
        print("search --> searchObj.group() : ", matchObj.group())
    else:
        print("No match!!")


if __name__ == '__main__':
    per()
