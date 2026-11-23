# ESP32 sensor and control interface

Use the ESP32 for timestamped sensor acquisition and bounded low-level interfacing. Keep heavyweight perception/training on a host or edge computer.

## First integration

Select the actual board/SoC and matching [ESP-IDF guide](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/). Record SDK/toolchain version, board revision, serial settings, sensor address, wiring, logic levels, and firmware commit. Consult board/sensor datasheets before choosing pins; no universal wiring is supplied.

Start with one sensor over its supported bus. Emit a simple documented serial record containing protocol version, sequence number, device timestamp and clock unit, sensor ID, measurement/unit, and status. Add host receipt time separately. Detect malformed records, missing sequences, resets, and clock rollover. USB receipt time alone is not the measurement time.

## Motor interface extension

A motor requires an appropriate driver and power design; do not power it from a GPIO. Define PWM/direction semantics, encoder polarity/resolution, command expiry, maximum command magnitude, and reset state. Enforce command bounds and a device-side watchdog even when the host disconnects.

Bring up telemetry first, then an output-disabled command parser, then a constrained bench motor test following the [commissioning gates](../README.md). Verify direction at low command, encoder agreement, timeout, and reset behavior.

## Evidence and alternative

Deliver a board/wiring record, protocol schema, ten-minute acquisition/dropout summary, reset/reconnect observations, and firmware/toolchain manifest. Firmware implementation is future work. Without hardware, implement a synthetic serial-stream producer and host parser that exercise the same malformed/stale/reset cases.
