# ----- REQUIRED IMPORTS -----

import os
import cv2
import json
import numpy as np
import helper as he


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


def hold_selection_wrapper(
    image_specific_filepath, image_general_filepath, json_filepath
):
    """
    wrapper function for reading hold selection
    """
    holds_array = []
    clicked_holds = set()
    holds_data = he.read_json(json_filepath)
    if holds_data[0]:
        holds_data = holds_data[1]
        image_filepath = image_specific_filepath[len(image_general_filepath) :]
        if image_filepath in holds_data:
            holds_array = [np.array(hold) for hold in holds_data[image_filepath]]
            print(f"Success: Holds found for {image_filepath}")
        else:
            print(f"Error: No holds found for {image_filepath}")
    else:
        print(f"Error: Unable to read holds from {json_filepath}")

    def mouse_callback(event, x, y, flags, param):
        """
        helper function that handles user hold selection
        """
        if event == cv2.EVENT_LBUTTONDOWN:
            for idx, contour in enumerate(holds_array):
                if cv2.pointPolygonTest(contour, (x, y), False) >= 0:
                    clicked_holds.add(idx)
                    print(f"Success: Clicked on hold: {idx}")

    def render_holds_image():
        """
        helper function that renders an image with OpenCV and allows users to select holds
        """
        try:
            image = cv2.imread(image_specific_filepath)
            if image is None:
                print(f"Error: Unable to read image at {image_specific_filepath}")
                return
            cv2.namedWindow(image_filepath)
            cv2.setMouseCallback(image_filepath, mouse_callback)
            while True:
                display_image = image.copy()
                for idx, contour in enumerate(holds_array):
                    color = (0, 255, 0) if idx not in clicked_holds else (0, 0, 255)
                    cv2.drawContours(display_image, [contour], -1, color, 2)
                cv2.imshow(image_filepath, display_image)
                key = cv2.waitKey(1)
                if key == 27:
                    break
            cv2.destroyAllWindows()
            return (True, clicked_holds)
        except:
            return (False, None)

    return render_holds_image()
