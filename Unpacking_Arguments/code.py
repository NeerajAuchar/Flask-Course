# def named(**kwargs):
#     print (kwargs)


# named(name="neeraj " , age=25)


def named(**Kwargs):
    print(**Kwargs)


details = {"name": "Neeraj", "age ": 25}

named(**details)
