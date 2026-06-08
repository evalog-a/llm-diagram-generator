import scripts
import template
import diagram_examples
import json
from config import client

def main():
    text_t = scripts.load_text_file()
    args = scripts.get_args_eval()
    eval_method = args.eval
    l_model = args.lmodel
    image_n = args.img
    image_id = scripts.create_file(image_path=f"../output/diagrams/{image_n}",
                                   )
    #print(args)
    icl_images = []
    for i in list(range(0, 9)):
        icl_images.append(scripts.create_file(image_path=f"data/prompts"
                                                         f"/E_ICL_files"
                                                         f"/image{i}.png"))

    text_format = {
        "format": {
            "type": "json_schema",
            "name": "dot",
            "schema": {
                "type": "object",
                "properties": {
                    "Q1": {"type": "integer"},
                    "Q2": {"type": "integer"},
                    "Q3": {"type": "integer"},
                },
                "required": ["Q1", "Q2", "Q3"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    }

    match eval_method:
        case "expl":
            response = client.responses.create(
                model=l_model,
                input=[{
                    "role": "user",
                    "content": [
                        {"type": "input_text",
                         "text": template.DIAGRAM_EVALUATOR
                                 + "Here's the source text for the diagram,"
                                   "which will aid you in the diagram "
                                   "assessment: "
                                 + str(text_t)},
                        {
                            "type": "input_image",
                            "file_id": image_id,
                        },
                    ],
                }],
                text=text_format,
            )
        case "impl":
            response = client.responses.create(
                model=l_model,
                input=[{
                    "role": "user",
                    "content": [
                        {"type": "input_text",
                         "text": "logical organization: 2; connectivity: 5; "
                                 "layout quality: "
                                 f"4; "
                                 f"{diagram_examples.DIAGRAM_EVAL_TEXTS[0]}"},
                        {
                            "type": "input_image",
                            "file_id":
                                icl_images[0],
                        },
                        {"type": "input_text",
                         "text": "logical organization: 2; connectivity: 4; "
                                 "layout quality: "
                                 f"4; "
                                 f"{diagram_examples.DIAGRAM_EVAL_TEXTS[1]}"},
                        {
                            "type": "input_image",
                            "file_id":
                                icl_images[1],
                        },
                        {"type": "input_text",
                         "text": "logical organization: 3; connectivity: 5; "
                                 "layout quality: "
                                 f"4; "
                                 f"{diagram_examples.DIAGRAM_EVAL_TEXTS[2]}"},
                        {
                            "type": "input_image",
                            "file_id":
                                icl_images[2],
                        },
                        {"type": "input_text",
                         "text": "logical organization: 3; connectivity: 4; "
                                 "layout quality: "
                                 f"4; "
                                 f"{diagram_examples.DIAGRAM_EVAL_TEXTS[0]}"},
                        {
                            "type": "input_image",
                            "file_id":
                                icl_images[3],
                        },
                        {"type": "input_text",
                         "text": "logical organization: 3; connectivity: 5; "
                                 "layout quality: "
                                 f"4; "
                                 f"{diagram_examples.DIAGRAM_EVAL_TEXTS[1]}"},
                        {
                            "type": "input_image",
                            "file_id":
                                icl_images[4],
                        },
                        {"type": "input_text",
                         "text": "logical organization: 4; connectivity: 5; "
                                 "layout quality: "
                                 f"4; "
                                 f"{diagram_examples.DIAGRAM_EVAL_TEXTS[2]}"},
                        {
                            "type": "input_image",
                            "file_id":
                                icl_images[5],
                        },
                        {"type": "input_text",
                         "text": "logical organization: 2; connectivity: 4; "
                                 "layout quality: "
                                 f"3; "
                                 f"{diagram_examples.DIAGRAM_EVAL_TEXTS[0]}"},
                        {
                            "type": "input_image",
                            "file_id":
                                icl_images[6],
                        },
                        {"type": "input_text",
                         "text": "logical organization: 5; connectivity: 5; "
                                 "layout quality: "
                                 f"4; "
                                 f"{diagram_examples.DIAGRAM_EVAL_TEXTS[1]}"},
                        {
                            "type": "input_image",
                            "file_id":
                                icl_images[7],
                        },
                        {"type": "input_text",
                         "text": "logical organization: 1; connectivity: 1; "
                                 "layout quality: "
                                 f"2;  "
                                 f"{diagram_examples.DIAGRAM_EVAL_TEXTS[2]}"},
                        {
                            "type": "input_image",
                            "file_id":
                                icl_images[8],
                        },
                        {"type": "input_text",
                         "text": "logical organization: ?; connectivity: ?; "
                                 f"layout quality: ?; text:{text_t}"},
                        {
                            "type": "input_image",
                            "file_id": image_id,
                        },
                    ],
                }],
                text=text_format,
            )
        case "comb":
            response = client.responses.create(
                model=l_model,
                input=[{
                    "role": "user",
                    "content": [
                        {"type": "input_text",
                         "text": "{}".format(template.DIAGRAM_EVALUATOR)},
                        {"type": "input_text",
                         "text": "logical organization: 2; connectivity: 5; "
                                 "layout quality: "
                                 f"4; "
                                 f"{diagram_examples.DIAGRAM_EVAL_TEXTS[0]}"},
                        {
                            "type": "input_image",
                            "file_id":
                                icl_images[0],
                        },
                        {"type": "input_text",
                         "text": "logical organization: 2; connectivity: 4; "
                                 "layout quality: "
                                 f"4; "
                                 f"{diagram_examples.DIAGRAM_EVAL_TEXTS[1]}"},
                        {
                            "type": "input_image",
                            "file_id":
                                icl_images[1],
                        },
                        {"type": "input_text",
                         "text": "logical organization: 3; connectivity: 5; "
                                 "layout quality: "
                                 f"4; "
                                 f"{diagram_examples.DIAGRAM_EVAL_TEXTS[2]}"},
                        {
                            "type": "input_image",
                            "file_id":
                                icl_images[2],
                        },
                        {"type": "input_text",
                         "text": "logical organization: 3; connectivity: 4; "
                                 "layout quality: "
                                 f"4; "
                                 f"{diagram_examples.DIAGRAM_EVAL_TEXTS[0]}"},
                        {
                            "type": "input_image",
                            "file_id":
                                icl_images[3],
                        },
                        {"type": "input_text",
                         "text": "logical organization: 3; connectivity: 5; "
                                 "layout quality: "
                                 f"4; "
                                 f"{diagram_examples.DIAGRAM_EVAL_TEXTS[1]}"},
                        {
                            "type": "input_image",
                            "file_id":
                                icl_images[4],
                        },
                        {"type": "input_text",
                         "text": "logical organization: 4; connectivity: 5; "
                                 "layout quality: "
                                 f"4; "
                                 f"{diagram_examples.DIAGRAM_EVAL_TEXTS[2]}"},
                        {
                            "type": "input_image",
                            "file_id":
                                icl_images[5],
                        },
                        {"type": "input_text",
                         "text": "logical organization: 2; connectivity: 4; "
                                 "layout quality: "
                                 f"3; "
                                 f"{diagram_examples.DIAGRAM_EVAL_TEXTS[0]}"},
                        {
                            "type": "input_image",
                            "file_id":
                                icl_images[6],
                        },
                        {"type": "input_text",
                         "text": "logical organization: 5; connectivity: 5; "
                                 "layout quality: "
                                 f"4; "
                                 f"{diagram_examples.DIAGRAM_EVAL_TEXTS[1]}"},
                        {
                            "type": "input_image",
                            "file_id":
                                icl_images[7],
                        },
                        {"type": "input_text",
                         "text": "logical organization: 1; connectivity: 1; "
                                 "layout quality: "
                                 f"2;  "
                                 f"{diagram_examples.DIAGRAM_EVAL_TEXTS[2]}"},
                        {
                            "type": "input_image",
                            "file_id":
                                icl_images[8],
                        },
                        {"type": "input_text",
                         "text": "logical organization: ?; connectivity: ?; "
                                 f"layout quality: ?; text:{text_t}"},
                        {
                            "type": "input_image",
                            "file_id": image_id,
                        },
                    ],
                }],
                text=text_format,
            )

    res = json.loads(response.output_text)
    grades=(res.get("Q1"), res.get("Q2"), res.get("Q3"))
    print(grades)
    scripts.save_grades(str(grades), custom_name=image_n)

if __name__ == "__main__":
    main()
