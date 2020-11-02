import pandas as pd

nfa = {}
num = int(input("No. of states : "))  # Enter no. of states
transition = int(input("No. of transitions : "))  # Enter no. of transitions/paths eg: a,b so input 2 for a,b,c input 3
for i in range(num):
    state = input("state name : ")  # Enter state name eg: A, B, C,..etc
    nfa[state] = {}  # Create a nested dictionary
    for j in range(transition):
        path = input("path : ")  # Enter path eg : a or b in {a,b} 0 or 1 in {0,1}
        print("Enter end state from state {} travelling through path {} : ".format(state, path))
        reach = [x for x in input().split()]  # Enter all the end states that
        nfa[state][path] = reach

print("\nNFA :- \n")
print(nfa)  # print NFA
print("\nPrinting NFA table :- ")
nfa_table = pd.DataFrame(nfa)
print(nfa_table.transpose())

print("Enter final state of NFA : ")
nfa_final_state = [x for x in input().split()]  # Enter final state/states of NFA

new_states_list = []  # holds all the new states created in dfa
dfa = {}  # dfa dictionary/table or the output structure we needed
keys_list = list(
    list(nfa.keys())[0])  # has all the states in nfa plus the states created in dfa are also appended
path_list = list(nfa[keys_list[0]].keys())  # list of all the paths eg: [a,b] or [0,1]

# Computing first row of DFA transition table
dfa[keys_list[0]] = {}  # create a nested dictionary in dfa
for y in range(transition):
    var = "".join(nfa[keys_list[0]][path_list[y]])
    # create a single string from all the elements of the list which is a new state
    dfa[keys_list[0]][path_list[y]] = var  # assigning the state in DFA table
    if var not in keys_list:  # if the state is newly created
        new_states_list.append(var)  # then append it to the new_states_list
        keys_list.append(var)  # as well as to the keys_list which contains all the states

# Computing the other rows of DFA transition table
while len(new_states_list) != 0:
    dfa[new_states_list[0]] = {}
    for _ in range(len(new_states_list[0])):
        for i in range(len(path_list)):
            temp = []
            for j in range(len(new_states_list[0])):
                temp += nfa[new_states_list[0][j]][path_list[i]]  # taking the union of the states
            s = ""
            s = s.join(temp)  # create a single string from all the elements of the list
            if s not in keys_list:  # if the state is newly created
                new_states_list.append(s)  # then append it to the new_states_list
                keys_list.append(s)  # also to the keys_list which contains all the states
            dfa[new_states_list[0]][path_list[i]] = s  # assign the new state in the DFA table

    new_states_list.remove(new_states_list[0])  # Remove the first element in the new_states_list

print("\nDFA :- \n")
print(dfa)  # Print the DFA created
print("\nPrinting DFA table :- ")
dfa_table = pd.DataFrame(dfa)
print(dfa_table.transpose())

dfa_states_list = list(dfa.keys())
dfa_final_states = []
for x in dfa_states_list:
    for i in x:
        if i in nfa_final_state:
            dfa_final_states.append(x)
            break

print("\nFinal states of the DFA are : ", dfa_final_states)  # Print Final states of DFA
