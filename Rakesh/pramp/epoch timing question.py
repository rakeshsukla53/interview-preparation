
# firt step is sort the time stamp
# [ add all counts for enter - all counts from exit ] n logn
{ time: 1440084737,  count: 4,  type: "enter" } ----  start time
{ time: 1440084737,  count: 5,  type: "enter" } ---
{ time: 1440084737,  count: 3,  type: "enter" } --- 12
{ time: 1440084737,  count: 2,  type: "exit" } --- 2 ( 10 people are inside the mall) end time
{ time: 1440084737,  count: 1,  type: "enter" } --
{ time: 1440084737,  count: 10,  type: "exit" } -- ( 0 people are inside the mall)
{ time: 1440084737,  count: 10,  type: "enter" } --
{ time: 1440084737,  count: 2,  type: "exit" } -- ( 8 people are inside the mall)
{ time: 1440084737,  count: 10,  type: "enter" }
{ time: 1440084737,  count: 10,  type: "exit" } -- (8 people are inside the mall)
{ time: 1440084737,  count: 5,  type: "enter" } - ( 13 people are inside the mall)


[4, 5, 3, -2, 1, -10, 10, -2 , 10, -10, 5] O(n)

Maximum subarray problem

Overall complexity = nlogn

