def readNumber(line, index):
  number = 0
  while index < len(line) and line[index].isdigit():
    number = number * 10 + int(line[index])
    index += 1
  if index < len(line) and line[index] == '.':
    index += 1
    keta = 0.1
    while index < len(line) and line[index].isdigit():
      number += int(line[index]) * keta
      keta /= 10
      index += 1
  token = {'type': 'NUMBER', 'number': number}
  return token, index


def readPlus(line, index):
  token = {'type': 'PLUS'}
  return token, index + 1

def readMinus(line, index):
  token = {'type': 'MINUS'}
  return token, index + 1

def readMul(line, index):
  token = {'type': 'MUL'}
  return token, index + 1

def readDiv(line, index):
  token = {'type': 'DIV'}
  return token, index + 1

def readOpen(line, index):
  token = {'type': 'OPEN'}
  return token, index + 1

def readClose(line, index):
  token = {'type': 'CLOSE'}
  return token, index + 1

def tokenize(line):
  tokens = []
  index = 0
  while index < len(line):
    if line[index].isdigit():
      (token, index) = readNumber(line, index)
    elif line[index] == '+':
      (token, index) = readPlus(line, index)
    elif line[index] == '-':
      (token, index) = readMinus(line, index)
    elif line[index] == '*':
      (token, index) = readMul(line, index)
    elif line[index] == '/':
      (token, index) = readDiv(line, index)
    elif line[index] == '(':
      (token, index) = readOpen(line, index)
    elif line[index] == ')':
      (token, index) = readClose(line, index)
    else:
      print('Invalid character found: ' + line[index])
      exit(1)
    tokens.append(token)
  return tokens

#calcMulDiv is only referenced from calcAddSub and index with type 'number' or 'open' is given.
#calculate * / until you reach + - or ) or the end of token.
#when ( is found it calls calcParenthesis.
#returns calculated value and the index after next + -, or the last index of token.
def calcMulDiv(tokens, index):
  print("-----calcMD", index)
  print(tokens)
  tokens.insert(index, {'type': 'MUL'})
  print(tokens)
  answer = 1
  i = index
  while i<len(tokens):
    print("tokens",i,tokens[i])
    if tokens[i]['type'] == 'NUMBER':   # when num is found
      if tokens[i - 1]['type'] == 'MUL':
        answer *= tokens[i]['number']
        print("* answer",answer)
        i += 1
      elif tokens[i - 1]['type'] == 'DIV':
        answer /= tokens[i]['number']
        print("/ answer",answer)
        i += 1
      else:
        print('Invalid syntax')
        exit(1)
    elif tokens[i]['type'] == 'OPEN':    # when ( is found
      print("( found")
      if tokens[i - 1]['type'] == 'MUL':
        ans, i = calcParenthesis(tokens,i)
        answer *= ans
        i += 1
        print("* answer P",answer)
      elif tokens[i - 1]['type'] == 'DIV':
        ans, i = calcParenthesis(tokens,i)
        answer /= ans
        i += 1
        print("/ answer P",answer)
      else:
        print('Invalid syntax')
        exit(1)
    elif tokens[i]['type'] == 'PLUS' or tokens[i]['type'] == 'MINUS':   #when + - is found
        print("+- found")
        print("-----returnMD",answer)
        return answer, i
    elif tokens[i]['type'] == 'CLOSE':   #when ) is found
      print("-----returnMD", i, answer)
      return answer, i
    else:
      print("else")
      i += 1
  print(i)
  print("-----returnMD",answer)
  return answer, i

#calculate formula consisting of + -
#returns calculated value and the last index
#index with type 'number' or 'open' is given
def calcAddSub(tokens, index):
  print("-----calcAS", index)
  answer = 0
  i = index
  while i<len(tokens):
    print("tokens=",i, tokens[i])
    if tokens[i]['type'] == 'NUMBER' or tokens[i]['type'] == 'OPEN':     # when num is found
      print("num found")
      if i==0 or tokens[i - 1]['type'] == 'PLUS' or tokens[i - 1]['type'] == 'OPEN':
        ans, i = calcMulDiv(tokens, i)     #call calcMulDiv and add
        answer += ans
        print("+ answer",answer)
        print(tokens)
      elif tokens[i - 1]['type'] == 'MINUS':
        ans, i = calcMulDiv(tokens, i)
        answer -= ans
        print("- answer",answer)
      else:
        print('Invalid syntax')
        exit(1)
    #elif tokens[i]['type'] == 'OPEN':        #when ( is found
    #  if tokens[i - 1]['type'] == 'PLUS' or tokens[i - 1]['type'] == 'OPEN':
    #    ans, i = calcParenthesis(tokens,i)    #call calcParenthesis and add
    #    answer += ans
    #    i += 1
    #    print("+ answer P ",answer)
    #  elif tokens[i - 1]['type'] == 'MINUS':
    #    ans, i = calcParenthesis(tokens,i)
    #    answer -= ans
    #    i += 1
    #    print("- answer P ",answer)
    #  else:
    #    print('Invalid syntax')
    #    exit(1)
    elif tokens[i]['type'] == 'CLOSE':      #when ) is found
      print("-----returnAS", i, answer)
      return answer, i
    else:
      i += 1
  print("-----returnAS", i, answer)
  return answer, i

#calcParenthesis is only referenced from calcMulDiv
#returns the calculated value inside the parenthesis and the index of )
#index of ( is given
def calcParenthesis(tokens,index):
  print("-----calcP", index)
  answer=0
  i=index+1
  while i < len(tokens):
    print("i=",i)
    if tokens[i]['type'] == 'OPEN':
      ans, i = calcParenthesis(tokens,i)
      answer += ans
      i += 1
    elif tokens[i]['type'] == 'NUMBER' or tokens[i]['type'] == 'MINUS':
      ans, i = calcAddSub(tokens, i)
      answer += ans
    elif tokens[i]['type'] == 'CLOSE':   #if ) is found return value and index of )
      print("-----returnP",i, answer)
      return answer, i
    else:
      print('Invalid syntax')
      exit(1)
  print("-----returnP",i, answer)
  return answer, i

def evaluate(tokens):
  answer = 0
  i=0
  tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
  print(tokens)
  answer, i = calcAddSub(tokens,i)
  return answer


def test(line):
  tokens = tokenize(line)
  actualAnswer = evaluate(tokens)
  expectedAnswer = eval(line)
  if abs(actualAnswer - expectedAnswer) < 1e-8:
    print("PASS! (%s = %f)" % (line, expectedAnswer))
  else:
    print("FAIL! (%s should be %f but was %f)" % (line, expectedAnswer, actualAnswer))


# Add more tests to this function :)
def runTest():
  print("==== Test started! ====")
  test("1+2")
  test("1.0+2.1-3")
  test("-1+2")
  test("1*3-4/6")
  test("2.0*3.5-3/6")
  test("2.0*3.5-3/6.0")
  test("4*(2-1)")
  test("4/5")
  test("(4)/5")
  test("(3.0+4)/5")
  test("(3.0+4*(2-1))/5")
  test("3+(2-1)")
  print("==== Test finished! ====\n")

runTest()

while True:
  print('> ', end="")
  line = input()
  tokens = tokenize(line)
  answer = evaluate(tokens)
  print("answer = %f\n" % answer)