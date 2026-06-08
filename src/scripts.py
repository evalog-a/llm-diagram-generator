import re
import json
import template
import diagram_examples
import graphviz
import argparse
from config import client

def load_text_file():
    try:
        with open("../input/input_text.txt", 'r', encoding='utf-8') as file:
            content = file.read()
            # Check if the file is empty or just whitespace
            if not content.strip():
                raise ValueError(f"The file is empty.")
            return content
    except FileNotFoundError:
        print(f"The file isn't found.")
        raise


def get_args_gen():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--method", choices=["zero", "rst1", "rst2"],
                        default="zero",
                        required=True,
                        help="Choose the method to produce your diagram")
    parser.add_argument("-lm", "--lmodel",
                        nargs=2,
                        required=True,
                        help="Choose the models: 1. for simple debugging " \
                             "2. for diagram generation and refinement")
    parser.add_argument("-n", "--name",
                        required=True,
                        help="Input a custom name for your diagram")
    parser.print_help()
    return parser.parse_args()


def get_args_eval():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--eval",
                        choices=["impl", "comb", "expl"],
                        default="expl",
                        required=True,
                        help="Choose evaluation method; default is explicit")
    parser.add_argument("-i", "--img",
                        required=True,
                        help="Image path")
    parser.add_argument("-m", "--lmodel",
                        required=True,
                        help="Model name")
    parser.print_help()
    return parser.parse_args()


def analyze_text(input_text: str, model: str, text_format):
    print("The text analysis has started; it might take some time.")
    response = client.responses.parse(
        model=model,
        input=[
            {"role": "system", "content": template.RST_ANALYST},
            {"role": "user",
             "content": "Here's the text to analyze: " + input_text}
        ],
        text_format=text_format,
    )
    return "Disclaimer: This text is generated with the {} language model.\n " \
           "The model uses the following paper to generate its output: Stede, " \
           "" \
           "Manfred, Maite Taboada, and Debopam Das. 'Annotation guidelines " \
           "for rhetorical structure.' Manuscript. University of Potsdam and " \
           "Simon Fraser University (2017).\n".format(
        model) + response.output_parsed.rst_tree


def find_similar(model_analysis: str, model: str,  text_format):
    response = client.responses.parse(
        model=model,
        input=[
            {"role": "system",
             "content": "You will be given a discourse analysis of a text and "
                        "asked to find a similar text based on Rhetorical "
                        "Structure Theory from a set of 4 texts. Your choice "
                        "should be based on the types of discourse relations "
                        "present in the text." + str(
                 diagram_examples.DIAGRAM_ANALYSES)
             },
            {"role": "user",
             "content": "You will be given a piece of analyzed text as input. "
                        "Your output should contain the id of the chosen text "
                        "from the 4 analyses. \n ***Text analysis***:\n" +
                        model_analysis
             }
        ],
        text_format=text_format,
    )
    return (response.output_parsed.id)


def return_id(id_string: str):
    temp = re.findall(r'\d+', id_string)
    id_s = int(temp[0])
    rst_example = diagram_examples.DIAGRAM_ANALYSES[id_s]
    text_example = diagram_examples.DIAGRAM_TEXTS[id_s]
    dot_example = diagram_examples.DIAGRAM_DOT[id_s]
    return ([rst_example, text_example, dot_example])


def produce_prompt(method: str, examples: list = None):
    d_prompt = None
    match method:
        case "zero":
            d_prompt = template.ZERO_SHOT_DIAGRAM_GENERATOR
        case "rst1":
            d_prompt = template.RST1_DIAGRAM_GENERATOR + str(examples[1]) + str(
                examples[-1])
        case "rst2":
            d_prompt = template.RST2_DIAGRAM_GENERATOR + str(examples[0]) + str(
                examples[-1])
    return d_prompt


def produce_diagram(text: str, model: str, prompt_diagram: str,
                    text_format):
    response = client.responses.parse(
        model=model,
        input=[
            {"role": "system", "content": prompt_diagram
             },
            {
                "role": "user",
                "content": "You will be given a piece of text as input. Your "
                           "output should contain a piece of dot diagram code "
                           "for the diagram generation. Add a disclaimer to "
                           "the diagram's label stating that it's generated "
                           "with an AI model. \n ***Text***:\n" + text
            }
        ],
        text_format=text_format
    )
    return response.output_parsed.dot_code


def create_file(image_path: str):
    with open(image_path, "rb") as file_content:
        result = client.files.create(
            file=file_content,
            purpose="vision",
        )
        return result.id


def refine_diagram(custom_name: str, model: str, diagram_dot: str):
    file_id = create_file(f"../output/diagrams/diagram_{custom_name}.png")

    response = client.responses.create(
        model=model,
        input=[{
            "role": "user",
            "content": [
                {"type": "input_text",
                 "text": template.DIAGRAM_CHECKER.format(diagram_dot)},
                {
                    "type": "input_image",
                    "file_id": file_id,
                },
            ],
        }],
        text={
            "format": {
                "type": "json_schema",
                "name": "dot",
                "strict": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "explanation": {"type": "string"},
                        "dot_code": {"type": "string"},
                    },
                    "required": ["explanation", "dot_code"],
                    "additionalProperties": False,
                },
                "strict": True,
            },
        },
    )

    res = json.loads(response.output_text)
    code = res.get("dot_code")
    explanation = res.get("explanation")
    return code, explanation


