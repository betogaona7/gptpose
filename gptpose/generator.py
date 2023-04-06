from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from gptpose.templates import POSE_VALUES_TEMPLATE
from gptpose.utils import build_image, get_logger


class PoseGenerator:
    """generates a pose image for the description."""

    def __init__(self, pose_description: str, output_path: str) -> None:
        """constructor

        Args:
            pose_description (str): body pose description.
            output_path (str): path to save pose image.
        """
        # initialize logger
        self.logger = get_logger("gptpose")

        self.pose_description = pose_description
        self.output_path = output_path

    def generate_pose(self, model_name):
        """builds a pose image based on GPT coords suggestions.

        Returns:
            pose_image: pose image.
        """
        self.logger.info(
            "Asking GPT to define the pose coords based on the pose body description..."
        )
        chain = self._create_chain(model_name)
        gpt_response = chain.run(self.pose_description)
        self.logger.info(f"GPT answer: {gpt_response}")

        self.logger.info("building pose image...")
        pose_image = build_image(gpt_response)

        self.logger.info(f"saving pose image in {self.output_path}")
        pose_image.save(self.output_path)

        return pose_image

    def _create_chain(self, model_name: str):
        """create chain object to send request to GPT.

        Args:
            model_name (str): OpenAI model name to use.

        Returns:
            LLMChain: chain object.
        """
        llm = OpenAI(model_name=model_name)
        prompt = PromptTemplate(
            input_variables=["pose_description"], template=POSE_VALUES_TEMPLATE
        )
        return LLMChain(prompt=prompt, llm=llm)
