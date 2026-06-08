DIAGRAM_ANALYSES = (
    "ID 0:\n***Analysis***:\nDisclaimer: This text is"
    "generated with the o3 language model.\n"
    "The model uses the following paper to generate its output: Stede, "
    "Manfred,"
    "Maite Taboada, and Debopam Das. 'Annotation guidelines for rhetorical"
    "structure.' Manuscript. University of Potsdam and Simon Fraser "
    "University ("
    "2017)."
    "EDUs:\n"
    "1. You might wonder what on earth 'REPL' stands for?\n"
    "2. Well, here's some short and sweet explanation:\n"
    "3. 'REPL' is short for read–evaluate–print loop.\n"
    "4. Those words convey the basic idea:\n"
    "5. read: You can type in bits of Scala that the REPL receives as input, "
    "or “reads”.\n"
    "6. evaluate: The REPL runs your code\n"
    "7. as soon as it receives it.\n"
    "8. For instance, when given an arithmetic expression,\n"
    "9. the REPL performs the given calculation to produce a result.\n"
    "10. print: The REPL reports the results of evaluation onscreen.\n"
    "11. loop: This interaction between the user and the REPL keeps repeating\n"
    "12. as long as the user likes.\n"
    "\n"
    "RST tree (mononuclear relations are [Relation-Name, Nucleus, Satellite];\n"
    "multinuclear relations are [Relation-Name, Nucleus₁, Nucleus₂, …]):\n"
    "\n"
    "[\"Elaboration\",\n"
    "[\"Preparation\",\n"
    "3,\n"
    "[\"Preparation\",\n"
    "2,\n"
    "1\n"
    "]\n"
    "],\n"
    "[\"Elaboration\",\n"
    "4,\n"
    "[\"List\",\n"
    "5,\n"
    "[\"Elaboration\",\n"
    "[\"Circumstance\", 6, 7],   \n"
    "[\"Circumstance\", 9, 8]   \n"
    "],\n"
    "10,\n"
    "[\"Circumstance\", 11, 12]\n"
    "]\n"
    "]\n"
    "]",
    "ID 1:\n***Analysis***:\nDisclaimer: This text is generated with the"
    "o3 language model.\n"
    "The model uses the following paper to generate its output: Stede, "
    "Manfred,"
    "Maite Taboada, and Debopam Das. 'Annotation guidelines for rhetorical"
    "structure.' Manuscript. University of Potsdam and Simon Fraser "
    "University ("
    "2017).\n"
    "EDUs:\n"
    "1. So how do packets travel in the TCP/IP protocol?\n"
    "2. The process is easier than it seems.\n"
    "3. First, a router receives a packet,\n"
    "4. then it checks the header of the packet for the IP-address of the "
    "recipient.\n"
    "5. Next, the router looks up the IP-address from its routing table\n"
    "6. and chooses the best match for passing the packet forward.\n"
    "7. If the router is not connected to the recipient,\n"
    "8. it passes the packet forward again.\n"
    "9. If the router is connected to the recipient,\n"
    "10. it forwards the packet to the recipient,\n"
    "11. which means that the packet has reached its destination.\n"
    "12. The packet is checked,\n"
    "13. and the recipient responds with a message to the sender,\n"
    "14. indicating that the packet has been received.\n"
    "\n"
    "RST tree (nested lists, Relation – roles – children):\n"
    "['Solutionhood',\n"
    "['Satellite', 1],\n"
    "['Nucleus',\n"
    "['Evaluation',\n"
    "['Satellite', 2],\n"
    "['Nucleus',\n"
    "    ['Sequence',\n"
    "        ['Sequence', 3, 4],\n"
    "        ['Sequence', 5, 6],\n"
    "        ['Contrast',\n"
    "            ['Condition', ['Satellite', 7], ['Nucleus', 8]],\n"
    "            ['Condition',\n"
    "                ['Satellite', 9],\n"
    "                ['Nucleus',\n"
    "                    ['Result', ['Nucleus', 10], ['Satellite', 11]]\n"
    "                ]\n"
    "            ]\n"
    "        ],\n"
    "        ['Sequence',\n"
    "            12,\n"
    "            ['E-Elaboration', ['Nucleus', 13], ['Satellite', 14]]\n"
    "        ]\n"
    "    ]\n"
    "]\n"
    "]\n"
    "]\n"
    "]",
    "ID 2:\n***Analysis***:\nDisclaimer: This text is generated with the"
    "o3 language model.\n"
    "The model uses the following paper to generate its output: Stede, "
    "Manfred,"
    "Maite Taboada, and Debopam Das. 'Annotation guidelines for rhetorical"
    "structure.' Manuscript. University of Potsdam and Simon Fraser "
    "University ("
    "2017)."
    "Motivation\n"
    "├── Satellite: EDU1\n"
    "└── Nucleus\n"
    "└── Enablement\n"
    "├── Nucleus: EDU2\n"
    "└── Satellite\n"
    "└── Sequence\n"
    "    ├── Nucleus: EDU3\n"
    "    ├── Nucleus: EDU4\n"
    "    ├── Nucleus: EDU5\n"
    "    ├── Nucleus: EDU6\n"
    "    └── Nucleus: EDU7\n"
    "\n"
    "EDUs:\n"
    "EDU1: The assignment “Pick 30 fully random numbers between 0 and 9.” is"
    "easier said than done.\n"
    "EDU2: One practical option is to use a “good enough” mathematical "
    "algorithm "
    "for computing a sequence of numbers.\n"
    "EDU3: Start by picking some number N, say N=20.\n"
    "EDU4: Take the Nth decimal of π.\n"
    "EDU5: Let that be the first “random number”.\n"
    "EDU6: Determine the next “random number” by taking the another digit "
    "from π "
    "at 2*N.\n"
    "EDU7: Follow with 3*N, 4*N, and so on.\n",
    "ID 3:\n***Analysis***:\nDisclaimer: This text is generated with the"
    "o3 language model.\n"
    "The model uses the following paper to generate its output: Stede, "
    "Manfred,"
    "Maite Taboada, and Debopam Das. 'Annotation guidelines for rhetorical"
    "structure.' Manuscript. University of Potsdam and Simon Fraser "
    "University (\n"
    "2017).\n"
    "EDUs:\n"
    "1. There are two types variables: shared and private.\n"
    "2. Any variable that is declared outside a parallel region is shared,\n"
    "3. while any declared inside is private.\n"
    "4. In case of a shared variable, there is only one copy of it,\n"
    "5. and all threads refer to the same variable.\n"
    "6. Care is needed\n"
    "7. whenever you refer to such a variable.\n"
    "8. On the other hand, in case of any private variable, each thread has "
    "its"
    "own copy of it.\n"
    "9. Such variables are always safe to use.\n"
    "10. If a shared variable is read-only,\n"
    "11. you can safely refer to it from multiple threads inside the parallel "
    "region.\n"
    "12. if any thread ever writes to a shared variable,\n"
    "13. then proper coordination is needed\n"
    "14. to ensure that no other thread is simultaneously reading or writing "
    "to it.\n"
    "\n"
    "RST tree (nested brackets, relation names in CAPS, N/S labels, "
    "EDU numbers in"
    "parentheses):\n"
    "\n"
    "JOINT [nuclei]\n"
    "├── ELABORATION\n"
    "│     ├── Nucleus (1)\n"
    "│     └── Satellite\n"
    "│           └── CONTRAST [nuclei]\n"
    "│                 ├── (2)\n"
    "│                 └── (3)\n"
    "├── CONTRAST [nuclei]\n"
    "│     ├── Cause\n"
    "│     │     ├── Nucleus\n"
    "│     │     │     └── CIRCUMSTANCE\n"
    "│     │     │           ├── Nucleus (6)\n"
    "│     │     │           └── Satellite (7)\n"
    "│     │     └── Satellite\n"
    "│     │           └── CONJUNCTION [nuclei]\n"
    "│     │                 ├── (4)\n"
    "│     │                 └── (5)\n"
    "│     └── Cause\n"
    "│           ├── Nucleus (9)\n"
    "│           └── Satellite (8)\n"
    "└── CONTRAST [nuclei]\n"
    "├── CONDITION\n"
    "│     ├── Satellite (10)\n"
    "│     └── Nucleus (11)\n"
    "└── CONDITION\n"
    " ├── Satellite (12)\n"
    " └── PURPOSE\n"
    "       ├── Nucleus (13)\n"
    "       └── Satellite (14)")

