POSE_VALUES_TEMPLATE="""
First, use OpenPose joints, and geometrically describe the body joints' positions with their angles of the next person's description:

{pose_description} 

Second, using your answer to the first point, use the draw_bodypose function from OpenPose as a reference to ONLY create the candidate and subset lists that represent the body's pose on a canvas of 512x512. You can just draw the upper body part, the low body part, or the full body depending on what suits the body joints' descriptions better, and expresses the person's action.

Regarding the output, the candidate must be a 2D list with shape (n, 2), where n is the number of keypoints with its x and y coordinates, e.g.,[x, y].  The x and y coords should
integers corresponding to the pixel positions on the canvas. Subset must be a 2D list with shape (m, 18), where m is the number of persons in the description. Each row contains 
the indices of the keypoints in the candidate list that form a person's pose. The length of each row should be 18 and If a keypoint is missing for a person, its index should be set to -1 in the subset list.

Avoid explanations or answer introductions. Don't display item descriptions neither the first answer.
"""