def debug_diagram(dot: str, error: str,  text_format, model: str):
    response = client.responses.parse(
        model=model,
        input=[
            {"role": "system",
             "content": "You are given a piece of faulty code in the dot "
                        "syntax and an error message. Correct the code by "
                        "fixing the error. Do not introduce any other changes."
             },
            {
                "role": "user",
                "content": "Your output should contain dot diagram code. Add "
                           "a disclaimer to the diagram's label stating it's "
                           "generated with an AI model if it's not already "
                           "there. ***Diagram code***:" + dot + "Error:" + error
            }
        ],
        text_format=text_format
    )
    return response.output_parsed.dot_code


def render_diagram(dot: str, custom_name: str):
    dia_dot = graphviz.Source(dot)
    dia_dot.render(filename='diagram_{}'.format(custom_name),
                   directory='../output/diagrams/', format='png').replace('\\', '/')


def out_diagram(dot, model: str, custom_name: str,  text_format):
    render = False
    i = 0
    while not render and i < 5:
        try:
            render_diagram(dot, custom_name)
            render = True
            # print('Diagram rendered!')
        except Exception as e:
            i += 1
            print(
                "The diagram isn't rendered, here is the error in the dot "
                "code:\n" + str(
                    e))
            print("Attempting to debug")
            dot = debug_diagram(dot=dot, error=str(e), model=model,
                                text_format=text_format)
            continue


def save_analysis(custom_name: str, analyzed_text):
    analysis_path = "../output/analyses/{}_analysis.txt".format(custom_name)
    try:
        with open(analysis_path, 'x') as textfile:
            textfile.write(analyzed_text)
    except FileExistsError:
        print("The analysis file already exists. Now it's rewritten.")
        with open(analysis_path, 'w') as textfile:
            textfile.write(analyzed_text)


def save_exp(expl_text, custom_name: str):
    exp_path = "../output/model_exp/{}_exp.txt".format(custom_name)
    try:
        with open(exp_path, 'x') as textfile:
            textfile.write(expl_text)
    except FileExistsError:
        print("The explanation file already exists. Now it's rewritten.")
        with open(exp_path, 'w') as textfile:
            textfile.write(expl_text)


def save_grades(grades, custom_name: str):
    exp_path = "../output/evaluation/{}_grade.txt".format(custom_name)
    try:
        with open(exp_path, 'x') as textfile:
            textfile.write(grades)
    except FileExistsError:
        print("The eval file already exists. Now it's rewritten.")
        with open(exp_path, 'w') as textfile:
            textfile.write(grades)


def execute_pipeline(input_t,  text_format_diagram,
                     text_format_analysis,
                     text_format_similarity,
                     model_1, model_2, img_name, method):
    d_dot = None

    match method:
        case "zero":
            d_prompt = produce_prompt(method="zero")
            d_dot = produce_diagram(input_t, model=model_2,
                                    prompt_diagram=d_prompt,
                                    text_format=text_format_diagram)

        case "rst1":
            t_analysis = analyze_text(input_text=input_t, model=model_2,
                                      text_format=text_format_analysis)
            print("The text has been analyzed")
            save_analysis(analyzed_text=t_analysis, custom_name=img_name)
            d_sim = find_similar(model_analysis=t_analysis,
                                 model=model_2,
                                 text_format=text_format_similarity)
            d_example = return_id(id_string=d_sim)
            d_prompt = produce_prompt(examples=d_example, method='rst1')
            print("The prompt has been constructed."\
                  "The diagram generation has started.")
            d_dot = produce_diagram(input_t, model=model_2,
                                    prompt_diagram=d_prompt,
                                    text_format=text_format_diagram)
            # print(t_analysis, d_sim)
        case "rst2":
            t_analysis = analyze_text(input_text=input_t, model=model_2,
                                      text_format=text_format_analysis)
            print("The text has been analyzed")
            save_analysis(analyzed_text=t_analysis, custom_name=img_name)
            d_sim = find_similar(model_analysis=t_analysis,
                                 model=model_2,
                                 text_format=text_format_similarity)
            d_example = return_id(id_string=d_sim)
            d_prompt = produce_prompt(examples=d_example, method='rst2')
            print("The prompt has been constructed." \
                  "The diagram generation has started.")
            d_dot = produce_diagram(input_t, model=model_2,
                                    prompt_diagram=d_prompt,
                                    text_format=text_format_diagram)
            # print(t_analysis, d_sim)
    # print(d_prompt)
    out_diagram(d_dot, model=model_1,
                custom_name=img_name,
                text_format=text_format_diagram)
    refined_dot, exp_text = refine_diagram(custom_name=img_name,
                                           model=model_2,
                                           diagram_dot=d_dot)
    save_exp(expl_text=exp_text, custom_name=img_name)
    out_diagram(refined_dot, model=model_1,
                custom_name="refined_" + img_name,
                text_format=text_format_diagram)
    print("The diagram generation is completed")
