constraint="""
exists <If> first:
    exists <If> second:
        (not inside(first, second) and not inside(second, first))
"""