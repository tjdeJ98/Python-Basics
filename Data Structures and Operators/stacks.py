# LIFO -> last in first out

browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)

last = browsing_session.pop()
print(last)
print(browsing_session)

if not browsing_session:  # incase all popped
    print("redirect", browsing_session[-1])  # -1 to always get the last item

if not browsing_session:
    print("Disable back button")
