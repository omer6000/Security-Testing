constraint="""
exists <Return>:
    exists <integer>:
        (inside(<integer>,<Return>) and str.to.int(<integer>) > 995 and str.to.int(<integer>) < 1005)
"""