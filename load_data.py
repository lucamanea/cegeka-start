import logging
import pickle

logger = logging.getLogger("flask-app")
CV_OBJ_FILE = "cv.obj"


def load_data_from_file():
    """
    This function checks for the presence of the CV data binary file and ensures
    proper loading.
    :return:
    dict containing the CV data or None if errors are encountered
    """
    logger.info("Deserializing CV data from file")
    cv_data = None

    try:
        with open(CV_OBJ_FILE, "rb") as target_file:
            cv_data = pickle.load(target_file)
    except FileNotFoundError:
        logger.error("File {} does not exist".format(CV_OBJ_FILE))
    except Exception as e:
        logger.error("Failed due to exception: {}".format(e))
    finally:
        return cv_data


if __name__ == "__main__":
    a = load_data_from_file()
    print(a.keys() if a else "error")