DIAGRAM_TEXTS = (
    "0:\n***Text***:\nYou might wonder what on earth \'REPL\' stands for? \n"
    "Well, here's some short and sweet explanation: \'REPL\' is short for"
    "read–evaluate–print loop. Those words convey the basic idea:"
    "\nread: You can type in bits of Scala that the REPL receives as input, "
    "or \"reads\""
    "\nevaluate: The REPL runs your code as soon as it receives it."
    "For instance, when given an arithmetic expression, the REPL performs "
    "the given calculation to produce a result."
    "\nprint: The REPL reports the results of evaluation onscreen."
    "\nloop: This interaction between the user "
    "and the REPL keeps repeating as long as the user likes.",
    "1:\n ***Text***:\nSo how do packets travel in the TCP/IP protocol? The "
    "process is easier than it seems. First, a router receives a packet, "
    "then it checks the header of the packet for the IP-address of the "
    "recipient. Next, the router looks up the IP-address from its routing "
    "table and chooses the best match for passing the packet forward. If "
    "the router is not connected to the recipient, it passes the packet "
    "forward again. If the router is connected to the recipient, it forwards "
    "the packet to the recipient, which means that the packet has reached its "
    "destination. The packet is checked, and the recipient responds with a "
    "message to the sender, indicating that the packet has been received.",
    "2:\n***Text***:\nThe assignment “Pick 30 fully random numbers between "
    "0 and 9.” is easier said than done. One practical option is to use a "
    "\'good enough\' mathematical algorithm for computing a sequence of "
    "numbers. \n"
    "For example:\n1.Start by picking some number N, say N=20.\n2.Take "
    "the Nth "
    "decimal of π. Let that be the first “random number”.\n3.Determine "
    "the "
    "next “random number” by taking the another digit from π at "
    "2*N.\n4.Follow "
    "with 3*N, 4*N, and so on.",
    "3:\n***Text***:\nThere are two types variables: shared and private."
    "Any variable that is declared outside a parallel region is shared, "
    "while any declared inside is private. In case of a shared variable,"
    "there is only one copy of it, and all threads refer to the same "
    "variable."
    "Care is needed whenever you refer to such a variable. On the other "
    "hand, "
    "in case of any private variable, each thread has its own copy of it. "
    "Such variables are always safe to use. If a shared variable is read-only, "
    "you can safely refer to it from multiple threads inside the parallel "
    "region. However, if any thread ever writes to a shared variable, "
    "then proper coordination is needed to ensure that no other thread is "
    "simultaneously reading or writing to it.")

