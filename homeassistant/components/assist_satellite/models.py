"""Models for assist satellite."""

from enum import StrEnum


class AssistSatelliteState(StrEnum):
    """Valid states of an Assist satellite entity."""

    WAITING_FOR_WAKE_WORD = "waiting_for_wake_word"
    """Device is waiting for a wake word."""

    LISTENING_WAKE_WORD = "listening_wake_word"
    """Device is streaming audio for wake word detection to Home Assistant."""

    LISTENING_COMMAND = "listening_command"
    """Device is streaming audio with the voice command to Home Assistant."""

    PROCESSING = "processing"
    """Device has stopped streaming audio and is waiting for Home Assistant to
    process the voice command."""

    RESPONDING = "responding"
    """Device is speaking the response."""
