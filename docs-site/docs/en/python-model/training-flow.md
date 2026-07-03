# Training Flow

The training notebook starts from point-cloud files, not raw ADC data. FFT preprocessing creates frame-level point clouds; the model notebook turns them into action sequences.

## Inputs

- Point-cloud files: frame-level NPZ or merged HDF5.
- Label CSV: segment labels and frame ranges.

## Steps

```text
load labels
-> load frame-level point clouds
-> normalize features
-> build fixed-length sequences
-> create DataLoaders
-> train CNN + BiLSTM
-> validate
-> run segment inference
```

## Missing for Full Reproduction

The repository still needs dataset layout examples, label samples, train/validation/test split details, and evaluation outputs before it can claim full experimental reproduction.
