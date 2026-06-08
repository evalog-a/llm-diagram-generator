# RST Diagram Generator

The code implementation of the Rhetorical Structure Theory based diagram generator.
You can read more in [Logacheva, Evanfiya, et al. "When Looks Do Not Lie: Discourse Structure Guided In-Context Learning for Faithful Diagram Generation"][arxiv]

[arxiv]: https://arxiv.org/abs/2601.20476.
```
@misc{logacheva2026improveeducationaldiagramgeneration,
      title={When Looks Do Not Lie: Discourse Structure Guided In-Context Learning for Faithful Diagram Generation}, 
      author={Evanfiya Logacheva and Arto Hellas and Tsvetomila Mihaylova and Juha Sorva and Ava Heinonen and Juho Leinonen},
      year={2026},
      eprint={2601.20476},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2601.20476}, 
}
```
## 🚀 What does it do?
- Feature 1: You place a short text you want to visualize as a GraphViz diagram in the input folder
- Feature 2: You get two rendered diagrams in the output folder: one initial, one LLM-refined.
Models often won't be able to reliably improve their output, you should evaluate which one is better.
- Feature 3: You can get your diagrams automatically evaluated.
## 💻 Usage
You need an OpenAI API key set as an env variable.

### To generate diagrams:
```bash
cd src
python generate.py -m {zero, rst1, rst2} -lm 'model_1' 'model_2' -n 'diagram_name'
```
run generate.py to generate your diagrams
you need to pass the following args: 
1. -m Choose your diagram generation method:
- 'zero' is a zero-shot generation,
- 'rst1' is a stable ICL-generation that uses your original text and a diagram example for generation,
- 'rst2' is the same but uses an RST analysis as input instead of your original text
2. -lm Choose two models: 
- 'model_1' is used only for debugging.
- 'model_2' is used for RST analysis, similarity search, and diagram generation and refinement. We strongly recommend using a large model, preferably with a high reasoning ability. It needs to be able to accept both image and text input.
3. -n 'diagram_name':
- A custom name for your diagram.

The script will save all model outputs (diagrams, RST analyses, refinement explanations) in the output folder.
### To evaluate diagrams:
```bash
cd src
python evaluate.py -e {expl, impl, comb} -i "diagram_name.png" -m "model"
```
1. -e Choose your evaluation method
- 'expl' is an instruction-based, explicit method (1 image input)
- 'impl' is an implicit method using 9 diagram examples (it will require 10 image inputs in the prompt)
- 'comb' is the combination of the methods above, it has the longest prompt (the instruction and the 9 examples + the diagram image you want to rate)

2. -i The diagram name that's in the output/diagrams directory
3. The name of the model, it needs to be able to accept both image and text as input
The script will print three scores from 1 (the lowest) to 5 (the highest) for logical organization, connectivity, and layout aesthetic.
## 📝 License
The code is distributed under the MIT License. See `LICENSE MIT` for more information.
### Texts used for ICL examples
The following diagram source texts were distributed by their respective authors under CC-BY-4.0 Shield: [![CC BY 4.0][cc-by-shield]][cc-by]

