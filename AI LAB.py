import wolframalpha
client=wolframalpha.Client("384JRJ-VWYKUE6QK7")
while True:
    query=str(input("Question:"))
    res=client.query(query)
    output=next(res.results).text
    print(output)