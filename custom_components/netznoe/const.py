"""Component constants for Netz NO Smartmeter."""
DOMAIN = "netznoe"

CONF_METERING_POINTS = "metering_points"


def is_meter_active(metering_point_data: dict) -> bool:
    """Check if a specific metering point is an active smart meter."""
    has_smart = metering_point_data.get("smartMeterType") is not None
    is_active = not metering_point_data.get("locked", False)
    return has_smart and is_active


# --- Import behaviour (see issues #3 / #4) -------------------------------------
# NOTE: stage 1 keeps these as module constants so the behaviour can be tested by
# editing one file. They belong in the options flow before this goes upstream.

# Re-import this many trailing days on every run instead of resuming exactly at
# the last written statistic. Because the recorder upserts per start timestamp,
# already-written hours can be corrected later. 0 restores the old behaviour.
# Kept small on purpose: the day loop makes one API call per day, and 14 days
# per run appeared to get throttled by Netz NO (every second run returned no
# data at all).
REIMPORT_DAYS = 3

# Fill hours that have no measured reading from the API's estimatedValues
# (quality "L3"). Off by default: estimates must not silently enter a statistic
# that is compared against a physical meter.
IMPORT_ESTIMATED_VALUES = False
