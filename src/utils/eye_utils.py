from scipy.spatial import distance

def eye_aspect_ratio(eye):
    """
    Calculate the Eye Aspect Ratio (EAR) for drowsiness detection.
    """
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear