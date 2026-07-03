# CNN + BiLSTM

User leaving is not a single-frame event. It is a sequence: sitting, standing up, turning, and moving away. `cnn_blstm_pointcloud_training.ipynb` uses CNN + BiLSTM for this type of data.

## Frame-Level Features

The CNN reads one frame of points and extracts spatial features from the point distribution.

## Temporal Modeling

The BiLSTM reads the frame features over time. It can use context from both directions inside a segment, which helps classify the whole action clip.

Typical input shape:

```text
[batch, sequence_length, num_points, point_features]
```

The model output is a class prediction that can be mapped to a security action such as locking the screen or hiding sensitive content.
