# DJI RoboMaster Python Wrapper Documentation

## 🚀 Basic Use Cases

This section highlights the most common features you'll use in your RoboMaster code: line following, distance measurement, and marker detection.

---

### 1. `LineFollowPID`

A PID controller wrapper that uses vision-based line following. Automatically uses the x-coordinate of the **5th detected line point** to compute steering corrections.

#### **Usage Example**

```python
lf = LineFollowPID(kp=0.5, ki=0.0, kd=0.1)
correction = lf.getCorrection()
chassis_ctrl.move(0.2, 0, correction)
```

---

### 2. `measureDistance(index=1)`

Measures distance using an IR sensor at the given index.

#### **Usage Example**

```python
dist = measureDistance()
if dist < 0.3:
    chassis_ctrl.stop()
```

---

### 3. `MarkerRecogniser`

Detects vision markers (e.g., arrows, letters, numbers) within a specified range.

#### **Usage Example**

```python
mr = MarkerRecogniser(detectionDist=1.0)
mr.detect()
print("Markers found:", mr.getDetectCount())

for i in range(mr.getDetectCount()):
    marker = mr.getMarker(i)
    print("Detected:", MarkerTypeEnum.getName(marker.idx))
```

---

## 🔍 Class and Method Reference

### `measureDistance(index: int = 1) -> float`

* **Description**: Enables IR distance measurement on the specified port index and returns the measured distance in meters.
* **Note**: Automatically disables the sensor after reading.

---

### `class MarkerRecogniser`

* **Constructor**: `MarkerRecogniser(detectionDist: float = 1.0)`

  * Enables marker detection and sets the maximum detection range.
* **Methods**:

  * `detect()`: Populates the internal marker list from the vision sensor.
  * `getDetectCount() -> int`: Returns the number of detected markers.
  * `getMarker(idx) -> Marker`: Returns the `Marker` object at the given index.

---

### `class Marker`

Represents a single detected marker.

* **Fields**:

  * `idx`: Marker ID (int)
  * `x, y`: UV-coordinates on the screen (float)
  * `w, h`: Width and height of the marker on screen (float)

---

### `class MarkerTypeEnum`

* **Static Data**: Defines known marker IDs and their names.
* **Method**:

  * `getName(marker_id) -> str | None`: Returns a human-readable name of the marker, or `None` if unknown.

---

### `class LineRecogniser`

Handles raw line detection from the vision system.

* **Constructor**: `LineRecogniser(colour, exposure)`

  * `colour`: e.g. `rm_define.line_follow_color_blue`
  * `exposure`: e.g. `rm_define.exposure_value_large`
* **Methods**:

  * `detect()`: Updates the list of detected line points.
  * `getLinePoint(idx) -> LinePoint`: Returns the `LinePoint` at index `idx`.

---

### `class LinePoint`

Represents a point detected on the line.

* **Fields**:

  * `x, y`: Position in UV space
  * `theta`: Tangential angle
  * `c`: Curvature

---

### `class LineFollowPID`

Provides PID-based correction output for line following.

* **Constructor**: `LineFollowPID(kp, ki, kd, colour, exposure)`
* **Method**:

  * `getCorrection() -> float`: Returns PID output based on lateral error from the 5th detected line point.
  * **Note**: You can plug this directly into steering commands.

---
