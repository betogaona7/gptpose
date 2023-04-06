POSE_VALUES_TEMPLATE="""
Imagine you are an OpenPose user expert, and you have the following two lists:

Candidate = [[241,77],[241,120],[191,118],[177,183],[163,252],[298,118],[317,182],[332,245],[225,241],[213,359],[215,454],[270,240],[282,360],[286,456],[232,59],[253,60],[225,70],[260,72]] 
Subset = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]]

The Candidate is a 2D list with the COCO model keypoint coordinates (x,y) that represent the joints and extremities locations of a default body skeleton on a 512x512 canvas. Subset is a 2D list with 18 indices per row; each index represents a visible keypoint coordinate, and missing keypoints are set to -1. 

Both lists are part of the input to OpenPose's draw_bodypose function which draws the body on the canvas. 

Your task is to update the Candidate keypoint coordinates to match as exactly as possible the next body pose description keeping consistency on the limbs connections defined in the limbSeq variable of draw_bodypose, also update the Subset list with -1 for those keypoints that may not be visible. 

So, 1) understand the keypoint indices in the Candidate list, 2) analyze the body pose description and determine which keypoints should be moved, removed, or kept as-is. 3) update the coordinates of the Candidate list based on the body pose description and 4) update the Subset list to reflect any missing or non-visible keypoints. Your output should be the Candidate and Subset lists in one line for each one, no explication is needed nor answer introductions, just the lists. Repeat internally your process at least 3 times until you are sure you have your best attempt and then display the output.

body pose description: {pose_description}
"""
