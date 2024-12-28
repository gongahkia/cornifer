# ----- REQUIRED IMPORTS -----

import cv2
import numpy as np
import os


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


def identify_contours(target_filepath_array, root_path, output_path):
    """
    identify contours in a specified image and write them to an output path
    """
    contour_data = {}
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
            contour_coordinates = []
            for i in range(len(contours)):
                if hierarchy[0][i][3] != -1:
                    cv2.drawContours(mask, contours, i, (0, 255, 0), 2)
                    contour_coords = contours[i].reshape(-1, 2)
                    contour_coordinates.append(contour_coords.tolist())
            modified_file_path = f"{output_path}{filepath[len(root_path):]}"
            cv2.imwrite(modified_file_path, mask)
            # render(modified_file_path, mask)
            contour_data[os.path.basename(filepath)] = contour_coordinates
        print("Success: Contours identified successfully")
        return (True, contour_data)
    except Exception as e:
        print(f"Error: Unable to run identify_contours: {e}")
        return (False, None)


def hold_selection_wrapper(target_filepath):
    """
    wrapper function for reading hold selection
    """
    holds_array = []

    def mouse_callback(event, x, y, flags, param):
        """
        helper function that handles user hold selection
        """
        if event == cv2.EVENT_LBUTTONDOWN:
            holds_array.append((x, y))
            print(f"Selected hold at: ({x}, {y})")

    def render_holds_image():
        """
        helper function that renders an image with opencv and allows users to select holds
        """
        image = cv2.imread(target_filepath)
        cv2.namedWindow("Image")
        cv2.setMouseCallback("Image", mouse_callback)
        while True:
            for hold in holds_array:
                cv2.circle(image, hold, 5, (0, 255, 0), -1)
            cv2.imshow("Image", image)
            key = cv2.waitKey(1)
            if key == 27:
                break
        cv2.destroyAllWindows()
        return holds_array

    return render_holds_image()
