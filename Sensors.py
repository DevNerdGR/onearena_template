#IR distance sensor
def measureDistance(index : int = 1) -> float:
    #Hope enabling and disabling donst lag stuff out
    ir_distance_sensor_ctrl.enable_measure(index)
    dat = float(ir_distance_sensor_ctrl.get_distance_info(index))
    ir_distance_sensor_ctrl.disable_measure(index)
    return dat

#Vision marker stuff
class MarkerRecogniser:
    def  __init__(self, detectionDist : float = 1):
        vision_ctrl.enable_detection(rm_define.vision_detection_marker)
        vision_ctrl.set_marker_detection_distance(detectionDist)
        self.rawInfo = []
        self.detectedMarkers = []

    def detect(self):
        self.detectedMarkers = []
        self.rawInfo = vision_ctrl.get_marker_detection_info()
        for i in range(1, self.rawInfo[0] * 5 + 1, 5):
            self.detectedMarkers.append(Marker(self.rawInfo[i], self.rawInfo[i + 1], self.rawInfo[i + 2], self.rawInfo[i + 3], self.rawInfo[i + 4]))
    
    def getDetectCount(self):
        return len(self.detectedMarkers)

    def getMarker(self, idx) -> Marker:
        return self.detectedMarkers[idx]

class Marker: 
    #NOTE: UV coordinate system in use!
    def __init__(self, idx : int, u, v, w, h)
        self.idx = idx
        self.x = u
        self.y = v
        self.w = w
        self.h = h


class MarkerTypeEnum:
    Stop = 1
    Dice = 2
    Target = 3
    Left_Arrow = 4
    Right_Arrow = 5
    Up_Arrow = 6
    Red_Heart = 8

    # Numbers 0-9 (IDs 10–19)
    Zero = 10
    One = 11
    Two = 12
    Three = 13
    Four = 14
    Five = 15
    Six = 16
    Seven = 17
    Eight = 18
    Nine = 19

    # Letters A–Z (IDs 20–45)
    A = 20
    B = 21
    C = 22
    D = 23
    E = 24
    F = 25
    G = 26
    H = 27
    I = 28
    J = 29
    K = 30
    L = 31
    M = 32
    N = 33
    O = 34
    P = 35
    Q = 36
    R = 37
    S = 38
    T = 39
    U = 40
    V = 41
    W = 42
    X = 43
    Y = 44
    Z = 45

    marker_names = [
        None,            # 0
        "Stop",          # 1
        "Dice",          # 2
        "Target",        # 3
        "Left_Arrow",    # 4
        "Right_Arrow",   # 5
        "Up_Arrow",      # 6
        None,            # 7
        "Red_Heart",     # 8
        None,            # 9
        "Zero",          # 10
        "One",           # 11
        "Two",           # 12
        "Three",         # 13
        "Four",          # 14
        "Five",          # 15
        "Six",           # 16
        "Seven",         # 17
        "Eight",         # 18
        "Nine",          # 19
        "A",             # 20
        "B",             # 21
        "C",             # 22
        "D",             # 23
        "E",             # 24
        "F",             # 25
        "G",             # 26
        "H",             # 27
        "I",             # 28
        "J",             # 29
        "K",             # 30
        "L",             # 31
        "M",             # 32
        "N",             # 33
        "O",             # 34
        "P",             # 35
        "Q",             # 36
        "R",             # 37
        "S",             # 38
        "T",             # 39
        "U",             # 40
        "V",             # 41
        "W",             # 42
        "X",             # 43
        "Y",             # 44
        "Z",             # 45
    ]

    def getName(marker_id):
        if 0 <= marker_id < len(MarkerTypeEnum.marker_names):
            return MarkerTypeEnum.marker_names[marker_id]
        return None


#Line following stuff
class LineRecogniser:
    def __init__(self, colour = rm_define.line_follow_color_blue, exposure = rm_define.exposure_value_large):
        vision_ctrl.enable_detection(rm_define.vision_detection_line)
        vision_ctrl.line_follow_color_set(colour)
        media_ctrl.exposure_value_update(exposure)
        self.detectedPoints = []
        self.rawInfo = []

    def detect(self):
        self.detectedPoints = []
        self.rawInfo = vision_ctrl.get_line_detection_info()

        if len(self.rawInfo) == 42:
            for i in range(2, self.rawInfo[0] * 4 + 2, 4):
                self.detectedPoints.append(LinePoint(self.rawInfo[i], self.rawInfo[i + 1], self.rawInfo[i + 2], self.rawInfo[i + 3]))
    
    def getLinePoint(self, idx) -> LinePoint:
        return self.detectedPoints[idx]

class LinePoint:
    def __init__(self, x, y, theta, c):
        self.x = x
        self.y = y
        self.theta = theta
        self.c = c

class LineFollowPID:
    def __init__(self, kp, ki, kd, colour = rm_define.line_follow_color_blue, exposure = rm_define.exposure_value_large):
        self.controller = PIDCtrl()
        self.controller.set_ctrl_params(kp, ki, kd)
        self.lr = LineRecogniser(colour, exposure)
    
    def getCorrection(self):
        #You can feed this directly into the steering command, note that this PID system uses only lateral data of the 5th detected point in the line
        self.lr.detect()
        self.controller.set_error(self.lr.getLinePoint().x - 0.5)
        return self.controller.get_output()
