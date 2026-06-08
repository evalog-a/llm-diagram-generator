import scripts
from pydantic import BaseModel


def main():
    class RSTResponse(BaseModel):
        rst_tree: str

    class ModelResponse(BaseModel):
        dot_code: str

    class SimilarResponse(BaseModel):
        id: str

    text_t = scripts.load_text_file()
    args = scripts.get_args_gen()
    model_1 = args.lmodel[0]
    model_2 = args.lmodel[1]
    img_name = args.name
    g_method = args.method
    scripts.execute_pipeline(input_t=text_t,
                             text_format_diagram=ModelResponse,
                             text_format_analysis=RSTResponse,
                             text_format_similarity=SimilarResponse,
                             model_1=model_1, model_2=model_2,
                             img_name=img_name, method=g_method)


if __name__ == "__main__":
    main()