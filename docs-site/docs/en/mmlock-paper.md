# mmLock Paper

The paper is titled *mmLock: User Leaving Detection Against Data Theft via High-Quality mmWave Radar Imaging*. It targets a narrow but practical security gap: a user may leave a device before the device is locked.

## Paper Information

- Repository PDF: [`C61.pdf`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/blob/main/C61.pdf)
- Authors: Jiawei Xu, Ziqian Bi, Amit Singha, Tao Li, Yimin Chen, Yanchao Zhang
- Venue: 2023 32nd International Conference on Computer Communications and Networks (ICCCN)
- DOI: https://doi.org/10.1109/ICCCN58024.2023.10230151
- ASU record: https://asu.elsevierpure.com/en/publications/mmlock-user-leaving-detection-against-data-theft-via-high-quality/
- Public PDF source: [ASU CNSG public PDF](https://labs.engineering.asu.edu/cnsg/wp-content/uploads/sites/147/2024/02/C61.pdf)

mmLock uses mmWave radar to sense the leaving process. The radar signal is processed into a human representation, a model detects whether the user is leaving, and the system can trigger data-protection actions.

![mmLock system figure](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/embedded/pdf_image-002-001.png)

## Notebook Link

`mmlock_c61_paper_reading_zh.ipynb` breaks the paper into system flow, threat model, point-cloud generation, three FFT stages, virtual antennas, denoising, PointNet/LSTM modeling, and experiment notes.

## Boundary

mmLock is a sensing trigger for security actions. It does not replace authentication, access control, or permission management. False alarms and missed detections matter, especially when nearby people or environmental reflections affect the radar signal.
