"""Gate 0 Experiment 001: show that flat record absence collapses distinct sensor causes."""

EVENT_FILE_CREATE = 0x01
FILE_F_ID = 0xF0

RAW_EVENT_E = bytes((EVENT_FILE_CREATE, FILE_F_ID))

SENSOR_A = {
    "name": "A",
    "can_observe_event_e": True,
    "drops_event_e": False,
}

SENSOR_B = {
    "name": "B",
    "can_observe_event_e": True,
    "drops_event_e": True,
}

SENSOR_C = {
    "name": "C",
    "can_observe_event_e": False,
    "drops_event_e": False,
}


def observe_event(sensor, raw_event):
    if not sensor["can_observe_event_e"]:
        return None

    if sensor["drops_event_e"]:
        return None

    return raw_event


def run_experiment():
    record_a = observe_event(SENSOR_A, RAW_EVENT_E)
    record_b = observe_event(SENSOR_B, RAW_EVENT_E)
    record_c = observe_event(SENSOR_C, RAW_EVENT_E)

    assert record_a == RAW_EVENT_E
    assert record_b is None
    assert record_c is None

    assert SENSOR_B["can_observe_event_e"] is True
    assert SENSOR_C["can_observe_event_e"] is False

    print(f"A: {record_a!r}")
    print(f"B: {record_b!r}")
    print(f"C: {record_c!r}")


if __name__ == "__main__":
    run_experiment()