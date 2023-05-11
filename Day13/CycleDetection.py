def has_cycle(head):
    df = {}
    while head:
        if df.get(head):
            return 1
        df[head] = 1
        head = head.next
    return 0