# Radar Basics

Radar sends electromagnetic waves, receives reflections, and estimates what is around it from the returned signal. The basic idea is simple, but the data is not a photo. Radar produces measurements such as range, velocity, angle, and reflection strength.

Range comes from propagation delay. A signal travels from the radar to the target and back. If the propagation speed is known, the delay can be converted into distance.

Velocity comes from phase or frequency changes across repeated measurements. A person moving toward or away from the radar leaves a different temporal pattern from a static object.

Angle comes from antenna arrays. The same reflection reaches different antennas with slightly different phases, and those phase differences contain direction information.

## Why mmWave Radar Fits This Project

mmWave radar is useful for short-range human sensing. It can capture movement without directly recording visible-light images. For mmLock, the key question is whether the user is leaving, not what the user's face or screen looks like.

Radar still has limits. Body pose, environmental reflection, multiple people, and sensor placement all affect the signal. The later FFT, point-cloud, and model steps exist because raw reflections need careful processing before they become useful behavior evidence.
