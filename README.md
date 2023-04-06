# gptpose

GPT-4 conditioning Stable Diffusion through automatic pose image generations based on body pose descriptions.

> DISCLAIMER: This is experimental and currently in development. GPT-4 gives the best result for this task. Be careful about API consumption. 

## How it works

Input a body description like: 

> "A person sitting in a chair with his left hand up, and the right hand over his leap. His head is straight and has a crossed leg over the other."

And get the pose image proposed by GPT: 

![GPT generated pose image](assets/example.png "GPT generated Pose Image")

You can then use that pose image reference along with [ControlNet](https://github.com/lllyasviel/ControlNet) in Stable Diffusion to generate conditioned pictures.

This is useful when you want to ilustrate a story and you don't know it before hand, therefore the character's posture is also unknown, so you can ask ChatGPT to imagine it, input the body pose description to `gptpose` and get the corresponding pose image template, allowing you to automatically have the assets and build an end-to-end AI powered workflow for image generation using Stable Diffusion along with ControlNet. 

**Note**: The more detailed the pose description, the better the result. 

## Installation 

Run the following command:

> conda env create -f environment.yaml

Which will create a conda env called `gptpose-dev`.

## Usage 

Inside the env, run the following command: 

> gptpose -d "[body_pose_description]" -o "[output_path]/[filename].png" -n "[GPT_model_name]" 

Refer to [models](https://platform.openai.com/docs/models/gpt-4) for the name.