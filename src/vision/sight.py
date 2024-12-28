# ----- REQUIRED IMPORTS -----

import cv2
import numpy as np


def render(target_filepath, mask):
    """
    render a specified image with opencv
    """
    try:
        cv2.imshow(target_filepath, mask)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return True
    except:
        return False


# ----- HELPER FUNCTIONS -----


def identify_contours(target_filepath_array, root_path, output_path="./identified/"):
    """
    identify contours in a specified image and write them to an output path
    """
    try:
        for filepath in target_filepath_array:
            image = cv2.imread(filepath)
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
            _, thresholded_image = cv2.threshold(
                blurred_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
            )
            contours, hierarchy = cv2.findContours(
                thresholded_image, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE
            )
            mask = np.zeros_like(image)
            for i in range(len(contours)):
                if hierarchy[0][i][3] != -1:
                    cv2.drawContours(mask, contours, i, (0, 255, 0), 2)
            modified_file_path = f"{output_path}{filepath[len(root_path):]}"
            cv2.imwrite(modified_file_path, mask)
            # render(modified_file_path, mask)
        return True
    except:
        print("Error: Unable to run identify_contours")
        return False