[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

Informally, the algorithm proceeds as follows. For each node u, its state s(u) alternates between 1 and 0, initially, s(u) ← 1 and c(u) ← ⊥: When s(u) = 1, the node receives the set of messages M(u), it then decides with probability 0.5 to be passive and set c(u) = ⊥ or to be active and pick a random color c(u) ∈ F(u), where F(u) = C(u)\M(u) is the set of free colors.. Next, it sets s(u) ← 0. When s(u) = 0, the node receives the set of messages M(u), it then verifies its choice. If the current color c(u) conflicts with one of the neighbors (c(u) ∈ M(u)), we go back to the initial state s(u) ← 1 and c(u) ← ⊥. However, if we were lucky and managed to pick a color that does not conflict with any of our neighbors, we keep the current value of c(u) and switch to the stopping state s(u) = 1 and c(u) ̸= ⊥. 
Adopted from: Juho Hirvonen and Jukka Suomela. Distributed Algorithms, 2020, https://jukkasuomela.fi/da2020/

How to Prevent Overwriting Plots in R. If you run ‘pdf’ multiple times without running ‘dev.off’, you will save plots to the most recently opened file. However, you won’t be able to open the previous ‘pdf’ files because the connections were not closed. You can take steps to prevent this. First, you can check your current status using the function ‘dev.cur’. If it says “pdf”, all your plots are being saved in the last pdf specified. In order to get out of this situation, you’ll need to run dev.off until all the ‘pdf’ connections are closed. If the current status says “null device” or “RStudioGD”, the plots will be visualized as intended without overwriting.
Adopted from: Thomas Cason and Rohit Goswami and Hugo Gruson and Katie O'Mahony. Programming with R, 2025, https://github.com/swcarpentry/r-novice-inflammation/

Write a script that loops through the gapminder data by continent and prints out whether the mean life expectancy is smaller or larger than 50 years. Step 1: We want to make sure we can extract all the unique values of the continent vector. Step 2: We also need to loop over each of these continents and calculate the average life expectancy for each subset of data. We can do that as follows: 1. Loop over each of the unique values of continent. 2. For each value of continent, create a temporary variable storing that subset 3.Return the calculated life expectancy to the user by printing the output. Step 3: The exercise only wants the output printed if the average life expectancy is less than 50 or greater than 50. So we need to add an if() condition before printing, which evaluates whether the calculated average life expectancy is above or below a threshold, and prints an output conditional on the result. We need to amend (3) from above: 3a. If the calculated life expectancy is less than some threshold (50 years), return the continent and a statement that life expectancy is less than threshold, otherwise return the continent and a statement that life expectancy is greater than threshold.
Adopted from: Naupaka Zimmerman and Sehrish Kanwal and Matthieu Bruneaux and Craig Gross. R for Reproducible Scientific Analysis, 2025, https://github.com/swcarpentry/r-novice-gapminder/

You might wonder what on earth 'REPL' stands for? Well, here's some short and sweet explanation: 'REPL' is short for read–evaluate–print loop. Those words convey the basic idea:
read: You can type in bits of Scala that the REPL receives as input, or “reads”.
evaluate: The REPL runs your code as soon as it receives it. For instance, when given an arithmetic expression, the REPL performs the given calculation to produce a result.
print: The REPL reports the results of evaluation onscreen.
loop: This interaction between the user and the REPL keeps repeating as long as the user likes.
Adopted from:Juha Sorva. 2024. Programming 1. https://plus.cs.aalto.fi/o1/2024/

So how do packets travel in the TCP/IP protocol? The process is easier than it seems. First, a router receives a packet, then it checks the header of the packet for the IP-address of the recipient. Next, the router looks up the IP-address from its routing table and chooses the best match for passing the packet forward. If the router is not connected to the recipient, it passes the packet forward again. If the router is connected to the recipient, it forwards the packet to the recipient, which means that the packet has reached its destination. The packet is checked, and the recipient responds with a message to the sender, indicating that the packet has been received. 
Adopted from: Arto Hellas. 2025. Web software development https://fitech101.aalto.fi/en/courses/web-software-development

The assignment “Pick 30 fully random numbers between 0 and 9.” is easier said than done. One practical option is to use a “good enough” mathematical algorithm for computing a sequence of numbers. For example: 1.Start by picking some number N, say N=20. 2.Take the Nth decimal of π. Let that be the first “random number”. 3.Determine the next “random number” by taking the another digit from π at 2`*`N. 4.Follow with 3`*`N, 4`*`N, and so on. Adopted from: Juha Sorva. 2024. Programming 1. https://plus.cs.aalto.fi/o1/2024/

There are two types variables: shared and private. Any variable that is declared outside a parallel region is shared, while any declared inside is private. In case of a shared variable, there is only one copy of it, and all threads refer to the same variable. Care is needed whenever you refer to such a variable. On the other hand, in case of any private variable, each thread has its own copy of it. Such variables are always safe to use. If a shared variable is read-only, you can safely refer to it from multiple threads inside the parallel region. However, if any thread ever writes to a shared variable, then proper coordination is needed to ensure that no other thread is simultaneously reading or writing to it. Adopted from: Jukka Suomela. 2025. Programming parallel computers https://ppc.cs.aalto.fi/ack/

Everybody is familiar with the centuries old board game Snakes and Ladders, which is an example of a Markov Chain. In a nutshell, there is a board with a hundred and one numbered squares on it (some of which are ‘snakes’ and ‘leaders’), which can be considered states. The game proceeds as follows. Players advance from the start state of 0 by throwing dice and using the numbers they obtain to move ahead to a new state (with the equal probability of 1/6) until they reach the terminal state of 100. When moving to a new state, they can advance to an ordinary state or one of the two special states: ‘snakes’ or ‘ladders’. If a player’s new state is the head of a snake, they have to go backwards, losing some of their advance. If it is the base of a ladder, they advance to the top of that ladder. Adopted from: Martin Frické. 2024. Artificial Intelligence and Librarianship: Notes for Teaching (3rd ed.). SoftOption. ISBN 978-0-473-72294-4. Open Textbook Library. 

