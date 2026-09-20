Design Memo:
    My linked list works by using Nodes for each customer. Each Node stores the persons name and a next value. The next value tells the program who comes after that person in the waitlist.
    The LinkedList class controls the whole list. It can add someone to the front, add someone to the end, remove someone, and print everyone thats waiting.
    The head is basically the first person in the list. It is important because the program needs to know where the list starts.
    If the head is None, then the waitlist is empty. When someone gets added to the front, that person becomes the new head.
    A real engineer might use a list like this if they need to keep people or items in a certain order.
    For example, a ticket company could put VIP customers in the front and regular customers in the back.
    It could also be used for waiting lines or tasks. A linked list is useful because you can add or remove stuff without moving everything around.
