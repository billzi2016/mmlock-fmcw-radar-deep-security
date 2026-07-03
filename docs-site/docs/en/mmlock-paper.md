# mmLock Paper

The paper is titled *mmLock: User Leaving Detection Against Data Theft via High-Quality mmWave Radar Imaging*. It targets a narrow but practical security gap: a user may leave a device before the device is locked.

mmLock uses mmWave radar to sense the leaving process. The radar signal is processed into a human representation, a model detects whether the user is leaving, and the system can trigger data-protection actions.

![mmLock system figure](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/embedded/pdf_image-002-001.png)

## Notebook Link

`mmlock_c61_paper_reading_zh.ipynb` breaks the paper into system flow, threat model, point-cloud generation, three FFT stages, virtual antennas, denoising, PointNet/LSTM modeling, and experiment notes.

## Boundary

mmLock is a sensing trigger for security actions. It does not replace authentication, access control, or permission management. False alarms and missed detections matter, especially when nearby people or environmental reflections affect the radar signal.
