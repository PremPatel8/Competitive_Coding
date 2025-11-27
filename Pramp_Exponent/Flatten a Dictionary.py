# My Solution
def flatten_dictionary(dictionary):
    resDict = {}

    def flatten(inptDict, currKey, resDict):
        for key, value in inptDict.items():
            if type(value) is str:
                if currKey:
                    if key != '':
                        resDict[currKey+'.'+key] = value
                    else:
                        resDict[currKey] = value
                else:
                    resDict[key] = value
            else:
                if currKey:
                    flatten(value, currKey+'.'+key, resDict)
                else:
                    flatten(value, key, resDict)

                return

    flatten(dictionary, None, resDict)

    return resDict


inpt_dict = {
    "Key1": "1",
    "Key2": {
        "a": "2",
        "b": "3",
        "c": {
            "d": "3",
            "e": {
                "": "1"
            }
        }
    }
}

""" output: {
            "Key1" : "1",
            "Key2.a" : "2",
            "Key2.b" : "3",
            "Key2.c.d" : "3",
            "Key2.c.e" : "1"
        } """


print(flatten_dictionary(inpt_dict))
