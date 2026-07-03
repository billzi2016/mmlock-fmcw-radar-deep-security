# Security Scenario

mmLock aims to reduce the exposure window after a user leaves a device. It can act as a sensing trigger for screen lock, sensitive-content hiding, or a stricter protection state.

The threat scenario is simple: the user has left, but the device remains accessible. A nearby person may see or interact with sensitive content.

Radar sensing does not replace passwords, access control, or authentication. It provides a state signal that can make those mechanisms respond sooner.

False alarms and missed detections matter. A false alarm hurts usability; a missed detection leaves the device exposed. Evaluation should separate normal leaving, nearby people, movement angle, speed, height, location, and environment changes.
