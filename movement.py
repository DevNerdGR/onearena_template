def setTranslationalSpeed(x:int): #set translational speed in m/s
    chassis_ctrl.set_trans_speed(x)

def setRotationalSpeed(angle:int): #set rotational speed in degree/s, clockwise
    chassis_ctrl.set_rotate_speed(angle)

def translate(angle:int, x:int): #degrees, distance, clockwise
    chassis_ctrl.move_with_distance(angle, x)

def rotateCW(duration:int): #rotate clockwise for certain amt of time
    chassis_ctrl.rotate_with_time(rm_define.clockwise, duration)

def rotateACW(duration:int): #rotate anticlockwise for certain amt of time
    chassis_ctrl.rotate_with_time(rm_define.anticlockwise, duration)

def setFree(): #gimbal and chassis moves independently from each other
    rm_define.robot_mode_free

def setFollowGimbal(): #chassis follows gimbal direction
    rm_define.robot_mode_chassis_follow

def setFollowChassis(): #gimbal follows chassis direction
    rm_define.robot_mode_gimbal_follow

def setGimbalRotationSpeed(x:int): #set the speed of the gimbal's rotation
    gimbal_ctrl.set_rotate_speed(x)

def gimbalRotateLeft(degree: int):
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left, degree)

def gimbalRotateRight(degree: int):
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right, degree)

def gimbalRotateUp(degree: int):
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_up, degree)

def gimbalRotateDown(degree: int):
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_down, degree)
    
def rotateGimbalBy(yaw:int, pitch:int):
    gimbal_ctrl.angle_ctrl(yaw, pitch)

def setGelBulletCount(x:int):
    gun_ctrl.set_fire_count(x)

def setLaserBulletCount(x:int):
    ir_blaster_ctrl.set_fire_count(x)

def fireGel():
    gun_ctrl.fire_once()

def fireLaser():
    ir_blaster_ctrl.fire_once()

def getArmPos(): #in mm
    return robotic_arm_ctrl.get_position

def recenterArm():
    robotic_arm_ctrl.recenter()

def moveArm(x: int, y: int): #relative
    robotic_arm_ctrl.move(x, y, wait_for_complete=True)

def moveArmTo(x: int, y: int): #absolute
    robotic_arm_ctrl.move(x, y, wait_for_complete=True)

def setGripperStrength(strength: int):
    gripper_ctrl.update_power_level(strength)

def openGripper():
    gripper_ctrl.open()

def closeGripper():
    gripper_ctrl.close()

def isOpen():
    return gripper_ctrl.is_open()

def toggleGripper():
    if isOpen():
        openGripper()
    else: closeGripper()
