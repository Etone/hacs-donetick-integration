from homeassistant import core


async def async_setup(hass: core.HomeAssistant, config: dict) -> bool:
    """Set up the Donetick Custom component."""
    hass.states.async_set("donetick.test", "test")
    return True
