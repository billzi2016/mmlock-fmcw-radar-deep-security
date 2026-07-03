# Point Cloud

A radar point is evidence of a strong reflection at a certain range, velocity, and angle. It is not a pixel. It is a compact representation extracted from the radar cube.

`point_cloud.py` outputs:

| Field | Meaning |
| --- | --- |
| `range_m` | range in meters |
| `velocity_mps` | radial velocity |
| `angle_deg` | estimated angle |
| `power_db` | reflection strength |
| `doppler_bin` | Doppler bin |
| `angle_bin` | angle bin |
| `range_bin` | range bin |

Point clouds are useful because leaving is a temporal process. One frame shows a moment; a sequence shows motion. That is why the model workflow feeds point-cloud sequences into CNN + BiLSTM.
