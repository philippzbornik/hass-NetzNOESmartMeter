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
#
# This is not just an API-load knob: it is the correction deadline for a day
# that Netz NO first delivered as estimates. Once such a day ages out of the
# window it can never be filled in, and while it is only partly inside the
# window a late delivery back-fills part of it - which raises the cumulative
# total by the wrong amount and looks like real data instead of a visible gap.
# Set to 7 so a day has a week to be replaced by measured values.
REIMPORT_DAYS = 7

# Fill hours that have no measured reading from the API's estimatedValues
# (quality "L3"). Off by default: estimates must not silently enter a statistic
# that is compared against a physical meter.
IMPORT_ESTIMATED_VALUES = False
