# traffic notation

rules:

1. `{abc}`: a set of independent jobs that can be run in any order.
1. `[abc]`: a sequence of jobs that are to be in run in this order `a` -> `b` -> `c`.

example 1: `[a{bc}de]`

example 2: `[{abc}def{ghijk}lm{n[op]}]`.

example 3: `{[a{bc}d{efg}hi]j[kl{mn}op]q}`
