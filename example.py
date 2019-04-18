import wolframalpha as wa

inp = input("QUESTION: ")
app_id = "#api_id"
client = wa.Client(app_id)
res=client.query(inp)
answer=next(res.results).text
print(answer)




