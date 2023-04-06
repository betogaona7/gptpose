"""
gptpose CLI
"""

import click
import os
import getpass

from gptpose.generator import PoseGenerator


def run(
    pose_description: str,
    output_path: str,
    model_name: str,
) -> None:
    """generates a pose image based on a body pose description."""

    generator = PoseGenerator(
        pose_description=pose_description, output_path=output_path
    )

    _ = generator.generate_pose(model_name=model_name)


@click.command()
@click.option(
    "-d",
    "--description",
    "pose_description",
    required=True,
    help="The body pose description",
)
@click.option(
    "-o",
    "--output-path",
    "output_path",
    required=True,
    help="The path to save the pose images.",
)
@click.option(
    "-n",
    "--model-name",
    "model_name",
    required=False,
    default="GPT-4",
    help="The OpenAI model name you want to use. https://platform.openai.com/docs/models",
)
def main(pose_description: str, output_path: str, model_name: str = "gpt-4"):
    if not os.environ.get("OPENAI_API_KEY"):
        os.environ["OPENAI_API_KEY"] = getpass.getpass(
            prompt="Enter your OpenAI API key: "
        )

    run(pose_description, output_path, model_name)


if __name__ == "__main__":
    main()
