cities = {
    "los angeles": ["new york", "montreal"],
    "montreal": ["new york", "los angeles"],
    "new york": ["los angeles", "paris", "montreal"],
    "paris" : ["new york"]
}

searched_queue = []
searched_queue.append("los angeles")
searched_queue.append("montreal")
searched_queue.append("new york")

print(searched_queue)

print(searched_queue.pop())
print(searched_queue)