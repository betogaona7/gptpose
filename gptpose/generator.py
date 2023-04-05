from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate 
from langchain.chains import LLMChain

from gptpose.templates import POSE_VALUES_TEMPLATE
from gptpose.utils import build_image, get_logger

class PoseGenerator:
    """generates a pose image for the description.
    """
    def __init__(
        self, 
        pose_description:str,
        output_path: str
    ) -> None:
        """constructor

        Args:
            pose_description (str): body pose description in plain english.
            output_path (str): path to save pose image.
        """
        self.pose_description = pose_description
        self.output_path = output_path
        self.logger = get_logger("gpt_posegen")

    def generate_pose(self):
        self.logger.info("asking GPT to set the pose based on the pose body description...")
        chain = self._create_chain()
        gpt_response = chain.run(self.pose_description)
        self.logger.info(f"GPT answer: {gpt_response}")

        self.logger.info(f"building pose...")
        pose_image = build_image(gpt_response)

        self.logger.info(f"saving pose in {self.output_path}")
        pose_image.save(self.output_path)


    def _create_chain(self):
        # this task is not well handled with GPT-3, it requires GPT-4
        llm = OpenAI(model_name="gpt-4")
        prompt = PromptTemplate(
            input_variables=["pose_description"],
            template = POSE_VALUES_TEMPLATE
        )
        return LLMChain(prompt=prompt, llm=llm)
