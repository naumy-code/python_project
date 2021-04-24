import json

if __name__ == '__main__':
    """
        python中的json的处理
    """

    jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';

    text = json.loads(jsonData)
    print(text)

    stra = "1"
    strb = "2"
    print(stra.update(strb))
