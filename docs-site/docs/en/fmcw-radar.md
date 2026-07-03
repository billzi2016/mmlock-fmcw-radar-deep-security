# FMCW Radar

FMCW means `Frequency-Modulated Continuous Wave`. Instead of sending one short pulse, the radar transmits a continuous signal whose frequency changes over time. One such sweep is called a `chirp`.

The received echo is delayed because it traveled to the target and back. When the radar mixes the transmitted signal with the received signal, it obtains a frequency difference called the `beat frequency`.

## Range, Velocity, and Angle

The farther the target is, the larger the delay. Since the chirp frequency is changing over time, a larger delay creates a larger beat frequency.

```text
range = c * beat_frequency / (2 * slope)
```

Velocity is estimated across multiple chirps. Moving targets create phase changes along the slow-time dimension, so Doppler FFT can recover velocity-related components.

Angle is estimated across virtual antennas. TX/RX channels form an antenna array, and phase differences across that array reveal direction.

The project code follows this chain:

```text
range_fft(frame_cube)
-> doppler_fft(range_cube)
-> angle_fft(doppler_cube)
```

## What TX and RX Mean

`TX` means transmit antenna. `RX` means receive antenna. TX antennas send chirps; RX antennas receive reflections from people, desks, walls, and other objects.

With 3 TX and 4 RX antennas, the radar can form:

```text
3 * 4 = 12 TX/RX channels
```

In TDM-MIMO, TX antennas transmit in turn rather than all at once:

```mermaid
flowchart LR
  F[One frame] --> L1[Loop 1]
  L1 --> C11[TX1 chirp]
  C11 --> C12[TX2 chirp]
  C12 --> C13[TX3 chirp]
  F --> L2[Loop 2]
  L2 --> C21[TX1 chirp]
  C21 --> C22[TX2 chirp]
  C22 --> C23[TX3 chirp]
```

Each chirp is received by all RX antennas, so one frame can be reshaped as:

```text
[loop, tx, rx, sample]
```

The `angle_fft` implementation flattens TX/RX into virtual antennas:

```text
[doppler_bin, tx, rx, range_bin]
-> [doppler_bin, virtual_antennas, range_bin]
```

The order matters. Angle estimation depends on the phase relationship across the antenna array, so strict reproduction should use calibrated virtual antenna geometry.

```mermaid
flowchart LR
  A["Raw ADC stream"] --> B["frame cube<br/>[loop, tx, rx, sample]"]
  B --> C["Range FFT<br/>[loop, tx, rx, range_bin]"]
  C --> D["Doppler FFT<br/>[doppler_bin, tx, rx, range_bin]"]
  D --> E["Virtual antenna reshape"]
  E --> F["Angle FFT<br/>[doppler_bin, angle_bin, range_bin]"]
  F --> G["Point detection"]
```
