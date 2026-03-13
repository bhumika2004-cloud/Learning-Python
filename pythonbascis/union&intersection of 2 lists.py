def list_union_intersection(list1,list2):
    a=set(list1)
    b=set(list2)
    u=list(a.union(b))
    i=list(a.intersection(b))
    return (sorted(u),i)
