def reverseInParentheses(inputString):
    output=[]
    for i in inputString:
        if i == ")":
            tmp=""
            while output[-1] != "(":
                tmp += output.pop()
            output.pop()
            for item in tmp:
                output.append(item)
        else:
            output.append(i)
    return "".join(output)