DIAGRAM_DOT = (
    """0:***Graphviz diagram***:\ndigraph {
    graph [fontname=Lato rankdir=LR]
    node [fontname=Lato style="filled,rounded" margin=0.2 penwidth=0 
    colorscheme=blues9]
    edge [fontname=Lato color="#2B303A"]
    A [label="'REPL' is short for read–evaluate–print loop" fillcolor=6 
    fontcolor=white shape="plaintext" width=4]
    B [label="read: the REPL 'reads' user input" fillcolor=2 shape="plaintext" 
    width=4]
    C [label="evaluate: the REPL runs code\nupon receiving it" fillcolor=2 
    shape="plaintext" width=4]
    D [label="print: the REPL reports\nthe results of evaluation onscreen" 
    fillcolor=2 shape="plaintext" width=4]
    E [label="loop: the REPL is repeated\nas long as the user wants" 
    fillcolor=2 shape="plaintext" width=4]                 
    A -> B [comment="the edge connects the main statement to the explanation 
    of its part" dir=none]
    A -> C [comment="the edge connects the main statement to the explanation 
    of its part" dir=none]
    A -> D [comment="the edge connects the main statement to the explanation 
    of its part" dir=none]
    A -> E [comment="the edge connects the main statement to the explanation 
    of its part" dir=none] 
    comment = "the nodes B, C, D, E represent a multinuclear list relation"
    label="The concept of REPL" peripheries=0 fontname=Lato	fontsize=20
}""", """1:***Graphviz diagram***:\ndigraph {
    graph [layout=dot splines="ortho" rankdir=TB]
    node [fontname=Lato style="filled,rounded" margin=0.2 penwidth=0 
    colorscheme=blues9 height=1 width=6 fixedsize=true]
    edge [fontname=Lato color="#2B303A" len = 1]
    E [label="A router receives a packet" fillcolor=1 shape="plaintext" 
    width=4]
    G [label="The router checks the packet's header\nfor the IP-address of the 
    recipient" fillcolor=2 shape="plaintext" width=4]
    H [label="The router looks up the IP-address\nfrom its routing table" 
    fillcolor=3 shape="plaintext" width=4]
    I [label="The router chooses the best match \nto pass the packet 
    forward" fillcolor=4 shape="plaintext" width=4]
    F [label="Is the router connected\nto the recipient?" shape="diamond" 
    fillcolor="#40e0d0" width=5]
    M [label="The router forwards\nthe packet to another router" 
    fillcolor=5 shape="plaintext" width=4]
    K [label="The router forwards\nthe packet to the recipient" 
    fillcolor=5 shape="plaintext" width=4]
    J [label="The packet is checked" fillcolor=6 shape="plaintext" 
    width=4]
    L [label="The recipient sends \na message to the sender\nto indicate 
    the packet is received" fillcolor=7 fontcolor=white shape="plaintext" 
    width=4]
    E -> G[weight=2 comment="the edge connects one step in the sequence 
    to another"]
    G -> H[weight=2 comment="the edge connects one step in the sequence 
    to another"]
    H -> I[weight=2 comment="the edge connects one step in the sequence 
    to another"]
    I -> F[weight=2 comment="the edge connects one step in the sequence 
    to another"]                        
    F -> M [xlabel="No" comment="the edge connects the node F, 
    which describes a conditional statement, to the node M, 
    which describes the outcome when the condition is not satisfied"]
    M -> E [weight=2 comment="the edge connects the node M, 
    which describes the outcome of the condition expressed in the node F 
    being unsatisfied, to the node E, which starts the sequence of the 
    packet delivery again"]
    F -> K [xlabel="Yes" comment="the edge connects the node F, 
    which describes a conditional statement, to the node K, which describes 
    the outcome when the condition is satisfied"]                           
    K -> J[weight=2 comment="the edge connects one step in the sequence 
    to another"] 
    J -> L[weight=2 comment="the edge connects one step in the sequence 
    to another"]
    E -> K [style=invis comment="visual attribute allignment, 
    no discourse relation between the nodes"]      
    label="Packet delivery in TCP/IP protocol" fontname=Lato fontsize=20	
}""", """2:***Graphviz diagram***:\ndigraph {
    graph [fontname=Lato rankdir=TB]
    node [fontname=Lato style="filled,rounded" margin=0.2 penwidth=0 
    colorscheme=blues9]
    edge [fontname=Lato color="#2B303A"]
    E [label="Pick a number N, e.g., N=20" fillcolor=2 shape="plaintext" 
    width=4]
    G [label="Take the Nth decimal of π;\nit's the first 'random number'" 
    fillcolor=3 shape="plaintext" width=4]
    H [label="Next 'random number':\ndigit at 2*N of π" fillcolor=4 
    shape="plaintext" width=4]
    I [label="Continue with 3*N, 4*N, etc." fillcolor=5 shape="plaintext" 
    width=4]
    E -> G[weight=2 comment="the edge connects one step in the sequence to 
    another"]
    G -> H[weight=2 comment="the edge connects one step in the sequence to 
    another"]
    H -> I[weight=2 comment="the edge connects one step in the sequence to 
    another"]
    label="An example solution for the 'Pick 30 fully random numbers between 
    0 and 9' assignment." peripheries=0 fontname=Lato fontsize=20
}""", """3:***Graphviz diagram***:\ndigraph {
    compound=true
    graph [fontname=Lato rankdir=TB splines=ortho]
    node [fontname=Lato style="filled,rounded" margin=0.2 penwidth=0 
    colorscheme=blues9]
    edge [fontname=Lato color="#2B303A"]
    F [label="There are two types variables:
    shared and private." shape="plaintext" fillcolor=4 width=2]
    J [label="Shared variables are declared\noutside a parallel region." 
    fillcolor=2 shape="plaintext" width=2 height=1]
    B [label="Private variables are declared\ninside a parallel region." 
    fillcolor=3 shape="plaintext" width=2 height=1]
    G [label="Is the shared variable\nread-only?" shape="diamond" 
    fillcolor="#40e0d0" width=2] 
    N[label = "The variables can be safely\nreferred to from multiple 
    threads\ninside the parallel region." fillcolor=2 shape="plaintext" 
    width=2 height=1]  
    O[label = "Proper coordination is needed\nto ensure that no other 
    thread is\nsimultaneously reading or writing to it." fillcolor=2 
    shape="plaintext" width=2 height=1]               
    subgraph cluster_shared_var { 
        style="rounded" label="Shared variables 
        properties" fontsize=15          
        C [label="There is only one copy of the\n variable.\nAll threads 
        refer to the same\n variable." fillcolor=2 shape="plaintext" 
        width=2 height=1]
        E [label="Care is needed whenever you\n refer to a shared 
        variable." fillcolor=2 shape="plaintext" width=1 height=1]
        color=lightgrey comment="the subgraph elaborates on shared 
        variables"
        C->E [comment="the edge connects the node C to the node E. C 
        explains E"]
        }
    subgraph cluster_private_var { 
        style="rounded" label="Private 
        variables properties" fontsize=15          
        L [label="Each thread has its own\n copy of the variable." 
        fillcolor=3 shape="plaintext" width=2 height=1]
        M [label="Private variables are\n always safe to use." 
        fillcolor=3 shape="plaintext" width=2 height=1]
        color=lightgrey comment="the subgraph elaborates on private 
        variables"
        L->M [comment="the edge connects the node L to the node M. L 
        explains M"]
        }
    F -> J [comment="the edge connects the node F, which describes a 
    nuclear statement, to the node J, which elaborates on it" dir=none]    
    F -> B [comment="the edge connects the node F, which describes a 
    nuclear statement, to the node B, which elaborates on it" dir=none]
    B -> L[lhead=cluster_private_var comment = "the edge connects the 
    node B to the list of its properties contained within the cluster 
    cluster_private_var" dir=none]
    J -> C[lhead=cluster_shared_var comment = "the edge connects the node 
    J to the list of its properties contained within the cluster 
    cluster_shared_var" dir=none]   
    J -> G[comment = "the edge connects the node J to the G that explains 
    further the use of shared variables" dir=none]    
    G -> N [xlabel="Yes" comment="the edge connects the node G, 
    which describes a conditional statement, to the node N, 
    which describes the outcome when the condition is satisfied"]    
    G -> O [xlabel="No" comment="the edge connects the node G, 
    which describes a conditional statement, to the node O, 
    which describes the outcome when the condition is not satisfied"]
    label="Shared and private variables in parallel programming" peripheries=0 
    fontname=Lato	fontsize=20
}""")

