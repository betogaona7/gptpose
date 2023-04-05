"""
GPT-PoseGen CLI 
"""

import click 
import os
import getpass

from generator import PoseGenerator

def run(
    pose_description: str,
    output_path: str
):
    """generates a pose image based on a body pose description.
    """

    generator = PoseGenerator(
        pose_description=pose_description, 
        output_path=output_path
    )

    generator.generate_pose()


@click.command()
@click.option("-d", "--description", "pose_description", required=True, help="The body pose description")
@click.option("-o", "--output-path", "output_path", required=True, help="The path to save the pose images.")
def main(
    pose_description: str,
    output_path: str
):
    if not os.environ.get("OPENAI_API_KEY"):
        os.environ["OPENAI_API_KEY"] = getpass.getpass(
            prompt="Enter your OpenAI API key: "
        )

    run(pose_description, output_path) 


if __name__ == "__main__":
    main()
