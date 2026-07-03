# Wireless Sensing

Wireless sensing starts from a simple fact: people and objects change wireless signals. When a person stands up, turns, walks, or moves away from a device, the propagation paths, reflections, phases, and amplitudes change.

mmLock uses mmWave FMCW radar, but it belongs to a broader family that also includes WiFi CSI sensing, UWB, RFID, acoustic sensing, and radar sensing.

## Shared Structure

Most wireless sensing systems follow this path:

```text
transmit a known signal
-> the signal interacts with people and the environment
-> receive the changed signal
-> extract features
-> infer position, motion, or state
```

The measured changes may include amplitude, phase, Doppler-related frequency shifts, or multipath structure.

## Why WiFi Sensing Feels Similar

WiFi CSI describes the wireless channel between transmitter and receiver. A moving body blocks, reflects, or scatters WiFi signals, so CSI amplitude and phase change over time.

FMCW radar also transmits a signal and reads the changed return. A human body reflects mmWave signals, and the return contains range, velocity, angle, and power information.

| Aspect | WiFi CSI | FMCW Radar |
| --- | --- | --- |
| Uses wireless propagation | Yes | Yes |
| Affected by body movement | Yes | Yes |
| Affected by multipath | Yes | Yes |
| Can detect presence or motion | Yes | Yes |
| Needs signal processing and modeling | Yes | Yes |

At the high level, both systems observe that people move and wireless signals change.

## The Important Difference

WiFi is primarily a communication system. Sensing with WiFi means extracting behavior clues from communication-channel measurements.

FMCW radar is designed for sensing. Its chirps make range, velocity, and angle estimation much more direct:

```text
raw ADC
-> Range FFT
-> Doppler FFT
-> Angle FFT
-> point cloud
-> sequence model
```

This is why mmLock is built around high-quality mmWave radar imaging rather than generic wireless disturbance detection. The task is not only to know that something moved, but to understand whether the user is leaving the device.

## Limits

Wireless sensing is not magic. Multipath, multiple people, body pose, sensor placement, and environment changes all matter. A good document should keep mmLock tied to its actual task: user-leaving detection for data protection.