DIAGRAM_EVAL_TEXTS = ("text:Informally, the algorithm proceeds "
                      "as follows. For "
                      "each node u, its state s(u) alternates "
                      "between 1 and 0, "
                      "initially, s(u) ← 1 and c(u) ← ⊥: When s("
                      "u) = 1, the node "
                      "receives the set of messages M(u), it then "
                      "decides with "
                      "probability 0.5 to be passive and set c(u) "
                      "= ⊥ or to be "
                      "active and pick a random color c(u) ∈ F("
                      "u), where F(u) = C("
                      r"u)\M(u) is the set of free colors.. Next, "
                      r"it sets s(u) ← 0. "
                      "When s(u) = 0, the node receives the set "
                      "of messages M(u), "
                      "it then verifies its choice. If the "
                      "current color c(u) "
                      "conflicts with one of the neighbors (c(u) "
                      "∈ M(u)), "
                      "we go back to the initial state s(u) ← 1 "
                      "and c(u) ← ⊥. "
                      "However, if we were lucky and managed to "
                      "pick a color that "
                      "does not conflict with any of our "
                      "neighbors, we keep the "
                      "current value of c(u) and switch to the "
                      "stopping state s(u) "
                      "= 1 and c(u) ̸= ⊥.",
                      "text:How to Prevent Overwriting Plots "
                      "in R. If you run "
                      "‘pdf’ multiple times without running "
                      "‘dev.off’, you will "
                      "save plots to the most recently opened "
                      "file. However, "
                      "you won’t be able to open the previous "
                      "‘pdf’ files because "
                      "the connections were not closed. You can "
                      "take steps to "
                      "prevent this. First, you can check your "
                      "current status "
                      "using the function ‘dev.cur’. If it says "
                      "“pdf”, all your "
                      "plots are being saved in the last pdf "
                      "specified. In order "
                      "to get out of this situation, you’ll need "
                      "to run dev.off "
                      "until all the ‘pdf’ connections are "
                      "closed. If the current "
                      "status says “null device” or “RStudioGD”, "
                      "the plots will be "
                      "visualized as intended without "
                      "overwriting.",
                      "text: Write a script that loops through "
                      "the gapminder "
                      "data by continent and prints out whether "
                      "the mean life "
                      "expectancy is smaller or larger than 50 "
                      "years. Step 1: We "
                      "want to make sure we can extract all the "
                      "unique values of "
                      "the continent vector. Step 2: We also need "
                      "to loop over "
                      "each of these continents and calculate the "
                      "average life "
                      "expectancy for each subset of data. We can "
                      "do that as "
                      "follows: 1. Loop over each of the unique "
                      "values of "
                      "continent. 2. For each value of continent, "
                      "create a "
                      "temporary variable storing that subset "
                      "3.Return the "
                      "calculated life expectancy to the user by "
                      "printing the "
                      "output. Step 3: The exercise only wants "
                      "the output printed "
                      "if the average life expectancy is less "
                      "than 50 or greater "
                      "than 50. So we need to add an if() "
                      "condition before "
                      "printing, which evaluates whether the "
                      "calculated average "
                      "life expectancy is above or below a "
                      "threshold, and prints "
                      "an output conditional on the result. We "
                      "need to amend (3) "
                      "from above: 3a. If the calculated life "
                      "expectancy is less "
                      "than some threshold (50 years), return the "
                      "continent and a "
                      "statement that life expectancy is less "
                      "than threshold, "
                      "otherwise return the continent and a "
                      "statement that life "
                      "expectancy is greater than threshold"
                      )

